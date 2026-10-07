
def check_number(n):
    if n>0:
        return"day la so duong"
    elif n < 0:
        return"day la so am"
    else:
        return"day la so 0"
try:
    number = int(input("nhap 1 so bat ky: "))

    result = check_number(number)
    print(result)
except ValueError:

    print("pli nhap 1 so nguyen hop le")