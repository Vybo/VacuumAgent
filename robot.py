from room import Room


class Robot:

    def __init__(self, starting_room):
        self.current_room = starting_room
        self.visited_rooms = [self.current_room]  # The robots memory, storing rooms it has already visited and cleaned.
        self.total_cleans = 0

    # Sensor function
    def can_move_to_room(self, room):
        # Room should be accessible only if it has a distance of exactly 1 in every direction, it is unlocked and the robot is not currently in it.
        if room != False and \
        room.accessible and \
        ((abs(self.current_room.x - room.x) == 1 and abs(self.current_room.y - room.y) == 0) or \
        (abs(self.current_room.x - room.x) == 0 and abs(self.current_room.y - room.y) == 1))\
        :
            return True
        else:
            return False

    # The robot has no sensor to check for trash, however it has a memory of visited rooms, which it can check.
    # It would be pointless to vacuum already visited room, which has been vacuumed for sure before.
    def should_vacuum_room(self, room):
        visited_rooms_set = frozenset(self.visited_rooms)

        if room in visited_rooms_set:
            return False
        else:
            return True

    def vacuum_current_room(self):
        self.current_room.clean()
        self.total_cleans += 1

    def move_to_room(self, new_room):
        # Check if the robot can move to a different room is outside this class, in the main engine 'vacuum.py'.
        self.current_room = new_room
        self.current_room.visit()
        self.visited_rooms.append(self.current_room)

        if self.should_vacuum_room(self.current_room):
            self.current_room.clean()
            self.total_cleans += 1

    def room_preferability(self, for_room):
        if for_room == False:
            return -1.0

        avg_x = 0
        avg_y = 0

        for room in self.visited_rooms:
            avg_x += room.x
            avg_y += room.y

        avg_x = avg_x / len(self.visited_rooms)
        avg_y = avg_y / len(self.visited_rooms)

        vector = {'x': for_room.x - avg_x, 'y': for_room.y - avg_y}
        # vector['x'] = vector['x'] * -1
        # vector['y'] = vector['y'] * -1

        if vector['y'] < 0.0:
            return vector['y']
        elif vector['x'] < 0.0:
            return vector['x']
        else:
            return 1.0