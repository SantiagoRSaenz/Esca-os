class reparticion_escaños:

    def __init__(self):
        self.partidos = []
        self.votos = [] 
        self.escaños = 0
        self.num_partidos = 0

    def solicitud_datos(self):
        self.num_partidos = int(input("Ingrese el número de partidos: "))
        self.escaños = int(input("Ingrese el número de escaños: "))

    def solicitud_partidos(self):
        for i in range(self.num_partidos):
            self.partidos.append(input(f"Ingrese el nombre del partido {i+1}: "))
            self.votos.append(int(input(f"Ingrese el número de votos del partido {i+1}: ")))

    def mostrar_datos(self):
        print("Partidos: ", self.partidos)
        print("Votos: ", self.votos)
        print("Escaños: ", self.escaños)

    def repartir_escaños(self):

        votos_partidos = self.votos.copy()
        escaños_partidos = [0 for i in range(self.num_partidos)]

        for i in range(self.escaños):
            coeficientes = [self.votos[j] / (1 + escaños_partidos[j]) for j in range(self.num_partidos)]
            index = coeficientes.index(max(coeficientes))
            escaños_partidos[index] += 1

        print("Escaños por partido: ", escaños_partidos)

    def run(self):
        self.solicitud_datos()
        self.solicitud_partidos()
        self.mostrar_datos()
        self.repartir_escaños()

if __name__ == "__main__":
    reparticion = reparticion_escaños()
    reparticion.run()


