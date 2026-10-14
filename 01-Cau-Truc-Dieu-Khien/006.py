def print_multiplication_table():
    for i in range(1, 11):
        print("_"*23)
        print(f"| bang cuu chuong {i:>3} |")
        for j in range(1, 11):
            print(f"|{i:<2}     x {j:>4}  = {i*j:>4}|")

print_multiplication_table()