enable_visualization = True
if enable_visualization:
    import numpy as np
    import matplotlib.pylab as plt

accessible_value = 1
inaccessible_value = 0
visited_value = 2
cleaned_value = 3

def visualize_maze_state(maze):
    if enable_visualization:

        matrix = np.zeros(shape=(maze.size, maze.size))

        for x in range(maze.size):
            for y in range(maze.size):
                if maze.rooms[x][y].accessible:
                    matrix[x,y] = accessible_value

        fig = plt.figure()
        ax = fig.add_subplot(1 ,1, 1)
        ax.set_aspect('equal')
        plt.imshow(matrix, interpolation='nearest', cmap=plt.cm.ocean)

        ax.invert_yaxis()
        plt.show()
