class Polynomial:
    '''
    Class for single-variable polynomials

    >>> str(Polynomial({1: 1}))
    '1 * X ** 1'
    >>> Polynomial({1: 1})
    Polynomial({1: 1})
    >>> print(Polynomial({1: 1}) + Polynomial({2: 2}))
    2 * X ** 2 + 1 * X ** 1
    >>> X = Polynomial({1: 1})
    >>> print(X + Polynomial({1: 1}))
    2 * X ** 1
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
        return ' + '.join([
            '{0} * X ** {1}'.format(coef, power)
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


# X = Polynomial({1: 1})

# p = 3 + X
# q = X - 2
# print(p.derivative())  # 2 * X + 2
# # print(p + q)  # X ** 2 + X + 1

if __name__ == '__main__':
    import doctest
    doctest.testmod()
