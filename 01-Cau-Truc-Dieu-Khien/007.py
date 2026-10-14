def check_nam_nhuan(year): # tao ham
    if year%4==0 or year%100!=0 or year%400==0: # ktra dieu kien
        return "nam nhuan" # dung thi tra ve nam nhuan
    else:
        return "khong phai nam nhuan" # sai thi tra ve ko phai
try: # bat loi neu ng dung nhap so k hop le
    year = int(input("nhap nam: ")) # nhap nam
    resulf = check_nam_nhuan(year)  # ket qua
    print(f"{year} la {resulf}") # in ket qua
except ValueError: # khi ng dung nhap so k hop le
    print("nhap so hop le, nhap lai") # in