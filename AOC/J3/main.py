if __name__ == '__main__':
    f = open('J3.txt', "r")
    data = f.read().split("\n")


    print(data)


epsilon = [11]
gamma = 0

A = 0

for i in range(0, len(data)):

    for j in range(0, len(epsilon)):

        if '0' == data[i][j]:
            print("zero")
            A = A - 1
            print(j)

        if 1 == int(data[i][j]):
            print("un")
            A = A + 1
            print(j)

        if A > 0:
                epsilon[j] = '1'
                A = 0
        else:
                epsilon[j] = '0'
                A = 0




print("epsilon =", epsilon[11])

power = epsilon * gamma
print("power =", power)