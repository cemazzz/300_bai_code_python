def is_palindrome(s):
    s = "".join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]


input_string = input("nhap 1 chuoi: ")
if is_palindrome(input_string):
    print(f'"{input_string}" la palindrome.')
else:
    print(f'"{input_string}" khong phai la palindrome.')
