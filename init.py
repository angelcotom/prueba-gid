print("hola mundo")
print("queso")
print("QUE ONDA")

from collections import deque
class Recepcion:
    def __init__(self):
        self.cola_pacientes = deque()
    def agregar_paciente(self, nombre):
        self.cola_pacientes.append(nombre)
        print(f"[RECEPCION]Paciente agregado:{nombre}")
    def atender_paciente(self):
        if self.cola_pacientes:
            atendido = self.cola_pacientes.popleft()
            print(f"[RECEPCION] Paciente atentido:{atendido}")
        else:
            print("[RECEPCION] No hay pacientesen la cola")
    def mostrar_cola(self):
        if self.cola_pacientes:
            print("[RECEPCION] Pacientes en espera:")
            for paciente in self.cola_pacientes:
                print(f"{paciente}")
            else:
                print("[RECPECION] La cola esta vacia")
if_name_=="":
    r=Recepcion()
    r.agregar_paciente("JUAN")
    r.agregar_paciente("LUIS")
    r.mostrar_cola()
    r.atender_paciente()
    r.mostrar_cola()


