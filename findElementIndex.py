def findElement(list, value):
    if value in list:
            return list.index(value)
    else:
        return -1
print(findElement(["alpha","beta", "gama"],"gama"))