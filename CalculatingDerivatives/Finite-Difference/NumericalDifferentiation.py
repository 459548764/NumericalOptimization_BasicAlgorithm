#coding=utf-8
# @Author: yangenneng
# @Time: 2018-06-04 14:48
# @Abstract：Numerical Differentiation

def f(x,y):
    return x**2 * y + y + 2

def forward_derivative(f, x, y, x_eps, y_eps):
    return (f(x + x_eps, y + y_eps) - f(x, y)) / (x_eps + y_eps)

def center_derivative(f, x, y, x_eps, y_eps):
    return (f(x + x_eps, y + y_eps) - f(x - x_eps, y - y_eps)) / (2 * (x_eps + y_eps))

df_dx = forward_derivative(f, 3, 4, 1e-8, 0)
df_dy = forward_derivative(f, 3, 4, 0, 1e-8)

print("forward_derivative df_dx", str(df_dx))
print("forward_derivative df_dy", str(df_dy))

df_dx = center_derivative(f, 3, 4, 1e-8, 0)
df_dy = center_derivative(f, 3, 4, 0, 1e-8)

print("center_derivative df_dx", str(df_dx))
print("center_derivative df_dy", str(df_dy))
