def checkngto(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


try:
    n = int(input("nhap 1 so nguyen n: "))
    if checkngto(n):
        print(f"{n} la so nguyen to")
    else:
        print(f"{n} ko phai la so nguyen to")

except ValueError:
    print("nhap lai so hop le")
