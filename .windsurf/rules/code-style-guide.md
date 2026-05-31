---
trigger: model_decision
description: When code is written, enforce this style guide.
---

# Code Style Guide

## Type Hints

- **Use subtle typing** - only add type hints where they provide clear value
- **No `-> None`** - never add explicit `-> None` return type annotations
- **Return types only when complex** - add return type hints only when:
  - The return type is not obvious from the implementation
  - The method is abstract and needs a defined interface
  - The function is a public API with complex return logic
- **Parameter types when helpful** - add parameter type hints when:
  - The parameter type is not obvious from usage
  - The parameter accepts multiple types
  - The type helps IDE autocomplete significantly

**Examples:**

```python
# Good - no return type, simple getter
def get_restriction(self):
    return self._restriction

# Good - parameter type helpful
def block_key(self, key: str):
    with self._lock:
        self._blocked_keys.add(key)

# Good - return type needed for abstract method
@abstractmethod
def _condition_met(self, live_client_data: LiveClientData) -> bool:
    pass

# Good - class attribute typing
class Quest(ABC):
    describtion: str
    difficulty: Difficulty
    tags: list[str]
```

## Naming Conventions

- **Classes:** PascalCase (`QuestManager`, `KeyboardController`)
- **Functions/Methods:** snake_case (`get_config`, `block_key`, `parse_hotkey`)
- **Private members:** underscore prefix (`_duration`, `_time_left`, `_update_time`)
- **Constants:** UPPER_SNAKE_CASE (`KEY_MAPPING`)

## Import Style

- Standard library imports first
- Third-party imports second
- Local imports third
- Use relative imports within the package (`from ..data import LiveClientData`)

## Modern Python

- Use modern type syntax: `list[str]` instead of `List[str]`
- Use `dict[str, int]` instead of `Dict[str, int]`
- Avoid importing from `typing` unless using special types like `Union`, `Optional`, etc.

## Code Organization

- Use abstract base classes (`ABC`) for interfaces
- Use pydantic `BaseModel` for data models
- Private methods start with underscore
- Public methods have no underscore prefix
- Group related methods together

## Threading

- Use daemon threads for background monitoring
- Always use locks (`threading.Lock`) for shared state
- Use context managers for lock acquisition

## Minimal Documentation

- No docstrings needed
- Code should be self-explanatory
- Add comments only for non-obvious logic
