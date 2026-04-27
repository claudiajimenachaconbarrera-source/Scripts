import numpy as np

# Definimos los coeficientes: [23, 1, 0, 0, 1]
# Representan: 23m^4 + 1m^3 + 0m^2 + 0m + 1
coeficientes = [23, 1, 0, 0, 1]

# Calculamos las raíces
raices = np.roots(coeficientes)

print("Las raíces de la ecuación son:")
for i, r in enumerate(raices, 1):
    print(f"m{i} = {r}")


