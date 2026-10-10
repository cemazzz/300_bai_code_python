def calculate_average (scores):
    average = sum(scores) / len(scores)
    return average

def classify_student(average):
    if average >= 8.5:
        return "xuat sac"
    elif average >= 7.0 and average < 8.5:
        return "gioi"
    elif average >= 5.5 and average < 7.0:
        return "kha"
    elif average >= 4.0 and  average < 5.5:
        return "trung binh"
    elif average < 4.0:
        return "yeu"

try:
    scores = []
    num_subjects = int(input("nhap so luong mon hoc: "))
    if num_subjects <= 0:
        print("so luong mon hoc phai lon hon 0")
    else:
        for i in range(num_subjects):
            score = float(input(f"nhap so diem mon hoc thu {i+1}: "))
            if score > 10 or score < 0:
                print("diem phai tu 0-10 \nnhap lai di")
                break
            scores.append(score)
        if len(scores)==num_subjects:
            average_score = calculate_average(scores)
            classification = classify_student (average_score)
            print(f"diem trung binh la: {average_score:.2f}")
            print(f"xep hang {classification}")
except ValueError:
    print("nhap so hop le pli")