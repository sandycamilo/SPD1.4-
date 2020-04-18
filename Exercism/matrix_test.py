from matrix import Matrix
import unittest

class MatrixTest(unittest.TestCase):

    def test_rows(self):
        assert Matrix.row('9 8 7\n5 3 2\n6 6 7') == '987'

    def test_columns(self):
        assert Matrix.column('9 8 7\n5 3 2\n6 6 7') == '956836727'

if __name__ == '__main__':
    unittest.main()