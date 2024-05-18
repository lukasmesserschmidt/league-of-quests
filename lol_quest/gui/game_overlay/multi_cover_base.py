class MultiCoverBase:
    def __init__(self, parent, ability, num_abilities):
        self.abilities = [ability(parent, i) for i in range(0, num_abilities)]

    def show(self, *args: int):
        for arg in args:
            self.abilities[arg].show()

    def hide(self, *args: int):
        for arg in args:
            self.abilities[arg].hide()
