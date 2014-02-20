def stats(seq):
    print(' '.join([str(i) for i in seq]))
    print('min: {0}, max: {1}'.format(min(seq), max(seq)))


stats([3, 1, 5, 7, 4])
stats('Quirrel')

f = lambda x, y: x + y
print(f(3, 4))
print(f([1, 2], [3, 4]))
print(f('ab', 'cd'))

a = ['abc', 'abd', 'abcd', 'de', 'defgh', 'aaaaa', 'abcdef']
print(min(a))
print(max(a))
print(min(a, key=lambda x: len(x)))
print(max(a, key=lambda x: len(x)))
print(min(a, key=len))
print(max(a, key=len))
print(min(a, key=lambda x: x[0]))
print(max(a, key=lambda x: x[0]))
print(min(a, key=lambda x: [x[0], x]))
print(max(a, key=lambda x: [x[0], x]))
print(sorted(a, key=len))
print(sorted(a, key=lambda x: x[::-1]))
