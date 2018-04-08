from room import Room


class Maze:

    def __init__(self, size, inaccessible_rooms):
        self.rooms = [[Room(x, y, True) for x in range(size)] for y in range(size)]

        for room in inaccessible_rooms:
            self.rooms[room.x][room.y] = room
