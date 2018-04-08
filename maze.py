from room import Room


class Maze:

    def __init__(self, size, inaccessible_rooms):
        self.rooms = [[Room(x, y, True) for y in range(size)] for x in range(size)]
        self.size = size

        for room in inaccessible_rooms:
            self.rooms[room.x][room.y] = room

    # def room_for_coordinates(self, x, y):
    #     for room in self.rooms:
    #         if self.rooms[room].x == x and self.rooms[room].y == y:
    #             return room
    #             break
    #
    #     return False

    def room_to_right(self, of_room):
        if of_room.x + 1 < self.size:
            return self.rooms[of_room.x+1][of_room.y]
        else:
            return False

    def room_to_left(self, of_room):
        if of_room.x - 1 < self.size and of_room.x >= 0:
            return self.rooms[of_room.x-1][of_room.y]
        else:
            return False

    def room_to_bottom(self, of_room):
        if of_room.y - 1 < self.size and of_room.x >= 0:
            return self.rooms[of_room.x][of_room.y-1]
        else:
            return False

    def room_to_top(self, of_room):
        if of_room.y + 1 < self.size:
            return self.rooms[of_room.x][of_room.y+1]
        else:
            return False
