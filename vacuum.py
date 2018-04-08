import argsparser
import sys
from robot import Robot
from room import Room
from maze import Maze
import error_messages


arguments = argsparser.parse_args(sys.argv[1:])

maze = 0
robot = 0


def load():
    maze_size = 0

    if "-n" in arguments.keys():
        try:
            maze_size = int(arguments["-c"])
        except ValueError:
            error_messages.value_integer_error()
            return False
    else:
        error_messages.required_parameter_missing("-n")
        return False

    if "-c" in arguments.keys():
        return True
    else:
        error_messages.required_parameter_missing("-c")
        return False


if load():
    exit(0)
else:
    print("Terminated with errors.")
    exit(1)