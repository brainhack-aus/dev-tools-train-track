import numpy
from intensify import modulate_image


def test_modulate():
    test_array = numpy.ones([10, 10])
    scalar = 10
    offset = 5
    scaled_array = modulate_image(test_array, scalar, offset)
    assert numpy.max(scaled_array) == numpy.max(test_array) * scalar + offset
