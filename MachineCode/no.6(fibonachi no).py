Acc = None
IR = None
PC = None
Input = None
Output = None
Mem = [0] * 100

Mem[0] = 1
Mem[99] = 800

# code and pc
CARDIACode = [100, 404, 601, 100, 201, 602, 502, 100, 201, 603, 503, 100,
              203, 604, 504, 103, 204, 605, 505, 104, 205, 606, 506, 105, 206,
              607, 507, 106, 207, 608, 508, 107, 208, 609, 509, 108, 209, 610,
              510, 109, 210, 611, 511, 110, 211, 612, 512, 111, 212, 613, 513, 900]
PC = 50

Mem[PC: (PC+len(CARDIACode))] = CARDIACode

while True:
    IR = Mem[PC]
    PC += 1

    op = int(IR/100)
    param = IR - (op * 100)

    if op == 0:
        Input = input("Enter a number: ")
        Mem[param] = int(Input)
        Input = None

    elif op == 1:
        Acc = Mem[param]

    elif op == 2:
        Acc = Acc + Mem[param]

    elif op == 3:
        if Acc < 0:
            PC = param

    elif op == 4:
        left = int(param/ 10)
        right = param % 10
        Acc = (Acc * (10 ** left)) % 10000
        Acc = int(Acc / (10 ** right))

    elif op == 5:
        Output = Mem[param]
        print(Output)

    elif op == 6:
        Mem[param] = Acc

    elif op == 7:
        Acc = Acc - Mem[param]

    elif op == 8:
        pc = Mem[param]

    elif op == 9:
        break
    
