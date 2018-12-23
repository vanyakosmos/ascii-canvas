import sys

import numpy as np

from renderer.settings import GREY_SCALE
from renderer.utils import to_vec


@to_vec(otypes=[np.object])
def map_char(i):
    i = max(0.0, min(1.0, i))
    c = GREY_SCALE[int((len(GREY_SCALE) - 1) * i)]
    return c * 2


def jump_to_the_top(buff):
    """
    > \033[K - clear line
    > \033[F - move cursor up
    """
    sys.stdout.write("\033[F" * buff.shape[0])


def draw_blank(buff):
    h, w = buff.shape
    for _ in range(h):
        print(' ' * w)


def draw_buff(buff):
    chars: np.ndarray = map_char(buff)
    jump_to_the_top(buff)
    print('\n'.join(chars.sum(axis=1)))
