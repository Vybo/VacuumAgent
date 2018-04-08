import argsparser
import sys
from robot import Robot
from room import Room
from maze import Maze
import error_messages
import helper


arguments = argsparser.parse_args(sys.argv[1:])

maze = 0
robot = 0


def load():
    maze_size = 0

    if "-n" in arguments.keys():
        try:
            maze_size = int(arguments["-n"])
        except ValueError:
            error_messages.value_integer_error()
            return False
    else:
        error_messages.required_parameter_missing("-n")
        return False

    if "-c" in arguments.keys():
        chess_coordinates = arguments["c"].split(",")
        chess_x_coordinates = [helper.chess_coordinate_to_x(x) for x in chess_coordinates]
        chess_y_coordinates = [helper.chess_coordinate_to_y(y) for y in chess_coordinates]

        inaccessible_rooms = []
        if len(chess_x_coordinates)-1 < maze_size and len(chess_y_coordinates)-1 < maze_size:
            for i in range(0, len(chess_x_coordinates)):
                inaccessible_rooms.append(Room(chess_x_coordinates[i], chess_y_coordinates[i], False))

            return Maze(maze_size, inaccessible_rooms)
        else:
            error_messages.coordinates_over_n(maze_size)
            return False
    else:
        error_messages.required_parameter_missing("-c")
        return False


maze = load()

if maze:
    exit(0)
else:
    print("Terminated with errors.")
    exit(1)