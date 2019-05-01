""" Example Matrix class for docstrings and testing in python.

Basic math classes used for demonstrating how code can be documented
and tested in python
"""

class Matrix:
    """ Represents a matrix of real numbers

    Very slow and basic matrix operations are performed.  Use NumPy instead!
    Also this is not tested very well, there are bugs, write tests to find them
    It is purposely written in a way to introduce bugs that can be found 
    via testing

    Attributes:
        rows: The number of rows in the matrix
        cols: The number of columns in the matrix
    """

    def __init__(self, n, m):
        """ Create an n x m matrix, filled with zeros 

        Args:
           n: the number of rows
           m: the number of columns
        """
        self.__rows = n
        self.__cols = m
        self.__data = [None] * n * m

    @property
    def rows(self):
        return self.__rows

    @property
    def cols(self):
        return self.__cols

    def __setitem__(self, key, value):
        """ Set matrix element [i,j] to value

        Args:
           key: tuple (i,j) with row and column indices
           value: value to set
        """
        self.__data[key[0] + key[1] * self.rows] = elem

    def __getitem__(self, key):
        """ Get element [i,j] from the matrix

        Args:
           key: tuple(i,j) with row and column indices
        """
        return self.__data[key[0] + key[1] * self.cols]

    def __mul__(self, rhs):
        """ Multiply this matrix by another matrix

        Args:
           rhs - the right hand side of the matrix multiplication
        Returns:
          A matrix that is self * rhs
        """
        if self.cols != rhs.rows:
            raise Exception("Dimension mismatch")

        result = Matrix(self.rows, rhs.cols)
        for i in range(self.rows):
            for j in range(rhs.cols):
                rowsum = 0
                for k in range(self.cols):
                    rowsum += self[(i,k)] * rhs[(k,i)]
                result[(i,j)] = rowsum
        return result
                
