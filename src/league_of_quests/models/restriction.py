from ..core import RestrictionEffect


class Restriction:
    def __init__(self, description: str, tags: list[str], effect: RestrictionEffect):
        self.description = description
        self.tags = tags
        self._effect = effect

    def activate(self):
        pass

    def update(self, dt: float):
        pass

    def deactivate(self):
        pass
