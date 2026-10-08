
def find_max(a, b ,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
try:
    a = int(input("nhap so a: "))
    b = int(input("nhap so b: "))
    c = int(input("nhap so c: "))
    max_nunber = find_max(a, b, c)
    print(f"so lon nhat la {max_nunber}")

except ValueError:
    print(f"vui long nhap lai so hop le")



