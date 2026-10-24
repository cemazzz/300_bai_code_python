def kiemtrachanle(numbers) :
    sl_sochan = 0
    sl_sole = 0
    for i in numbers:
        if i%2==0 :
            sl_sochan +=1   
        else:
            sl_sole +=1     
    return sl_sochan, sl_sole
try:
    input_list = input("nhap so nguyen: ")
    numbers = [int(num) for num in input_list.split()]
    chan, le = kiemtrachanle(numbers)
    print(f"so luong so chan: {chan} ")
    print(f"so luong so le:  {le} ")
except ValueError:
    print("nhap lai so hop le")