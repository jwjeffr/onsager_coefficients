"""
Submodule with an OVITO modifier that acts as a general particle property reduction
"""

from typing import Callable

from ovito.data import DataCollection
import numpy as np
from numpy.typing import ArrayLike


def particle_reduction_modifier(particle_property: str, reducer: Callable[[ArrayLike], ArrayLike]) -> callable:
    """
    Wrapper function returning a particle reduction modifier
    :param particle_property: property to reduce
    :param reducer: A function to perform the reduction operation, taking in a numpy array and outputting a numpy array
                    with lesser dimensionality
    :return: a particle reduction modifier for a specific property and reduction operation
    """

    def wrapper(frame: int, data: DataCollection) -> None:
        """
        Modifier function to return
        :param frame: frame to modify
        :param data: DataCollection to modify
        :return: None
        """

        # access particle types and per-particle data to reduce
        types = data.particles['Particle Type'][...]
        per_particle_data = data.particles[particle_property][...]

        # get per-type data and reduce it
        for type_ in set(types):
            data_to_reduce = per_particle_data[types == type_]
            data.attributes[f'Total displacement {type_:.0f}'] = reducer(data_to_reduce)

    return wrapper


# example calculation for getting mean square displacement of each type
mean_square_displacement_modifier = particle_reduction_modifier(
    particle_property='Displacement Magnitude',
    reducer=lambda x: np.mean(x ** 2, axis=0)
)
