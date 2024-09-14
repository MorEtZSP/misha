from scipy.optimize import minimize

# Определение целевой функции
def objective(x):
    x1, x2, x3 = x
    return x1**2 + 3*x2**2 + 5*x1*x3**2

# Определение ограничений (уравнения должны равняться нулю)
def constraint1(x):
    x1, x2, x3 = x
    return x1 * x3 + 2 * x2 + x2**2 - 11

def constraint2(x):
    x1, x2, x3 = x
    return x1**2 + 2 * x1 * x2 + x3**2 - 14

# Попробуем другое начальное приближение
x0 = [0.5, 1.5, 2.5]

# Определение ограничений для функции minimize
constraints = [{'type': 'eq', 'fun': constraint1},
               {'type': 'eq', 'fun': constraint2}]

# Границы для переменных, чтобы избежать переполнения
bounds = [(-10, 10), (-10, 10), (-10, 10)]

# Решение задачи минимизации с новым начальным приближением и границами
solution = minimize(objective, x0, constraints=constraints, bounds=bounds)

# Получение результата
x_opt = solution.x
objective_min = solution.fun

print("Минимум функции достигается при x =", x_opt)
print("Значение функции в точке минимума:", objective_min)