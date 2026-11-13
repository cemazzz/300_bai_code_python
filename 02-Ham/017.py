def tinhluythua(coso, somu):
    result = 1
    for _ in range(abs(somu)):
        result *= coso
    if somu < 0:
        result = 1 / result
    return result


try:
    coso = float(input("nhap co so: "))
    somu = int(input("nhap so mu: "))
    print(f"{coso} ^ {somu}: {tinhluythua(coso, somu)}")
except ValueError:
    print("vui long nhap so hop le ")
