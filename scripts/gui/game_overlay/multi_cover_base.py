class MultiCoverBase:
    def __init__(self, parent, cover, num_covers):
        self.covers = [cover(parent, i) for i in range(0, num_covers)]

    def show(self, *args: int):
        for arg in args:
            self.covers[arg].show()

    def hide(self, *args: int):
        for arg in args:
            self.covers[arg].hide()
