e = 1
N =[]
M =[]
O =[]
c = 0
print("please enter the first group's numbers(type finish at the end:)):")
while True:
    a = input()
    c < e
    if a == "finish":
        break
    try:
        a = float(a)
        N.append(a)
        e = len(N)
        N.sort()
    except ValueError:
        print("invalid input.")
print("enter the second group's number(type finish at the end:)):")
while True:
    b = input()
    if b == "finish":
        break
    try:
        b = float(b)
        M.append(b)
        M.sort()
        d = M[c]-N[c]
        O.append(d)
        c = c + 1
    except ValueError:
        print("invalid input.")
print(sum(O))

