import unittest
# unittest is the unittesting framework we are using. It is standard python
# Other testing frameworks include nose2 and pytest.
# They will be explored later in this tutorial.
# An advantages of unittest over pytest:
#    Built in to the python standard library
# Disadvantages of unittest over pytest:
#    Requires special assertion functions
#    More boilerplate than pytest
from matrix import Matrix

# A class derived from unittest.TestCase is used to actually write the tests
# methods in this class that start with "test" will automatically be detected
# By the testing framework
class TestMatrix(unittest.TestCase):
    # code in setup is run before every test case
    def setUp(self):
        self.mat22 = Matrix(2,2)
        self.mat33 = Matrix(3,3)
        self.mat12 = Matrix(1,2)
        
    # test that a matrix is initialized to all zeros
    # Note: stylistically it is a good idea to make the names for
    # test cases verbose as these are what you see when the test fails
    # and they are not called during the normal operation of your program
    def test_matrix_initted_to_zeros(self):
        # assertEqual is an assertion function that verifies that its
        # two arguments are equal to each other
        self.assertEqual(self.mat22[(1, 1)], 0)

    # test that multiplying incompatible matrix dimensions raises an exception
    def test_matrix_mult_incompatible_dimensions_exception(self):
        with self.assertRaises(Exception):
            self.mat33 * self.mat12


# When we run this code as a program, the unittest test runner will execute
# Try running this code and see what happens.   Note that no tests will run
# because we have not created any yet
# pass --help to see some options that you have
if __name__ == '__main__':
    unittest.main()
