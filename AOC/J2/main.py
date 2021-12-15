if __name__ == '__main__':
    f = open('J2.txt', "r")
    data = f.read().split("\n")


    print(data)

position = 0
depth = 0
aim = 0

for i in range(0, len(data)):

    if 'forward' == data[i].split(" ")[0]:
        position = position + int(data[i].split(" ")[1])
        depth = depth + (int(data[i].split(" ")[1]) * aim)

    if 'up' == data[i].split(" ")[0]:
        # depth = depth - int(data[i].split(" ")[1])#
        aim = aim - int(data[i].split(" ")[1])

    if 'down' == data[i].split(" ")[0]:
        #depth = depth + int(data[i].split(" ")[1])#
        aim = aim + int(data[i].split(" ")[1])


print("position =", position)
print("depth =", depth)
Sousmarin = depth * position
print("Sousmarin =",Sousmarin)

