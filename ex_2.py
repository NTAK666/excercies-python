import os
import uuid
from typing import List
import pandas as pd
import openpyxl
import xlwt


class Student:
    def __init__(self, ten, tuoi, toan, hoa, ly):
        self.msv = uuid.uuid4()
        self.ten = ten
        self.tuoi = tuoi
        self.toan = toan
        self.hoa = hoa
        self.ly = ly
        self.dtb = (int(toan) + int(hoa) + int(ly)) / 3

    @classmethod
    def read(cls, msv, ten, tuoi, toan, hoa, ly):
        student = cls(ten, tuoi, toan, hoa, ly)
        student.msv = msv
        return student

    def __str__(self):
        return f"MSV: {self.msv}, Ten: {self.ten}, Tuoi: {self.tuoi}, Toan: {self.toan}, Hoa: {self.hoa}, Ly: {self.ly}, DTB: {self.dtb}"

    @staticmethod
    def input_student(students_list):
        try:
            while True:
                ten = str(input("Nhap ten: "))
                if ten == "":
                    print("Ten khong duoc de trong!")
                    continue
                tuoi = int(input("Nhap tuoi: "))
                if not isinstance(tuoi, int):
                    print("Tuoi phai la so!")
                    continue
                if tuoi < 0 | tuoi > 100:
                    print("Tuoi khong duoc nho hon 0!")
                    continue
                toan = int(input("Nhap diem toan: "))
                if not isinstance(toan, int):
                    print("Diem toan phai la so!")
                    continue
                if toan > 10:
                    print("Diem khong duoc nho hon 0!")
                    continue
                hoa = int(input("Nhap diem hoa: "))
                if not isinstance(hoa, int):
                    print("Diem toan phai la so!")
                    continue
                if hoa > 10:
                    print("Diem khong duoc nho hon 0!")
                    continue
                ly = int(input("Nhap diem ly: "))
                if not isinstance(ly, int):
                    print("Diem toan phai la so!")
                    continue
                if ly > 10:
                    print("Diem khong duoc nho hon 0!")
                    continue
                students_list.append(Student(ten, tuoi, toan, hoa, ly))
                if input("Nhap tiep? (y/n): ") == "n":
                    break
            return students_list
        except Exception as e:
            print(e)


if __name__ == "__main__":
    try:
        students: List[Student] = []

        if os.path.exists('assets/students.xlsx'):
            df = pd.read_excel("assets/students.xlsx")
            for index, row in df.iterrows():
                students.append(Student.read(row["msv"], row["ten"], row["tuoi"], row["toan"], row["hoa"], row["ly"]))
            print(f"Loaded {len(students)} in students.xlsx: ")
            delete = input("Delete all old students? (y/n (default)): ")
            if delete == "y":
                students.clear()
                print("Deleted all!")

        Student.input_student(students)
        mode: int = int(input("Nhap mode sort (1: sort theo dtb tang dan, 2: sort theo dtb giam dan): "))

        if mode == 1:
            students.sort(key=lambda student: student.dtb)
        elif mode == 2:
            students.sort(key=lambda student: student.dtb, reverse=True)

        df = pd.DataFrame([student.__dict__ for student in students])
        df.to_excel("assets/students.xlsx", index=False)

        print("Done!")
    except Exception as e:
        print(e)
