class myPila:

    def __init__(self, tamMax):
        self.tamMax = tamMax
        self.data =[]

    def push(algo):
        pass  # TODO **********

    def pop(): # -> algo
        pass # TODO ************


if __name__ == "__main__":

    p = myPila(3)
    p.push(11)
    print(p.data)    

    p.push(22)
    print(p.data)    

    p.push(33)
    print(p.data)    

    # p.push(44)   # CRACK
    print(p.data)    

    print(p.pop())  # -> 33
    print(p.pop())  # -> 22    
    print(p.pop())  # -> 11
    # print(p.pop())  # -> CRAK , None "vacia"







pila.append(22)
print(pila)     # [11,22]

pila.append(33)
print(pila)     # [11,22,33]

pila.append(44)
print(pila)     # [11,22,33,44]

pila.append(55)
print(pila)     # [11,22,33,44]
