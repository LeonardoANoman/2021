import sympy as sp
sp.init_printing()

a = sp.Matrix([[1,2,3],[4,5,6]])

b = sp.Matrix([[1,2,3]]).T
c = sp.Matrix([[1],[2],[3]])
d = sp.Matrix([1,2,3])
# b == c == d

# Sistema linear
x1,x2,x3 = sp.symbols(["x1", "x2", "x3"])

x = sp.Matrix([x1,x2,x3])
e = sp.Matrix([[1,2,3],[4,5,6],[7,8,9]])
r = sp.Matrix([11,22,33])

# EX = R

e*x - r