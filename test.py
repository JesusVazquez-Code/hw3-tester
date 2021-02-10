__author__ = 'CS540-testers-SP21'
__credits__ = ['Nicholas Beninato']
__version__ = '0.1'

import unittest
import numpy as np
from pca import *

FILENAME = 'YaleB_32x32.npy'

class TestPrincipalComponentAnalysis(unittest.TestCase):
    def test_load_and_center_dataset(self):
        X = load_and_center_dataset(FILENAME)
        self.assertIsInstance(X, np.ndarray)
        self.assertEqual(X.shape, (2414, 1024))
        self.assertTrue(np.isclose(X.mean(), 0.0))

    def test_get_covariance(self):
        X = load_and_center_dataset(FILENAME)
        S = get_covariance(X)
        self.assertIsInstance(S, np.ndarray)
        self.assertEqual(S.shape, (1024, 1024))
        self.assertTrue(np.allclose(S, np.cov(X.T)))

    def test_get_eig(self):
        X = load_and_center_dataset('YaleB_32x32.npy')
        S = get_covariance(X)
        Lambda, U = get_eig(S, 2)
        L_test = np.array([[1369142.41612494, 0],[0, 1341168.50476773]])
        self.assertIsInstance(Lambda, np.ndarray)
        self.assertEqual(Lambda.shape, (2, 2))
        self.assertTrue(np.allclose(Lambda, L_test))

        U_test_1 = [[-0.01304065, -0.0432441],[-0.01177219,-0.04342345],[-0.00905278,-0.04095089]]
        U_test_2 = [[ 0.00148631,0.03622013],[ 0.00205216,0.0348093],[ 0.00305951,0.03330786]]
        self.assertIsInstance(U, np.ndarray)
        self.assertEqual(U.shape, (1024, 2))
        self.assertTrue(np.allclose(U[:3], U_test_1))
        self.assertTrue(np.allclose(U[-3:], U_test_2))

    def test_get_eig_perc(self):
        X = load_and_center_dataset('YaleB_32x32.npy')
        S = get_covariance(X)
        Lambda, U = get_eig_perc(S, 0.07)
        L_test = np.array([[1369142.41612494, 0],[0, 1341168.50476773]])
        self.assertIsInstance(Lambda, np.ndarray)
        self.assertEqual(Lambda.shape, (2, 2))
        self.assertTrue(np.allclose(Lambda, L_test))

        U_test_1 = [[-0.01304065, -0.0432441],[-0.01177219,-0.04342345],[-0.00905278,-0.04095089]]
        U_test_2 = [[ 0.00148631,0.03622013],[ 0.00205216,0.0348093],[ 0.00305951,0.03330786]]
        self.assertIsInstance(U, np.ndarray)
        self.assertEqual(U.shape, (1024, 2))
        self.assertTrue(np.allclose(U[:3], U_test_1))
        self.assertTrue(np.allclose(U[-3:], U_test_2))

    def test_project_image(self):
        x = load_and_center_dataset('YaleB_32x32.npy')
        S = get_covariance(x)
        l, U = get_eig_perc(S, 0.07)
        projection = project_image(x[0], U)
    
        P_test_1 = [6.84122225,4.83901287,1.41736694]
        P_test_2 = [8.75796534,7.45916035,5.4548656]
        self.assertIsInstance(projection, np.ndarray)
        self.assertEqual(projection.shape, (1024,))
        self.assertTrue(np.allclose(projection[:3], P_test_1))
        self.assertTrue(np.allclose(projection[-3:], P_test_2))

    def test_display_image(self):
        # TODO: Check matplotlib
        pass

if __name__ == '__main__':
    print(f'Running CS540 SP21 HW3 tester v{__version__}')
    unittest.main()