def find_max(numbers):
    if not numbers:
        return "danh sach rong, k co so lon nhat"
    max_numbers = numbers[0]
    for num in numbers:
        if num > max_numbers:
            max_numbers = num
    return max_numbers


try:
    n = input("nhap cac so, cach nhau boi dau cach: ")
    numbers = [float(num) for num in n.split()]
    if not numbers:
        print("danh sach rong, k co so lon nhat")
    else:
        max = find_max(numbers)
        print(f"so lon nhat trong danh sach la {max}")

except ValueError:
    print("nhap lai so hop le")
