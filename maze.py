from room import Room


class Maze:

    def __init__(self, size, inaccessible_rooms):
        self.rooms = [[Room(x, y, True) for x in range(size)] for y in range(size)]
        self.size = size-1

        for room in inaccessible_rooms:
            self.rooms[room.x][room.y] = room

    # def room_for_coordinates(self, x, y):
    #     for room in self.rooms:
    #         if self.rooms[room].x == x and self.rooms[room].y == y:
    #             return room
    #             break
    #
    #     return False
