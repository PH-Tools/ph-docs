/**
 * Remark plugin that transforms MkDocs-style admonitions
 * (!!! type "title") into styled HTML callout blocks.
 *
 * Syntax:
 *   !!! warning "Title here"
 *       Body text with **inline** formatting.
 *
 * Produces:
 *   <div class="callout callout--warning">
 *     <div class="callout__title">Title here</div>
 *     <div class="callout__body"><p>Body text…</p></div>
 *   </div>
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
  value?: string;
  children?: MdastNode[];
}

const ADMONITION_RE = /^!!!\s+(\w+)(?:\s+"([^"]*)")?/;

export default function remarkAdmonitions() {
  return (tree: MdastNode) => {
    function walk(node: MdastNode) {
      if (!node.children) return;

      const newChildren: MdastNode[] = [];

      for (let i = 0; i < node.children.length; i++) {
        const child = node.children[i];

        if (
          child.type === "paragraph" &&
          child.children?.length &&
          child.children[0].type === "text" &&
          ADMONITION_RE.test(child.children[0].value || "")
        ) {
          const firstText = child.children[0].value || "";
          const match = firstText.match(ADMONITION_RE)!;
          const admonType = match[1];
          const title =
            match[2] ||
            admonType.charAt(0).toUpperCase() + admonType.slice(1);

          // Strip the !!! line from the first text node
          const firstLineEnd = firstText.indexOf("\n");
          let remaining = "";
          if (firstLineEnd !== -1) {
            remaining = firstText
              .substring(firstLineEnd + 1)
              .replace(/^    /gm, ""); // strip MkDocs 4-space indent
          }

          // Build body children: modified first text + remaining inline nodes
          const bodyChildren: MdastNode[] = [];
          if (remaining) {
            bodyChildren.push({ type: "text", value: remaining });
          }
          for (let j = 1; j < child.children.length; j++) {
            bodyChildren.push(child.children[j]);
          }

          // Emit open → body paragraph → close
          newChildren.push({
            type: "html",
            value: `<div class="callout callout--${escapeHtml(admonType)}"><div class="callout__title">${escapeHtml(title)}</div><div class="callout__body">`,
          });

          if (bodyChildren.length > 0) {
            newChildren.push({
              type: "paragraph",
              children: bodyChildren,
            });
          }

          newChildren.push({
            type: "html",
            value: `</div></div>`,
          });

          continue;
        }

        // Recurse into non-admonition nodes
        walk(child);
        newChildren.push(child);
      }

      node.children = newChildren;
    }

    walk(tree);
  };
}
