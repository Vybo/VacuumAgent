enable_visualization = True
if enable_visualization:
    import numpy as np
    import matplotlib.pylab as plt

accessible_value = 0
inaccessible_value = 4
dirty_value = 2.1
visited_value = 2
cleaned_value = 1

def visualize_maze_state(maze):
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



        fig = plt.figure()
        ax = fig.add_subplot(1 ,1, 1)
        ax.set_aspect('equal')
        plt.imshow(matrix, interpolation='nearest', cmap=plt.cm.binary)

        ax.invert_yaxis()
        # plt.colorbar()
        plt.show()
