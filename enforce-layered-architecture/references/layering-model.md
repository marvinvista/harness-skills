# Layering Model

One common forward-only layer order is:

`types -> config -> repo -> service -> runtime -> ui`

Interpretation:
- lower layers should not import higher layers
- cross-cutting concerns should enter through explicit seams
- utilities should not become an unbounded escape hatch

If your repo uses the opposite dependency direction, keep the same `layer_order` but set `allowed_direction` to `"backward"` in the rule file.
