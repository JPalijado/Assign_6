def InputFourNumbers():
    n1 = int(input("Enter the 1st number: "))
    n2 = int(input("Enter the 2nd number: "))
    n3 = int(input("Enter the 3rd number: "))
    n4 = int(input("Enter the 4th number: "))
    return n1,n2, n3, n4

def DisplayLowestNumber(n1, n2, n3, n4):
    if n1 < n2 and n1 < n3 and n1 < n4:
        if n1 < n2 and n2 < n3 and n3 < n4:
            print(f"\n{n4}, {n3}, {n2}, {n1}")
        elif n1 < n2 and n2 < n4 and n4 < n3:
            print(f"\n{n3}, {n4}, {n2}, {n1}")
        elif n1 < n3 and n3 < n4 and n4 < n2:
            print(f"\n{n2}, {n4}, {n3}, {n1}")
        elif n1 < n3 and n3 < n2 and n2 < n4:
            print(f"\n{n4}, {n2}, {n3}, {n1}")
        elif n1 < n4 and n4 < n2 and n2 < n3:
            print(f"\n{n3}, {n2}, {n4}, {n1}")
        else:
            print(f"\n{n2}, {n3}, {n4}, {n1}")
    elif n2 < n1 and n2 < n3 and n2 < n4:
        if n2 < n1 and n1 < n3 and n3 < n4:
            print(f"\n{n4}, {n3}, {n1}, {n2}")
        elif n2 < n1 and n1 < n4 and n4 < n3:
            print(f"\n{n3}, {n4}, {n1}, {n2}")
        elif n2 < n3 and n3 < n4 and n4 < n1:
            print(f"\n{n1}, {n4}, {n3}, {n2}")
        elif n2 < n3 and n3 < n1 and n1 < n4:
            print(f"\n{n4}, {n1}, {n3}, {n2}")
        elif n2 < n4 and n4 < n1 and n1 < n3:
            print(f"\n{n3}, {n1}, {n4}, {n2}")
        else:
            print(f"\n{n1}, {n3}, {n4}, {n2}")
    elif n3 < n1 and n3 < n2 and n3 < n4: 
        if n3 < n1 and n1 < n2 and n2 < n4:
            print(f"\n{n4}, {n2}, {n1}, {n3}")
        elif n3 < n1 and n1 < n4 and n4 < n2:
            print(f"\n{n2}, {n4}, {n1}, {n3}")
        elif n3 < n2 and n2 < n4 and n4 < n1:
            print(f"\n{n1}, {n4}, {n2}, {n3}")
        elif n3 < n2 and n2 < n1 and n1 < n4:
            print(f"\n{n4}, {n1}, {n2}, {n3}")
        elif n3 < n4 and n4 < n1 and n1 < n2:
            print(f"\n{n2}, {n1}, {n4}, {n3}")
        else:
            print(f"\n{n1}, {n2}, {n4}, {n3}")
    else:
        if n4 < n1 and n1 < n2 and n2 < n3:
            print(f"\n{n3}, {n2}, {n1}, {n4}") 
        elif n4 < n1 and n1 < n3 and n3 < n2:
            print(f"\n{n2}, {n3}, {n1}, {n4}")
        elif n4 < n2 and n2 < n3 and n3 < n1:
            print(f"\n{n1}, {n3}, {n2}, {n4}")
        elif n4 < n2 and n2 < n1 and n1 < n3:
            print(f"\n{n3}, {n1}, {n2}, {n4}")
        elif n4 < n3 and n3 < n2 and n2 < n1:
            print(f"\n{n1}, {n2}, {n3}, {n4}")
        else:
            print(f"\n{n2}, {n1}, {n3}, {n4}")

n1, n2, n3, n4 = InputFourNumbers()

DisplayLowestNumber(n1, n2, n3, n4)