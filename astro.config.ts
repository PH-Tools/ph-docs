import { defineConfig } from "astro/config";
import remarkMermaid from "./src/plugins/remark-mermaid";

export default defineConfig({
  output: "static",
  site: "https://docs.passivehousetools.com",
  markdown: {
    remarkPlugins: [remarkMermaid],
  },
});
