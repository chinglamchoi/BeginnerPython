Acc = None
IR = None
PC = None
Input = None
Output = None
Mem = [0] * 100

Mem[0] = 1
Mem[99] = 800

# code and pc
CARDIACode = [001, 002, 101, 404, 698, 198, 200, 698, 101, 702, 342,
              835, 198, 700, 699, 198, 699, 599, 900] #returns "1" no matter what
PC = 30

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
    
