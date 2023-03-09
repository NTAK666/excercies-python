import pandas as pd

from lib.ex4.db import connection_db
from lib.ex4.student import create_table_students
from lib.ex4.student_repo import StudentRepo


def get_list_student(file, mydb, cursor):
    df = file
    df = df.iloc[10:62, 1:8]
    df = df.rename(
        columns={df.columns[0]: "code", df.columns[1]: "firstName", df.columns[2]: "lastName", df.columns[3]: "dob",
                 df.columns[4]: "math",
                 df.columns[5]: "physics", df.columns[6]: "chemistry"})
    for index, row in df.iterrows():
        code = row["code"]
        firstName = row["firstName"]
        lastName = row["lastName"]
        dob = row["dob"]
        math = row["math"]
        physics = row["physics"]
        chemistry = row["chemistry"]
        StudentRepo.insert(mydb, cursor, (code, firstName, lastName, dob, math, physics, chemistry))


def exit_program():
    print("Chương trình đã kết thúc")
    exit()


def menu():
    print("MENU")
    print("1. Đọc dữ liệu từ file lưu vào DB")
    print("2. Hiển thị từ các sinh viên")
    print("3. Tạo mới một sinh viên")
    print("4. Cập nhật một sinh viên")
    print("5. Xóa một sinh viên")
    print("6. Tìm sinh viên theo id")
    print("7. Thoát chương trình")


if __name__ == '__main__':
    mydb = connection_db()
    cursor = mydb.cursor()

    create_table_students(mydb, cursor)
    readFile = pd.read_excel("input.xlsx")

    while True:
        menu()
        choice = input("Vui lòng chọn một chức năng: ")
        if choice == "1":
            get_list_student(readFile, mydb, cursor)
        elif choice == "2":
            list = StudentRepo.find_all(mydb, cursor)
            for student in list:
                print(student)
        elif choice == "3":
            code = input("Nhập mã sinh viên: ")
            firstName = input("Nhập họ và tên đệm: ")
            lastName = input("Nhập tên: ")
            dob = input("Nhập ngày sinh (yyyy-mm-dd): ")
            math = float(input("Nhập điểm toán: "))
            physics = float(input("Nhập điểm lý: "))
            chemistry = float(input("Nhập điểm hóa: "))
            StudentRepo.insert(mydb, cursor, (code, firstName, lastName, dob, math, physics, chemistry))
        elif choice == "4":
            id = input('Nhập id muốn cập nhật: ')
            studentCheck = StudentRepo.find_by_id(mydb, cursor, id)
            if studentCheck is None:
                print("Không tìm thấy sinh viên")
            else:
                code = input("Nhập mã sinh viên: ")
                firstName = input("Nhập họ và tên đệm: ")
                lastName = input("Nhập tên: ")
                dob = input("Nhập ngày sinh (yyyy-mm-dd): ")
                math = float(input("Nhập điểm toán: "))
                physics = float(input("Nhập điểm lý: "))
                chemistry = float(input("Nhập điểm hóa: "))
                StudentRepo.update(mydb, cursor, id, (code, firstName, lastName, dob, math, physics, chemistry))
                print("Cập nhật thông tin thành công")
        elif choice == "5":
            id = input('Nhập id muốn xoá: ')
            studentCheck = StudentRepo.find_by_id(mydb, cursor, id)
            if studentCheck is None:
                print("Không tìm thấy sinh viên")
            else:
                StudentRepo.delete(mydb, cursor, id)
                print("Xoá thành công")
        elif choice == "6":
            id = input('Nhập id muốn tìm: ')
            studentCheck = StudentRepo.find_by_id(mydb, cursor, id)
            if studentCheck is None:
                print("Không tìm thấy sinh viên")
            else:
                print(studentCheck)
        elif choice == "7":
            exit_program()
        else:
            print("Vui lòng chọn một lựa chọn hợp lệ.")
