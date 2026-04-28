# --- CALCULADORA DE IMC  ---
datos_confirmados = False

while not datos_confirmados:
    print("\n" + "="*40)
    print("Bienvenido, Le pediremos unos datos para completar su registro y calcular tu Índice de Masa Corporal (IMC)")
    print("="*40)

    # 1. VALIDAR NOMBRE (Sin números)
    while True:
        nombre = input("¿Cuál es tu nombre? ").strip()
        if nombre.replace(" ", "").isalpha() and nombre != "":
            break
        print("❌ Error: El nombre debe contener solo letras y no estar vacío.")

    # 2. VALIDAR APELLIDOS (Sin números)
    while True:
        apellido_p = input("¿Cuál es tu apellido paterno? ").strip()
        apellido_m = input("¿Cuál es tu apellido materno? ").strip()
        
        # Juntamos ambos para validar en un solo paso
        apellidos = apellido_p + apellido_m
        if apellidos.replace(" ", "").isalpha() and apellidos != "":
            break
        print("❌ Error: Los apellidos deben contener solo letras.")

    # 3. VALIDAR DATOS NUMÉRICOS (Con Try-Except)
    while True:
        try:
            edad = int(input("¿Cuántos años tienes? "))
            peso = float(input("¿Cuánto pesas en kg? (Ejemplo: 70.5): "))
            estatura = float(input("¿Cuánto mides en metros? (Ejemplo: 1.75): "))

            if edad > 0 and peso > 0 and estatura > 0:
                break
            else:
                print("❌ Los números deben ser mayores a cero.")
        except ValueError:
            print("⚠️ Error: Ingresa valores numéricos válidos. Usa punto para decimales.")

    # --- PANTALLA DE REVISIÓN ---
    print("\n" + "*"*30)
    print("REVISIÓN DE TUS DATOS:")
    print(f"Nombre: {nombre} {apellido_p} {apellido_m}")
    print(f"Edad: {edad} años")
    print(f"Peso: {peso} kg")
    print(f"Estatura: {estatura} m")
    print("*"*30)

    confirmar = input("¿Son correctos estos datos? (S/N): ").upper()

    if confirmar == "S":
        datos_confirmados = True
    else:
        print("\nMete los datos nuevamente.\n")

# --- CÁLCULO FINAL Y CLASIFICACIÓN ---
imc = peso / (estatura ** 2)

print("\n" + "="*40)
print(f"RESULTADO PARA: {nombre.upper()}")
print(f"Tu IMC es: {imc:.2f}")

# Clasificación del IMC
if imc < 18.5:
    print("Estado: Bajo peso")
elif 18.5 <= imc < 24.9:
    print("Estado: Peso normal (Saludable)")
elif 25 <= imc < 29.9:
    print("Estado: Sobrepeso")
else:
    print("Estado: Obesidad")
print("="*40)