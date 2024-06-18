import sympy as sp

sp.init_printing()

x,y = sp.symbols(["x","y"])

f_x = sp.sin(x)

# derivada
dfdx = sp.diff(f_x,x)
dfdx2 = sp.diff(f_x,x,x)

# integral
f_x2 = sp.sin(x)**2
int_f_x2 = sp.integrate(f_x2)

f_x3 = sp.exp(-x)
sp.integrate(f_x3,(x, 0, sp.oo))