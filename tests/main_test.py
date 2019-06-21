import os
import subprocess
import sys
import unittest
from os import path

import cv2
import numpy as np

from bgAna import main


class MyTestCase(unittest.TestCase):
    oldDir = ""

    def setUp(self) -> None:
        MyTestCase.oldDir = os.getcwd()
        os.chdir(os.path.dirname(__file__))

    def test_mode_getting(self):
        """
        in case scipy changes how it behaves
        """
        res = main.get_mode(cv2.imread(path.join('examples', 'random.jpg')))
        print('xx', res, 'xx')
        self.assertTrue(np.array_equal(res, (26,21,23)))

    def test_cmd(self):
        cmd = ' '.join((sys.executable, path.join('..','bgAna','main.py'), path.join('examples','random.jpg')))
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, _ = p.communicate()
        self.assertTrue(stdout.decode(encoding='utf-8').strip().endswith('[26 21 23]'))

    def tearDown(self) -> None:

        os.chdir(MyTestCase.oldDir)

if __name__ == '__main__':
    unittest.main()
