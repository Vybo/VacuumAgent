class Room:

    def __init__(self, x, y, accessible):
        self.x = x
        self.y = y
        self.accessible = accessible
        self.cleaned = False
        self.visited = 0

    def change_coordinate(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def visit(self):
        self.visited += 1

    def clean(self):
        self.cleaned = True

    def lock(self):
        self.accessible = False
