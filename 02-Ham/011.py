def tinhGiaiThua(n):
    t = 1
    for i in range(1, n + 1):
        t *= i
    return t


try:
    n = int(input("nhap 1 so nguyen duong n: "))

    if n < 0:
        print("giai thua khong tinh duoc so am")
    else:
        giathua = tinhGiaiThua(n)
        print(f"giai thua cua {n} la: {giathua}")
except ValueError:
    print("vui long nhap so hop le")
