class MultiCoverBase:
    def __init__(self, parent, ability, num_abilities):
        self.abilities = [ability(parent, i) for i in range(0, num_abilities)]

    def activate_cover(self, *args: int):
        for i in args:
            self.abilities[i].show()

    def deactivate_cover(self, *args: int):
        for i in args:
            self.abilities[i].hide()
