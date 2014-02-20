class Polynomial:
    '''
    Class for single-variable polynomials

    >>> print(Polynomial({1: 1}))
    1 * x ** 1
    >>> Polynomial({1: 1})
    Polynomial({1: 1})
    >>> print(Polynomial({1: 1}) + Polynomial({2: 2}))
    2 * x ** 2 + 1 * x ** 1
    >>> x = Polynomial({1: 1})
    >>> print(x + Polynomial({1: 1}))
    2 * x ** 1
    >>> a = 3 * x ** 2 - 4 * x
    >>> b = 5 * x ** 2 - 1
    >>> print(a * b)
    15 * x ** 4 - 20 * x ** 3 - 3 * x ** 2 + 4 * x 
    >>> print(a)
    3 * x ** 2 - 4 * x
    >>> print(b)
    b = 5 * x ** 2 - 1
    '''
    def __init__(self, coefs):
        self.d = {}
        for power, coef in coefs.items():
            if coef:
                self.d[power] = coef

    def derivative(self):
        d = {power - 1: coef * power for power, coef in self.d.items()}
        if -1 in d:
            del d[-1]
        return Polynomial(d)

    def __str__(self):
        return ' + '.join(['{0} * x ** {1}'.format(coef, power)
                           for power, coef in self.d.items()])

    def __add__(self, y):
        if not isinstance(y, Polynomial):
            p = Polynomial(self.d)
            p.d[0] = p.d.get(0, 0) + y
            return p
        else:
            raise NotImplementedError()

    def __sub__(self, y):
        return self.__add__(-y)

    def __radd__(self, y):
        return self.__add__(y)

    def __repr__(self):
        return 'Polynomial({0})'.format(repr(self.d))


x = Polynomial({1: 1})

# p = 3 + x
# q = x - 2
# print(p.derivative())  # 2 * x + 2
# # print(p + q)  # x ** 2 + x + 1

if __name__ == '__main__':
    import doctest
    doctest.testmod()
