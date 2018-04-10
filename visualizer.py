enable_visualization = True
rendering_available = False

if enable_visualization:
    try:
        import numpy as np
        import matplotlib.pylab as plt
        import matplotlib.animation as animation
        rendering_available = True
    except ImportError:
        enable_visualization = False
        print("[Warning] numpy and matplotlib not installed. Rendering unavailable. Continuing.")

accessible_value = 0
inaccessible_value = 4
dirty_value = 2.9
visited_value = 2
cleaned_value = 1
robot_value = 3.5

ims = []

if enable_visualization:
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_aspect('equal')

def visualize_maze_state(maze, robot):

    if enable_visualization:

        matrix = np.zeros(shape=(maze.size, maze.size))
        matrix.fill(inaccessible_value)

        for x in range(maze.size):
            for y in range(maze.size):
                if maze.rooms[x][y].cleaned:
                    matrix[y, x] = cleaned_value
                elif maze.rooms[x][y].visited > 0:
                    matrix[y, x] = visited_value
                elif maze.rooms[x][y].accessible:
                    matrix[y, x] = dirty_value

        matrix[robot.current_room.y, robot.current_room.x] = robot_value

        plt.imshow(matrix, interpolation='nearest', cmap=plt.cm.binary)

        ax.invert_yaxis()
        # plt.colorbar()
        plt.show()


def render_maze_state(maze, robot):
    if enable_visualization:

        matrix = np.zeros(shape=(maze.size, maze.size))
        matrix.fill(inaccessible_value)

        for x in range(maze.size):
            for y in range(maze.size):
                if maze.rooms[x][y].cleaned:
                    matrix[y, x] = cleaned_value
                elif maze.rooms[x][y].visited > 0:
                    matrix[y, x] = visited_value
                elif maze.rooms[x][y].accessible:
                    matrix[y, x] = dirty_value

        matrix[robot.current_room.y, robot.current_room.x] = robot_value


        im = plt.imshow(matrix, interpolation='nearest', cmap=plt.cm.binary, animated=True)

        ax.invert_yaxis()
        ims.append([im])
        # plt.show()


def render_video(file_name):
    for i in range(10):
        ims.append(ims[-1])

    from matplotlib.animation import FFMpegWriter
    writer = FFMpegWriter(fps=15, bitrate=1800)
    ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)
    ani.save(file_name, writer=writer)