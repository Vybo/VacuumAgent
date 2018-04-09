import argsparser
import sys
from robot import Robot
from room import Room
from maze import Maze
import error_messages
import helper
import visualizer
from time import sleep

arguments = argsparser.parse_args(sys.argv[1:])

maze = 0
robot = 0
inaccessible_rooms = []

def load():
    maze_size = 0

    if "-v" in arguments.keys():
        try:
            if bool(arguments["-v"]):
                visualizer.enable_visualization = True
        except ValueError:
            error_messages.value_boolean_error()

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

    left_preferability = robot.room_preferability(maze.room_to_left(robot.current_room))
    right_preferability = robot.room_preferability(maze.room_to_right(robot.current_room))
    top_preferability = robot.room_preferability(maze.room_to_top(robot.current_room))
    bottom_preferability = robot.room_preferability(maze.room_to_bottom(robot.current_room))

    preferred_room = 0

    room_to_bottom = maze.room_to_bottom(robot.current_room)
    room_to_top = maze.room_to_top(robot.current_room)
    room_to_right = maze.room_to_right(robot.current_room)
    room_to_left = maze.room_to_left(robot.current_room)

    # If room is in current direction to which robot is heading and is not cleaned, assign it to preferred room.
    if robot.room_in_current_direction(room_to_bottom) and robot.can_move_to_room(room_to_bottom) and robot.should_vacuum_room(room_to_bottom):
        # preferred_room = room_to_bottom
        robot.move_to_room(room_to_bottom)
        visualizer.visualize_maze_state(maze, robot)
        return True
    elif robot.room_in_current_direction(room_to_left) and robot.can_move_to_room(room_to_left) and robot.should_vacuum_room(room_to_left):
        robot.move_to_room(room_to_left)
        visualizer.visualize_maze_state(maze, robot)
        return True
    elif robot.room_in_current_direction(room_to_right) and robot.can_move_to_room(room_to_right) and robot.should_vacuum_room(room_to_right):
        robot.move_to_room(room_to_right)
        visualizer.visualize_maze_state(maze, robot)
        return True
    elif robot.room_in_current_direction(room_to_top) and robot.can_move_to_room(room_to_top) and robot.should_vacuum_room(room_to_top):
        robot.move_to_room(room_to_top)
        visualizer.visualize_maze_state(maze, robot)
        return True
    else:
        # Backtrack until unclean room found
        backtracking_path = robot.visited_rooms[:-1]
        dirty_room_next_to_robot = robot.should_vacuum_room(room_to_bottom) or robot.should_vacuum_room(
            room_to_top) or robot.should_vacuum_room(room_to_left) or robot.should_vacuum_room(
            room_to_right)

        while dirty_room_next_to_robot == False:
            try:
                robot.move_to_room(backtracking_path[-1])
                backtracking_path = backtracking_path[:-1]

            except IndexError:
                visualizer.visualize_maze_state(maze, robot)
                return False

            room_to_bottom = maze.room_to_bottom(robot.current_room)
            room_to_top = maze.room_to_top(robot.current_room)
            room_to_right = maze.room_to_right(robot.current_room)
            room_to_left = maze.room_to_left(robot.current_room)

            visualizer.visualize_maze_state(maze, robot)

            dirty_room_next_to_robot = robot.should_vacuum_room(room_to_bottom) or robot.should_vacuum_room(
                room_to_top) or robot.should_vacuum_room(room_to_left) or robot.should_vacuum_room(
                room_to_right)

        # robot.visited_rooms = backtracking_path[:-1]
        return True

def print_results():
    counter = 0

    for x in range(len(maze.rooms)-1):
        for y in range(len(maze.rooms[x])-1):
            counter += maze.rooms[x][y].visited

    print("[Results] Total squares visited: %(counter)i" %{'counter': counter})
    print("[Results] Visited sequence follows:")

    sequence = []
    for i in range(len(robot.visited_rooms)-1):
        sequence.append(helper.coordinate_to_chess(robot.visited_rooms[i].x) + str(robot.visited_rooms[i].y))
        if i%10 == 0:
            sequence.append('\n')
        print(", ".join(sequence))
    print("[Results] Used maze follows:.")

    sequence = []
    for i in range(len(inaccessible_rooms)-1):
        sequence.append(helper.coordinate_to_chess(inaccessible_rooms[i].x) + str(inaccessible_rooms[i].y))
        if i % 10 == 0:
            sequence.append('\n')

    print(", ".join(sequence))
    print("[Results] Finished.")

maze = load()

if maze:
    # Coordinate system is starting at [0,0] which is left-bottom corner, corresponding to coordinate a1, h8 would be [7,7].
    robot = Robot(maze.rooms[0][7])
    while tick():
        # sleep(0.2)
        continue

    print_results()
    exit(0)
else:
    print("Terminated with errors.")
    exit(1)