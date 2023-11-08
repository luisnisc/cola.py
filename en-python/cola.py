class myCola:

    def __init__(self, capacidad) -> None:
        self.capacidad = capacidad
        self.altura = 0
        self.buffer = [None] * capacidad

    def __str__(self) -> str:
        return f"{self.buffer.__str__()}"

    def push(self, item) -> bool:
        if (self.altura == self.capacidad):
            return False
        self.buffer[self.altura] = item
        self.altura += 1
        return True
    def pop(self):
        if (self.altura == 0):
            return None
        answ= self.buffer[self.capacidad-self.altura-1]
        self.altura -= 1
        self.buffer[self.capacidad-self.altura-1]=None
        return answ
    
    def altura(self) -> int:
        return self.altura

    def esVacia(self) -> bool:
        return self.altura != 0

    def esLlena(self) -> bool:
        return self.altura == self.capacidad

    def vaciar(self):
        self.buffer = [None] * self.capacidad
        self.altura = 0


if __name__ == "__main__":

    p = myCola(5)
    print(f"{p}: {p.altura}")

    if p.push(11):
        print("push ok")
    print(f"{p}: {p.altura}")

    if p.push(22):
        print("push ok")
    print(f"{p}: {p.altura}")
    if p.push(33):
        print("push ok")
    print(f"{p}: {p.altura}")   
    if p.push(44):
        print("push ok")
    print(f"{p}: {p.altura}")   
    if p.push(55):
        print("push ok")
    print(f"{p}: {p.altura}")   

    # print(f"{p}: {p.altura}")
    # if p.push(44):
    #     print("push ok")
    # print(f"{p}: {p.altura}")

    p.pop()
    print(f"{p}: {p.altura}")
    p.pop()
    print(f"{p}: {p.altura}")
    p.pop()
    print(f"{p}: {p.altura}")
    p.pop()
    print(f"{p}: {p.altura}")
    p.pop()
    print(f"{p}: {p.altura}")

    if p.push(66):
        print("push ok")
    print(f"{p}: {p.altura}")

    if p.push(77):
        print("push ok")
    print(f"{p}: {p.altura}")
    if p.push(99):
        print("push ok")
    print(f"{p}: {p.altura}")   
    if p.push(111):
        print("push ok")
    print(f"{p}: {p.altura}")   
    if p.push(222):
        print("push ok")
    print(f"{p}: {p.altura}")   


    p.vaciar()
    print(f"{p}: {p.altura}")

    # p.altura = -4 # falta de privacidad
