def calculate_taxi_fare(n):

    if n <= 1:
        fare = 10000
        
    elif n <= 10:
        fare = 10000 + (n-1)*8500
    else:
        fare = 10000 + 9*8500 + (n-10)*7500
    return fare

try:
    
    distance = float(input("nhap so km da di: "))
    if distance < 0:
        print("so km phai lon hon 0")
    else:
        total_fare = calculate_taxi_fare(distance)
        print(f"tong tien taxi la {total_fare:,.0f} VND")
except ValueError:
    print("nhap so hop le pli")