from pydantic import BaseModel


class Game(BaseModel):
    MinimapScale: float = 1.0


class Input(BaseModel):
    evtCastSpell4: list[str] = []
    evtCastSpell3: list[str] = []
    evtCastSpell2: list[str] = []
    evtCastSpell1: list[str] = []


class LiveClientConfig(BaseModel):
    game: Game
    input: Input
