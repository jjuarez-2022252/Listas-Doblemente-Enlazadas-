class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None


class ListaDoble:
    def __init__(self):
        self.inicio = None
        self.fin = None

    # Insertar al inicio
    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)
        if self.inicio is None:
            self.inicio = self.fin = nuevo
        else:
            nuevo.siguiente = self.inicio
            self.inicio.anterior = nuevo
            self.inicio = nuevo

    # Insertar al final
    def insertar_final(self, dato):
        nuevo = Nodo(dato)
        if self.fin is None:
            self.inicio = self.fin = nuevo
        else:
            self.fin.siguiente = nuevo
            nuevo.anterior = self.fin
            self.fin = nuevo

    # Mostrar normal
    def mostrar(self):
        temp = self.inicio
        while temp:
            print(temp.dato, end=" <-> ")
            temp = temp.siguiente
        print("None")

    # Mostrar inverso
    def mostrar_inverso(self):
        temp = self.fin
        while temp:
            print(temp.dato, end=" <-> ")
            temp = temp.anterior
        print("None")

    # Eliminar nodo
    def eliminar(self, dato):
        temp = self.inicio
        while temp:
            if temp.dato == dato:
                if temp == self.inicio:
                    self.inicio = temp.siguiente
                    if self.inicio:
                        self.inicio.anterior = None
                elif temp == self.fin:
                    self.fin = temp.anterior
                    if self.fin:
                        self.fin.siguiente = None
                else:
                    temp.anterior.siguiente = temp.siguiente
                    temp.siguiente.anterior = temp.anterior
                return
            temp = temp.siguiente

    # Insertar en posición
    def insertar_en_posicion(self, dato, pos):
        if pos == 0:
            self.insertar_inicio(dato)
            return
        nuevo = Nodo(dato)
        temp = self.inicio
        for _ in range(pos):
            if temp is None:
                return
            temp = temp.siguiente
        if temp is None:
            self.insertar_final(dato)
            return
        nuevo.anterior = temp.anterior
        nuevo.siguiente = temp
        if temp.anterior:
            temp.anterior.siguiente = nuevo
        temp.anterior = nuevo

    # Modificar posición
    def modificar(self, pos, nuevo_dato):
        temp = self.inicio
        for _ in range(pos):
            if temp is None:
                return
            temp = temp.siguiente

        if temp:
            temp.dato = nuevo_dato

    # Suma de nodos
    def suma(self):
        total = 0
        temp = self.inicio
        while temp:
            total += temp.dato
            temp = temp.siguiente
        return total

    # Ordenar menor a mayor
    def ordenar_ascendente(self):
        i = self.inicio
        while i:
            j = i.siguiente
            while j:
                if i.dato > j.dato:
                    i.dato, j.dato = j.dato, i.dato
                j = j.siguiente
            i = i.siguiente

    # Ordenar mayor a menor
    def ordenar_descendente(self):
        i = self.inicio
        while i:
            j = i.siguiente
            while j:
                if i.dato < j.dato:
                    i.dato, j.dato = j.dato, i.dato
                j = j.siguiente
            i = i.siguiente

    # Insertar después de un valor
    def insertar_despues(self, buscado, dato):
        temp = self.inicio
        while temp:
            if temp.dato == buscado:
                nuevo = Nodo(dato)
                nuevo.siguiente = temp.siguiente
                nuevo.anterior = temp

                if temp.siguiente:
                    temp.siguiente.anterior = nuevo

                temp.siguiente = nuevo

                if temp == self.fin:
                    self.fin = nuevo
                return
            temp = temp.siguiente


# Ejemplo de uso
lista = ListaDoble()

lista.insertar_inicio(10)
lista.insertar_final(20)
lista.insertar_final(5)
lista.insertar_inicio(15)

print("Lista normal:")
lista.mostrar()

print("Lista inversa:")
lista.mostrar_inverso()

lista.insertar_en_posicion(50, 2)
print("Insertar en posición 2:")
lista.mostrar()

lista.modificar(1, 99)
print("Modificar posición 1:")
lista.mostrar()

lista.eliminar(20)
print("Eliminar 20:")
lista.mostrar()

print("Suma:", lista.suma())

lista.ordenar_ascendente()
print("Orden ascendente:")
lista.mostrar()

lista.ordenar_descendente()
print("Orden descendente:")
lista.mostrar()

lista.insertar_despues(99, 77)
print("Insertar después de 99:")
lista.mostrar()