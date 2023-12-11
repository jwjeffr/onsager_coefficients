import matplotlib.pyplot as plt
import matplotlib as mpl

from onsager_coefficients import get_onsager_matrix


def main():
    # weird matplotlib-ovito conflict, need to change backend of matplotlib
    # might not be necessary, comment out
    mpl.use('Agg')

    # calculate Onsager matrix
    matrix = get_onsager_matrix('transV.dump', num_trajectories=15, timestep=0.002, transient_time=200)

    # access number of types for easy iteration
    num_types = matrix.num_types

    # plot time series <R_i(t)\cdot R_j(t)>
    for i in range(num_types):
        for j in range(i, num_types):
            plt.plot(matrix.time, matrix.time_series[i, j], label=f'{i}{j}')

    # print out matrix elements
    print(matrix[...])

    plt.legend(title='ij')
    plt.ylabel(r'$ij$ Onsager coefficient $L_{ij}$ ($\AA^2$/ps)')
    plt.ylabel(r'time $t$ (ps)')
    plt.grid()
    plt.savefig('square_displacement.svg', bbox_inches='tight')


if __name__ == '__main__':
    main()
