import sympy as sp

x = sp.symbols('x')

print(x+x)
print(x*x)

sp.init_printing()

lista_simbolos = ["y", "x"]
y,x = sp.symbols(lista_simbolos)

f_x_y = x**2 + y**2 + x*y
# f_x_y in jupyter notebook prints out x² + xy + x²

resposta = f_x_y.subs(x,1).subs(y,2)
print(resposta)

f_xy = (x+y)**2 + y**2 + 2*x*y + y**2
# f_xy == 2xy+2y²+(x+y)²

sp.simplify(f_xy)
# x² + 4xy + 3y²

