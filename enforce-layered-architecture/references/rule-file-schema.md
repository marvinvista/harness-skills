# Rule File Schema

The checker expects JSON with:

- `allowed_direction`: `"forward"` or `"backward"` relative to `layer_order`
- `layer_order`: ordered array of layer names from lowest to highest
- `layers`: object mapping each layer name to path prefixes in the repo

Example:

```json
{
  "allowed_direction": "forward",
  "layer_order": ["types", "service", "ui"],
  "layers": {
    "types": ["src/types/"],
    "service": ["src/service/"],
    "ui": ["src/ui/"]
  }
}
```
