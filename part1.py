def InputFourNumbers():
    n1 = int(input("Enter the 1st number: "))
    n2 = int(input("Enter the 2nd number: "))
    n3 = int(input("Enter the 3rd number: "))
    n4 = int(input("Enter the 4th number: "))
    return n1,n2, n3, n4

def DisplayLowestNumber(n1, n2, n3, n4):
    if (n1 < n2 and n2 < n3 and n3 < n4) or (n1 < n2 and n2 < n4 and n4 < n3) or (n1 < n3 and n3 < n4 and n4 < n2) or (n1 < n3 and n3 < n2 and n2 < n4) or (n1 < n4 and n4 < n2 and n2 < n3) or (n1 < n4 and n4 < n3 and n3 < n2):
        print("\nThe lowest number is:",n1)
    elif (n2 < n1 and n1 < n3 and n3 < n4) or (n2 < n1 and n1 < n4 and n4 < n3) or (n2 < n3 and n3 < n4 and n4 < n1) or (n2 < n3 and n3 < n1 and n1 < n4) or (n2 < n4 and n4 < n1 and n1 < n3) or (n2 < n4 and n4 < n3 and n3 < n1):
        print("\nThe lowest number is:",n2)
    elif (n3 < n1 and n1 < n2 and n2 < n4) or (n3 < n1 and n1 < n4 and n4 < n2) or (n3 < n2 and n2 < n4 and n4 < n1) or (n3 < n2 and n2 < n1 and n1 < n4) or (n3 < n4 and n4 < n1 and n1 < n2) or (n3 < n4 and n4 < n2 and n2 < n1):
        print("\nThe lowest number is:",n3)
    else:
        print("\nThe lowest number is:",n4)

n1, n2, n3, n4 = InputFourNumbers()

DisplayLowestNumber(n1, n2, n3, n4)