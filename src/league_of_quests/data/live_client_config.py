from typing import Annotated

from pydantic import BaseModel, BeforeValidator


def validate_float(value: str) -> float:
    try:
        return float(value)
    except ValueError:
        return 1.0


def validate_int(value: str) -> int:
    try:
        return int(value)
    except ValueError:
        return 0


class Game(BaseModel):
    MinimapScale: Annotated[float, BeforeValidator(validate_float)] = 1.0
    GlobalScale: Annotated[float, BeforeValidator(validate_float)] = 0.0
    FlipMiniMap: Annotated[int, BeforeValidator(validate_int)] = 0
    Width: Annotated[int, BeforeValidator(validate_int)] = 2560
    Height: Annotated[int, BeforeValidator(validate_int)] = 1440


class Input(BaseModel):
    evtCastSpell4: list[str]
    evtCastSpell3: list[str]
    evtCastSpell2: list[str]
    evtCastSpell1: list[str]


class LiveClientConfig(BaseModel):
    game: Game
    input: Input
