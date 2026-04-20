import fs from "node:fs";
import path from "node:path";
import matter from "gray-matter";

export interface LibraryIndexFrontmatter {
  title: string;
  subtitle?: string;
  version?: string;
  pills?: string[];
}

export interface SectionCardFrontmatter {
  title: string;
  card_title?: string;
  card_description?: string;
  card_index?: string;
}

/**
 * Read front-matter from a markdown file.
 * Returns the parsed data, or an empty object if the file doesn't exist.
 */
export function readFrontmatter<T extends Record<string, unknown>>(
  filePath: string,
): T {
  if (!fs.existsSync(filePath)) return {} as T;
  const raw = fs.readFileSync(filePath, "utf-8");
  const { data } = matter(raw);
  return data as T;
}

/**
 * Read front-matter from a library's index.md.
 */
export function getLibraryIndexFrontmatter(
  libId: string,
): LibraryIndexFrontmatter {
  const indexPath = path.resolve(
    process.cwd(),
    `src/content/docs/${libId}/index.md`,
  );
  return readFrontmatter<LibraryIndexFrontmatter>(indexPath);
}

/**
 * Read section card front-matter from a specific doc file.
 */
export function getSectionCardFrontmatter(
  libId: string,
  relPath: string,
): SectionCardFrontmatter {
  const filePath = path.resolve(
    process.cwd(),
    `src/content/docs/${libId}/${relPath}`,
  );
  return readFrontmatter<SectionCardFrontmatter>(filePath);
}
