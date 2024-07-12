class Personas:
    def __init__(self, nombre, edad, tel):
        self.nombre = nombre
        self.edad = edad
        self.tel = tel

    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getEdad(self):
        return self.edad
    def setEdad(self, edad):
        self.edad = edad
    
    def getTel(self):
        return self.tel
    def setTel(self, tel):
        self.tel = tel
    
    def info_persona(self):
        print(f"Nombre: {self.getNombre()} \nEdad: {self.getEdad()} \nTelefono: {self.getTel()}")

class Estudiantes(Personas):
    def __init__(self, nombre, edad, tel, carrera, matricula):
        super().__init__(nombre, edad, tel)
        self.__carrera = carrera
        self.__matricula = matricula
    
    def getCarrera(self):
        return self.__carrera
    def setCarrera(self, carrera):
        self.__carrera = carrera
    
    def getMatricula(self):
        return self.__matricula
    def setMatricula(self, matricula):
        self.__matricula = matricula
    
    def informar_carrera(self):
        print(f"La carrera de {self.getNombre()} es {self.getCarrera()}")
    
    def info_persona(self):
        super().info_persona()
        print(f"Carrera: {self.getCarrera()} \nMatricula: {self.getMatricula()}")

class Docentes(Personas):
    def __init__(self, nombre, edad, tel, modaliad, num_empleado):
        super().__init__(nombre, edad, tel)
        self._modaliad = modaliad
        self._num_empleado = num_empleado
    
    def getModalidad(self):
        return self._modaliad
    def setModalidad(self, modaliad):
        self._modaliad = modaliad
    
    def getNumEmpleado(self):
        return self._num_empleado
    def setNumEmpleado(self, num_empleado):
        self._num_empleado = num_empleado
    
    def informar_modalidad(self):
        print(f"La modalidad de {self.getNombre()} es {self.getModalidad()}")
    
    def info_persona(self):
        super().info_persona()
        print(f"Modalidad: {self.getModalidad()} \nNumero de empleado: {self.getNumEmpleado()}")