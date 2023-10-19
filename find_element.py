def findElement(list, value):
    count = 0
    for input in list:
        if value == input:
            return count
        count += 1
    return -1
print(findElement(["alpha","beta", "gama"],"gama"))