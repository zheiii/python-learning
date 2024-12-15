N =[]
M =[]
O =[]
c = 0
print("please enter the first group's numbers(type finish at the end:)):")
while True:
    a = input()
    if a == "finish":
        break
    try:
        a = float(a)
        N.append(a)
        e = len(N)
    except ValueError:
        print("invalid input.")
print("enter the second group's numbers(type finish at the end:)):")
while True:
    b = input()
    if b == "finish":
        break
    try:
        b = float(b)
        M.append(b)
        M.sort()
        N.sort()
    except ValueError:
        print("invalid input.")
while c < e:
    d = abs(M[c]-N[c])
    O.append(d)
    c = c + 1
print(sum(O))

