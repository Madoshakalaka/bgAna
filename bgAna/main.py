#!/usr/bin/env python3
import argparse
import os
from sys import stderr
from typing import List, Union, Tuple
from scipy import stats

import cv2
import numpy as np

from bgAna import color_name_finder


class ImageParsingError(Exception):
    pass


class ImageLike:
    def __init__(self, src, true_np_img):
        self._true_np_img = true_np_img
        self._src = src

    def get_np_img(self):
        return self._true_np_img

    @classmethod
    def parse_img(cls, dubious_obj):

        parsed_obj = None
        if isinstance(dubious_obj, str):
            if os.path.isfile(dubious_obj):
                try:
                    img = cv2.imread(dubious_obj)
                except Exception as e:
                    print(e, stderr)
                    raise ImageParsingError()
                else:
                    if img is None:
                        raise ImageParsingError()
            else:
                print("no file")
                raise ImageParsingError(dubious_obj)

            parsed_obj = ImageLike(dubious_obj, img)
        else:

            if isinstance(dubious_obj, np.ndarray):
                if len(dubious_obj.shape) == 3:
                    if dubious_obj.shape[2] not in (1, 3):
                        raise ImageParsingError()
                    if dubious_obj.shape[0] == 0 or dubious_obj.shape[1] == 0:
                        raise ImageParsingError()
                elif len(dubious_obj.shape) == 2:
                    if dubious_obj.shape[0] == 0 or dubious_obj.shape[1] == 0:
                        raise ImageParsingError()
                else:
                    raise ImageParsingError()

                parsed_obj = ImageLike(dubious_obj, dubious_obj)

        return parsed_obj


def get_mode(img: np.ndarray) -> np.ndarray:
    return stats.mode(img.reshape((img.shape[0]*img.shape[1],3)))[0][0]


def cmd():
    parser = argparse.ArgumentParser(
        description="Heuristics to get the background color of any image"
    )

    parser.add_argument(
        "filename",
        action="store",
        type=str,
        help="the image file (in freaking any format you want)",
    )

    argv = parser.parse_args()

    try:
        res = analyze_bg(argv.filename)
    except ImageParsingError:
        print(stderr)
        print("can't parse image")

    else:
        print("background color (BGR): ", tuple(res[0]), res[1])


def analyze_bg(img: Union[str, np.ndarray]) -> Tuple[np.ndarray, str]:
    """

    :param img: filename or ndarray
    :return: color in BGR
    """
    img = ImageLike.parse_img(img).get_np_img()
    res = get_mode(img)
    return res, color_name_finder.ColorNames.findNearestWebColorName(res[::-1])


if __name__ == "__main__":
    # just to provide a way to test the cmd entry point
    cmd()