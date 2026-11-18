from __future__ import annotations
from typing import Any

def _resolve(root: dict[str, Any], ref: str) -> dict[str, Any]:
    value: Any = root
    for part in ref.removeprefix("#/").split("/"):
        value = value[part.replace("~1", "/").replace("~0", "~")]
    return value

def validate(instance: Any, schema: dict[str, Any], *, root: dict[str, Any] | None = None, path: str = "$") -> list[str]:
    root = root or schema; errors: list[str] = []
    if "$ref" in schema: return validate(instance, _resolve(root, schema["$ref"]), root=root, path=path)
    if "const" in schema and instance != schema["const"]: errors.append(f"{path}: expected constant {schema['const']!r}")
    if "enum" in schema and instance not in schema["enum"]: errors.append(f"{path}: value is outside enum")
    expected = schema.get("type")
    allowed = expected if isinstance(expected, list) else [expected] if expected else []
    names = {"object":dict,"array":list,"string":str,"number":(int,float),"integer":int,"boolean":bool,"null":type(None)}
    if allowed and not any(isinstance(instance, names[k]) and not (k in {"number","integer"} and isinstance(instance,bool)) for k in allowed):
        return [f"{path}: expected {' or '.join(allowed)}"]
    if isinstance(instance, dict):
        for key in schema.get("required", []):
            if key not in instance: errors.append(f"{path}: missing {key}")
        for key, value in instance.items():
            if key in schema.get("properties", {}): errors += validate(value, schema["properties"][key], root=root, path=f"{path}.{key}")
        if "anyOf" in schema and not any(not validate(instance, option, root=root, path=path) for option in schema["anyOf"]): errors.append(f"{path}: no anyOf branch matched")
    if isinstance(instance, list):
        if len(instance) < schema.get("minItems", 0): errors.append(f"{path}: too few items")
        if "maxItems" in schema and len(instance) > schema["maxItems"]: errors.append(f"{path}: too many items")
        if schema.get("uniqueItems") and len({repr(v) for v in instance}) != len(instance): errors.append(f"{path}: duplicate items")
        for index, subschema in enumerate(schema.get("prefixItems", [])):
            if index < len(instance): errors += validate(instance[index], subschema, root=root, path=f"{path}[{index}]")
        if isinstance(schema.get("items"), dict):
            for index, value in enumerate(instance): errors += validate(value, schema["items"], root=root, path=f"{path}[{index}]")
    if isinstance(instance, (int,float)) and not isinstance(instance,bool):
        if instance < schema.get("minimum", instance): errors.append(f"{path}: below minimum")
        if instance > schema.get("maximum", instance): errors.append(f"{path}: above maximum")
    if isinstance(instance, str) and len(instance) < schema.get("minLength", 0): errors.append(f"{path}: too short")
    return errors
