def timUSCLN(a, b):
    while b:
        a, b = b, a % b
    return a


try:
    a = int(input("nhap so nguyen a: "))
    b = int(input("nhap so nguyen b: "))
    uscln = timUSCLN(a, b)
    print(f"USCLN cua {a} va {b} la {uscln}")
except ValueError:
    print("vui long nhap dung so nguyen")
