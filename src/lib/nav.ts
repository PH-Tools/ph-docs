import fs from "node:fs";
import path from "node:path";
import yaml from "js-yaml";

export interface NavLeaf {
  label: string;
  path: string;
}

export interface NavGroup {
  label: string;
  children: NavItem[];
}

export type NavItem = NavLeaf | NavGroup;
export type NavTree = NavItem[];

export function isLeaf(item: NavItem): item is NavLeaf {
  return "path" in item;
}

export function isGroup(item: NavItem): item is NavGroup {
  return "children" in item;
}

/**
 * Parse a single nav.yml entry. MkDocs nav format:
 *   - Label: path.md          → NavLeaf
 *   - Label:                  → NavGroup
 *     - Child: child.md
 */
function parseNavItem(item: unknown): NavItem | null {
  if (typeof item !== "object" || item === null) return null;

  const entries = Object.entries(item as Record<string, unknown>);
  if (entries.length !== 1) return null;

  const [label, value] = entries[0];

  // Leaf: { "Label": "path.md" }
  if (typeof value === "string") {
    return { label, path: value };
  }

  // Group: { "Label": [ ... ] }
  if (Array.isArray(value)) {
    const children = value
      .map((child) => parseNavItem(child))
      .filter((c): c is NavItem => c !== null);
    return { label, children };
  }

  return null;
}

/**
 * Parse a nav.yml file into a NavTree.
 */
export function parseNavYaml(filePath: string): NavTree {
  const raw = fs.readFileSync(filePath, "utf-8");
  const data = yaml.load(raw) as { nav?: unknown[] };
  if (!data?.nav || !Array.isArray(data.nav)) return [];

  return data.nav
    .map((item) => parseNavItem(item))
    .filter((item): item is NavItem => item !== null);
}

/**
 * Load the nav tree for a given library id.
 * Returns an empty array if nav.yml doesn't exist.
 */
export function getNavTree(libId: string): NavTree {
  const navPath = path.resolve(
    process.cwd(),
    `src/content/docs/${libId}/nav.yml`,
  );
  if (!fs.existsSync(navPath)) return [];
  return parseNavYaml(navPath);
}

/**
 * Get the first file path from each top-level NavGroup.
 * Used to locate section card front-matter.
 */
export function getFirstFilePerGroup(
  tree: NavTree,
): { groupLabel: string; filePath: string }[] {
  const results: { groupLabel: string; filePath: string }[] = [];

  for (const item of tree) {
    if (!isGroup(item)) continue;
    const firstLeaf = findFirstLeaf(item.children);
    if (firstLeaf) {
      results.push({ groupLabel: item.label, filePath: firstLeaf.path });
    }
  }

  return results;
}

function findFirstLeaf(items: NavItem[]): NavLeaf | null {
  for (const item of items) {
    if (isLeaf(item)) return item;
    if (isGroup(item)) {
      const found = findFirstLeaf(item.children);
      if (found) return found;
    }
  }
  return null;
}

/**
 * Collect all leaf paths from the nav tree (for getStaticPaths).
 */
export function getAllLeafPaths(tree: NavTree): NavLeaf[] {
  const leaves: NavLeaf[] = [];

  function walk(items: NavItem[]) {
    for (const item of items) {
      if (isLeaf(item)) leaves.push(item);
      else if (isGroup(item)) walk(item.children);
    }
  }

  walk(tree);
  return leaves;
}

/**
 * Find the top-level group label that contains a given leaf path.
 * Returns null if the leaf is at the top level (not inside a group).
 */
export function findParentGroupLabel(
  tree: NavTree,
  targetPath: string,
): string | null {
  for (const item of tree) {
    if (!isGroup(item)) continue;
    if (groupContainsLeaf(item.children, targetPath)) return item.label;
  }
  return null;
}

function groupContainsLeaf(items: NavItem[], targetPath: string): boolean {
  for (const item of items) {
    if (isLeaf(item) && item.path === targetPath) return true;
    if (isGroup(item) && groupContainsLeaf(item.children, targetPath))
      return true;
  }
  return false;
}
