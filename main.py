import os
import funciones

# Probando las funciones
print("El resultado de la suma es:", funciones.suma(10, 5))
print("El resultado de la resta es:", funciones.resta(20, 8))

# Generacin de la carpeta y los nuevos archivos
if not os.path.exists("resultados"):
    os.makedirs("resultados")

# Simulamos la creacin de una imagen png y un archivo eps
with open("resultados/grafica.png", "w") as f:
    f.write("Simulacion de imagen PNG")
    
with open("resultados/diagrama.eps", "w") as f:
    f.write("Simulacion de archivo EPS")

print("¡Archivos generados exitosamente en la carpeta 'resultados'!")