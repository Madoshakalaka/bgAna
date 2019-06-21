import os
import subprocess
import sys
import unittest
from os import path

import cv2
import numpy as np

from bgAna import main


class MyTestCase(unittest.TestCase):
    def test_mode_getting(self):
        """
        in case scipy changes how it behaves
        """
        res = main.get_mode_of_margin(cv2.imread(path.join('examples', 'random.jpg')))
        self.assertTrue(np.array_equal(res, (18,18,20)))

    def test_cmd(self):
        cmd = ' '.join((sys.executable, path.join('..','bgAna','main.py'), path.join('examples','random.jpg')))
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, _ = p.communicate()
        self.assertTrue(stdout.decode(encoding='utf-8').strip().endswith('[18 18 20]'))


if __name__ == '__main__':
    unittest.main()
