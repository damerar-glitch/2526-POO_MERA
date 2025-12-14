def obtener_temperaturas_diarias():
    """
    Solicita al usuario las temperaturas de 7 días.
    Retorna una lista de las temperaturas (float).
    """
    # Aquí defino la función que me permitirá pedir las temperaturas de cada día.
    temperaturas = []
    dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]

    # Muestro un mensaje inicial para indicar que voy a ingresar las temperaturas.
    print("--- Ingreso de Temperaturas Diarias (7 días) ---")
    for dia in dias:
        while True:
            try:
                # En este punto le pido al usuario que ingrese la temperatura del día correspondiente.
                temp = float(input(f"Ingrese la temperatura del {dia} (°C): "))
                # Una vez que recibo el dato, lo agrego a mi lista de temperaturas.
                temperaturas.append(temp)
                break
            except ValueError:
                # Si el usuario se equivoca, le aviso que debe ingresar un número válido.
                print("Entrada no válida. Por favor, ingrese un número.")
    # Finalmente, retorno la lista completa con las temperaturas registradas.
    return temperaturas


def calcular_promedio_semanal(temperaturas):
    """
    Calcula el promedio de una lista de temperaturas.
    Retorna el promedio (float).
    """
    # Aquí defino la función que me permitirá calcular el promedio semanal.
    if not temperaturas:
        # Si no tengo datos, retorno 0 para evitar errores de división.
        return 0

        # Sumo todas las temperaturas que recibí.
    suma_temperaturas = sum(temperaturas)
    # Cuento cuántos días fueron ingresados.
    num_dias = len(temperaturas)
    # Divido la suma entre el número de días para obtener el promedio.
    promedio = suma_temperaturas / num_dias
    # Retorno el promedio calculado.
    return promedio


def ejecutar_programa_tradicional():
    """
    Función principal para el enfoque tradicional.
    """
    # Inicio el programa mostrando un encabezado.
    print("\n=============================================")
    print("      PROGRAMACIÓN TRADICIONAL (Estructural)")
    print("=============================================")

    # Primero llamo a la función que me pide las temperaturas.
    datos_temperaturas = obtener_temperaturas_diarias()

    # Luego calculo el promedio semanal con los datos ingresados.
    promedio = calcular_promedio_semanal(datos_temperaturas)

    # Finalmente muestro los resultados al usuario.
    print("\n--- Resultado ---")
    if datos_temperaturas:
        # Si tengo datos, los imprimo junto con el promedio.
        print(f"Temperaturas registradas: {datos_temperaturas}")
        print(f"El promedio semanal del clima es: {promedio:.2f} °C")
    else:
        # Si no se ingresaron temperaturas, aviso al usuario.
        print("No se ingresaron temperaturas.")

# Aquí llamaría a la función principal para ejecutar todo el programa.
ejecutar_programa_tradicional()