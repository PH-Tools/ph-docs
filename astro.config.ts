import { defineConfig } from "astro/config";
import remarkMermaid from "./src/plugins/remark-mermaid";
import remarkAdmonitions from "./src/plugins/remark-admonitions";

export default defineConfig({
  output: "static",
  site: "https://docs.passivehousetools.com",
  markdown: {
    remarkPlugins: [remarkAdmonitions, remarkMermaid],
  },
});
