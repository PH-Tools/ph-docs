import fs from "node:fs";
import path from "node:path";
import yaml from "js-yaml";

export interface LibraryMeta {
  id: string;
  repo: string;
  label: string;
  docs_path: string;
  branch: string;
  enabled: boolean;
  index: string;
  tag_line: string;
  category: string;
  description: string;
}

export interface GuideMeta {
  id: string;
  label: string;
  href: string;
  enabled: boolean;
  index: string;
  tag_line: string;
  category: string;
  description: string;
}

interface LibrariesFile {
  libraries: LibraryMeta[];
  guides?: GuideMeta[];
}

const LIBRARIES_PATH = path.resolve(process.cwd(), "libraries.yml");

let _cache: LibraryMeta[] | null = null;

export function getLibraries(): LibraryMeta[] {
  if (_cache) return _cache;
  const raw = fs.readFileSync(LIBRARIES_PATH, "utf-8");
  const data = yaml.load(raw) as LibrariesFile;
  _cache = (data.libraries ?? []).filter((lib) => lib.enabled !== false);
  return _cache;
}

export function getLibrary(id: string): LibraryMeta | undefined {
  return getLibraries().find((lib) => lib.id === id);
}

let _guidesCache: GuideMeta[] | null = null;

export function getGuides(): GuideMeta[] {
  if (_guidesCache) return _guidesCache;
  const raw = fs.readFileSync(LIBRARIES_PATH, "utf-8");
  const data = yaml.load(raw) as LibrariesFile;
  _guidesCache = (data.guides ?? []).filter((g) => g.enabled !== false);
  return _guidesCache;
}
