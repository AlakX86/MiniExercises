def factorial (n):
    ncounter = n - 1
    nresult = n * ncounter
    while ncounter > 0:
        ncounter = ncounter -1
        nresult = nresult * ncounter 

    return nresult
print (factorial(0))