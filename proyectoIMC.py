print("Bienvenido, Le pediremos unos datos para completar su registro y calcular tu Índice de Masa Corporal (IMC)")
nombre = input("¿Cuál es tu nombre? ")
apellidoPaterno = input("¿Cuál es tu apellido paterno? ")
apellidoMaterno = input("¿Cuál es tu apellido materno? ")
edad = input("¿Cuántos años tienes? ")
peso = float(input("¿Cuánto pesas en kg? "))
estatura = float(input("¿Cuánto mides en metros? "))
imc = float(peso / (estatura ** 2))
print("Hola revisemos tus datos", nombre, "\n", apellidoPaterno, "\n", apellidoMaterno, "\n", "edad:", edad, "\n", "peso:", peso, "\n", "estatura:", estatura, "\n", "Tu indice de masa corporal es:", imc)

while True:
    if imc < 18.5:
        print(" Tu IMC es", imc, "y estás en bajo peso")
        break
    elif imc >= 18.5 and imc < 25:
        print(" Tu IMC es", imc, "y estás en peso normal")
        break
    elif imc >= 25 and imc < 30:
        print(" Tu IMC es", imc, "y estás en sobrepeso")
        break
    elif imc >= 30 and imc < 35:
        print(" Tu IMC es", imc, "y estás en obesidad grado 1")
        break
    elif imc >= 35 and imc < 40:
        print(" Tu IMC es", imc, "y estás en obesidad grado 2")
        break
    elif imc >= 40:
        print(" Tu IMC es", imc, "y estás en obesidad grado 3")
        break
