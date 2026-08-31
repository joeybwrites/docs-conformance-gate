---
title: Block-list frontmatter arrays
content-type: lifecycle-map
assumes:
  - skill
  - connector
canonical_for:
  - plugin
---
# Plugins

Skills, connectors, and plugins are all declared in block-list frontmatter, so
no S4 findings and no FM finding: the parser must accept YAML block-list arrays,
not only inline `[a, b]` arrays.
