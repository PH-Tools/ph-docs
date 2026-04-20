/**
 * Remark plugin that transforms ```mermaid``` code blocks into
 * <div class="mermaid"> containers for client-side rendering.
 */

function escapeHtml(text: string): string {
  return text
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

interface MdastNode {
  type: string;
  lang?: string;
  value?: string;
  children?: MdastNode[];
}

export default function remarkMermaid() {
  return (tree: MdastNode) => {
    function walk(node: MdastNode) {
      if (!node.children) return;
      for (let i = 0; i < node.children.length; i++) {
        const child = node.children[i];
        if (child.type === "code" && child.lang === "mermaid") {
          node.children[i] = {
            type: "html",
            value: `<div class="mermaid" data-pagefind-ignore>\n${escapeHtml(child.value || "")}\n</div>`,
          };
        } else {
          walk(child);
        }
      }
    }
    walk(tree);
  };
}
