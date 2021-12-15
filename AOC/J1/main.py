
if __name__ == '__main__':
    f = open('J1.txt', "r")
    data = f.read().split("\n")

    print(data)

    a = data[0]

Conteur = 0

dataint = [int (d) for d in data]

for i in range(0, len(dataint)-3):

    A = dataint[i] + dataint[i+1] + dataint[i+2]
    B = dataint[i+1] + dataint[i+2] + dataint[i+3]

    if B > A :
        Conteur = Conteur +1

    print("A =", A)
    print("B =", B)
    print("Conteur =", Conteur)


