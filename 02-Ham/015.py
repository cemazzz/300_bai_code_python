def TinhTong(n):
    n = abs(n)
    tong = 0
    while n > 0:
        tong += n % 10
        n //= 10
    return tong


try:
    n = int(input("nhap 1 so nguyen n: "))
    print(f"tong cac chu so cua {n} la: {TinhTong(n)}")
except ValueError:
    print("nhap lai so hop le")
