import argsparser
import sys
from robot import Robot
from room import Room
from maze import Maze
import error_messages
import helper
import visualizer


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
        chess_coordinates = arguments["-c"].split(",")
        chess_x_coordinates = [helper.chess_coordinate_to_x(x) for x in chess_coordinates]
        chess_y_coordinates = [helper.chess_coordinate_to_y(y) for y in chess_coordinates]

        inaccessible_rooms = []

        for i in range(0, len(chess_x_coordinates)):
            if chess_x_coordinates[i] < maze_size and chess_y_coordinates[i] < maze_size:
                inaccessible_rooms.append(Room(chess_x_coordinates[i], chess_y_coordinates[i], False))
            else:
                error_messages.coordinates_over_n(maze_size)
                return False

        return Maze(maze_size, inaccessible_rooms)

    else:
        error_messages.required_parameter_missing("-c")
        return False

def tick():
    if robot.should_vacuum_room(robot.current_room):
        robot.vacuum_current_room()

    if robot.can_move_to_room(maze.room_to_bottom(robot.current_room)):
        robot.move_to_room(maze.room_to_bottom(robot.current_room))
    else:



maze = load()

if maze:
    # Coordinate system is starting at [0,0] which is left-bottom corner, corresponding to coordinate a1, h8 would be [7,7].
    robot = Robot(maze.rooms[0][7])
    robot.vacuum_current_room()
    robot.move_to_room(maze.rooms[0][6])
    robot.move_to_room(maze.rooms[0][5])
    visualizer.visualize_maze_state(maze)
    exit(0)
else:
    print("Terminated with errors.")
    exit(1)