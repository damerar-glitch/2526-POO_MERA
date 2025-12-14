# --- Programación Orientada a Objetos: Clima Semanal ---

class ClimaSemanal:
    """
    Clase que representa el registro y cálculo del clima semanal.
    """

    def __init__(self):
        """
        Constructor de la clase
        """
        # Aquí creo mi objeto y defino que tendrá una lista interna para guardar las temperaturas.

        self._temperaturas = []

    def ingresar_temperaturas(self):
        """
        Solicita al usuario las temperaturas de 7 días y las almacena internamente.
        """
        # Cada vez que llamo este metodo, reinicio la lista para empezar desde cero.
        self._temperaturas = []
        dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]

        # Muestro un mensaje inicial para indicar que voy a ingresar las temperaturas.
        print("--- Ingreso de Temperaturas Diarias (7 días) ---")
        for dia in dias:
            while True:
                try:
                    # Aquí le pido al usuario la temperatura del día correspondiente.
                    temp = float(input(f"Ingrese la temperatura del {dia} (°C): "))
                    # Una vez que recibo el dato, lo guardo en mi lista interna.
                    self._temperaturas.append(temp)
                    break
                except ValueError:
                    # Si el usuario se equivoca, le aviso que debe ingresar un número válido.
                    print("Entrada no válida. Por favor, ingrese un número.")

    def calcular_promedio(self):
        """
        Calcula el promedio de las temperaturas almacenadas en la instancia.
        Retorna el promedio (float).
        """
        # Aquí calculo el promedio de las temperaturas que ya guardé.
        if not self._temperaturas:
            # Si no tengo datos, retorno 0 para evitar errores.
            return 0

            # Sumo todas las temperaturas.
        suma_temperaturas = sum(self._temperaturas)
        # Cuento cuántos días fueron ingresados.
        num_dias = len(self._temperaturas)
        # Divido la suma entre el número de días para obtener el promedio.
        promedio = suma_temperaturas / num_dias
        return promedio

    def mostrar_resultados(self):
        """
        Muestra las temperaturas registradas y el promedio calculado.
        """
        # Llamo internamente al metodo calcular_promedio para obtener el resultado.
        promedio = self.calcular_promedio()

        print("\n Resultado ")
        if self._temperaturas:
            # Si tengo datos, muestro la lista y el promedio calculado.
            print(f"Temperaturas registradas: {self._temperaturas}")
            print(f"El promedio semanal del clima es: {promedio:.2f} °C")
        else:
            # Si no se ingresaron temperaturas, aviso al usuario.
            print("No se ingresaron temperaturas.")


def ejecutar_programa_poo():
    """
    Función principal para el enfoque de POO.
    """
    # Inicio el programa mostrando un encabezado.
    print("\n=============================================")
    print("      PROGRAMACIÓN ORIENTADA A OBJETOS (POO)")
    print("=============================================")

    # Primero creo un objeto de la clase ClimaSemanal.
    reporte_clima = ClimaSemanal()

    # Luego uso el metodo del objeto para ingresar las temperaturas.
    reporte_clima.ingresar_temperaturas()

    # Finalmente llamo al metodo mostrar_resultados, que internamente calcula y muestra el promedio.
    reporte_clima.mostrar_resultados()


# Aquí llamo a la función principal para ejecutar todo el programa.
ejecutar_programa_poo()