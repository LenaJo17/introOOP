class Persona:
    def __init__(self, nombre, edad, ciudad, profesion):
        # Atributos de instancia
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad
        self.profesion = profesion

    # Método 1: Presentar a la persona
    def presentar(self):
        print(f"Hola, me llamo {self.nombre}, tengo {self.edad} años, y soy {self.profesion}.")

    # Método 2: Cambiar ciudad de residencia
    def cambiar_ciudad(self, nueva_ciudad):
        self.ciudad = nueva_ciudad
        print(f"{self.nombre} se ha mudado a {self.ciudad}.")

    # Método 3: Cumplir años
    def cumplir_anios(self):
        self.edad += 1
        print(f"{self.nombre} ha cumplido {self.edad} años.")

    # Método 4: Cambiar profesión
    def cambiar_profesion(self, nueva_profesion):
        self.profesion = nueva_profesion
        print(f"{self.nombre} ahora trabaja como {self.profesion}.")

    # Método 5: Obtener información completa de la persona
    def informacion_completa(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Ciudad: {self.ciudad}, Profesión: {self.profesion}"

    # Método 6: Saludar a otra persona
    def saludar(self, otra_persona):
        print(f"Hola {otra_persona.nombre}, me llamo {self.nombre}.")

# Crear tres instancias de la clase Persona
persona1 = Persona("Carlos", 30, "Mexico", "Ingeniero")
persona2 = Persona("Victor", 10, "Mexico", "estudiante")
persona3 = Persona("Brenda", 21, "Mexico", "Ingeniera")

# Usar los métodos de las instancias
persona1.presentar()
persona2.presentar()
persona3.presentar()

persona1.cumplir_anios()
persona2.cumplir_anios()
persona3.cumplir_anios()

persona1.cambiar_ciudad("Barcelona")
persona2.cambiar_ciudad("Rusia")
persona3.cambiar_ciudad("Japon")

persona1.cambiar_profesion("Arquitecto")
persona2.cambiar_profesion("Cardiólogo")
persona3.cambiar_profesion("Jueza")

# Obtener la información completa de cada persona
print(persona1.informacion_completa())
print(persona2.informacion_completa())
print(persona3.informacion_completa())

# Carlos saluda a Victor (al final)
persona1.saludar(persona2)  # Salida: Hola Victor, me llamo Carlos.
# Victor saluda a Brenda (al final)
persona2.saludar(persona3)  # Salida: Hola Brenda, me llamo Victor, Mucho gusto.

