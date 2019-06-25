import unittest
import main
import numpy as np


class TestMain(unittest.TestCase):
    def test_cross_product(self):
        expected = np.array([0.0, 0.0, 1.0])
        c = np.cross(list(main.a), list(main.b))
        try:
            np.testing.assert_allclose(expected, c)
        except AssertionError as e:
            self.fail()

    def test_cross_product2(self):
        expected = np.array([0.0, 0.0, 10.0])
        c = np.cross(list(main.a), list(main.b))
        np.testing.assert_allclose(expected, c)

    def test_cross_product3(self):
        expected = np.array([0.0, 0.0, 1.0])
        c = np.cross(list(main.a), list(main.b))
        np.testing.assert_allclose(expected, c)

    def test_cross_product4(self):
        expected = np.array([0.0, 0.0, 1.0])
        c = np.cross(list(main.a), list(main.b))
        np.testing.assert_allclose(expected, c)


if __name__ == '__main__':
    unittest.main()
