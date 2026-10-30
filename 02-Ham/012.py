# def tinhtong(n):
#    t = 0
#    for i in range(1, n+1):
#        t +=i
#    return t
# my idea
def tinhtong(n):
    return (n * (n + 1)) // 2


try:
    n = int(input("nhap 1 so nguyen duong n: "))
    if n < 0:
        print("so phai lon hon 0, nhap lai!")
    else:
        resulf = tinhtong(n)
        print(f"tong cua cac so nguyen duong tu 1 den {n} la: {resulf}")
except ValueError:
    print("vui long nhap dung !")
