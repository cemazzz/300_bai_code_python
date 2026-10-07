
def check_number(n):
    if n%2==0:
        return"day la so chan"
    else:
        return"day la so le"
try:
    number = int(input("nhap 1 so bat ky: "))

    result = check_number(number)
    print(result)
except ValueError:

    print("pli nhap 1 so nguyen hop le")