for a in range(1,101):
    if(a % 8 == 0):
        continue
    elif(a % 10 == 8 or a // 10 == 8):
        continue
    print(a)
