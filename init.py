print("hola mundo")
print("queso")
print("QUE ONDA")

from collections import deque
class Recepcion:
    def __init__(self):
        self.cola_pacientes = deque()
    def agregar_paciente(self, nombre):
        self.cola_pacientes.append(noombre)
        print(f"[RECEPCION]Paciente agregado:{nombre}")
    def atender_paciente(self):
        if self.cola_pacientes:
        atendido= self.cola_pacientes.popleft()
        print(f"[RECEPCION] Paciente atentido;{atendido}")
        else:

