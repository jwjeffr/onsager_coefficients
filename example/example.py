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

    type_map = {0: 'Fe', 1: 'Ni', 2: 'Cr'}

    # plot time series <R_i(t)\cdot R_j(t)>
    for i in range(num_types):
        for j in range(i, num_types):
            plt.plot(matrix.time / 1e3, matrix.time_series[i, j], label=f'{type_map[i]}{type_map[j]}')

    # print out matrix elements
    print(matrix[...])

    plt.legend(title=r'$\alpha\beta$')
    plt.ylabel(r'$\left\langle \mathbf{R}_\alpha(t)\cdot\mathbf{R}_\beta(t)\right\rangle$ ($\AA^2$)')
    plt.xlabel(r'time $t$ (ns)')
    plt.grid()
    plt.savefig('square_displacement.svg', bbox_inches='tight')


if __name__ == '__main__':
    main()
