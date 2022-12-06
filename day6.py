with open('6.txt') as f:
    data = f.read()

length = len(data) - 4
for i in range(length):
    set = { *data[i:i+4] }
    if len(set) == 4:
        packetstart = i
        print(i + 4)
        break
length -= 10
for i in range(packetstart, length):
    set = { *data[i:i+14] }
    if len(set) == 14:
        print(i + 14)
        break