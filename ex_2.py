import os
import re
import time
import uuid
from typing import List

import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate


# region Student Example

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


def run():
    try:
        students: List[Student] = []

        if os.path.exists('assets/students.xlsx'):
            df = pd.read_excel("assets/students.xlsx")
            for index, row in df.iterrows():
                students.append(
                    Student.read(row["msv"], row["ten"], row["tuoi"], row["toan"], row["hoa"], row["ly"]))
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


# endregion


# region Input TXT Example

def load_input_file():
    with open("assets/ex2/input.txt", "r") as f:
        return f.read()


def find_max_value(files):
    max_value = 0
    for line in files:
        for value in line.split(" "):
            if int(value) > max_value:
                max_value = int(value)
    return max_value


def find_odd_value(files):
    odd_values = []
    for line in files:
        for value in line.split(" "):
            if int(value) % 2 == 1:
                odd_values.append(int(value))
    return odd_values


def find_even_value(files):
    even_values = []
    for line in files:
        for value in line.split(" "):
            if int(value) % 2 == 0:
                even_values.append(int(value))
    return even_values


def apper_each_number(files):
    apper_values = {}
    for line in files:
        for value in line.split(" "):
            if int(value) in apper_values:
                apper_values[int(value)] += 1
            else:
                apper_values[int(value)] = 1
    return apper_values


def all_prime_number(files):
    prime_numbers = []
    for line in files:
        for value in line.split(" "):
            if is_prime_number(int(value)):
                prime_numbers.append(int(value))
    return prime_numbers


def is_prime_number(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def run2():
    files = load_input_file()
    print(find_max_value(files))
    print(find_odd_value(files))
    print(find_even_value(files))
    print(apper_each_number(files))
    print(all_prime_number(files))


# endregion


# region Input XLSX Example

def load_input_file_xlsx():
    df = pd.read_excel("assets/ex2/input.xlsx")
    return df


def sort_by_name(excel_file):
    df = excel_file
    df = df.iloc[10:62, 2:8]
    df = df.rename(columns={df.columns[0]: "ho", df.columns[1]: "ten", df.columns[2]: "tuoi", df.columns[3]: "toan",
                            df.columns[4]: "ly", df.columns[5]: "hoa"})
    df = df.sort_values(by=["ten"])
    print(df)


def statistical_classification(excel_file):
    df = excel_file
    df = df.iloc[10:62, 2:8]
    df = df.rename(columns={df.columns[0]: "ho", df.columns[1]: "ten", df.columns[2]: "tuoi", df.columns[3]: "toan",
                            df.columns[4]: "ly", df.columns[5]: "hoa"})
    df = df.sort_values(by=["ten"])
    df["dtb"] = (df["toan"] + df["hoa"] + df["ly"]) / 3
    df["xep_loai"] = df["dtb"].apply(lambda x: "gioi" if x > 8 else "kha" if x >= 6.5 else "trung binh")
    df.to_excel("assets/ex2/output.xlsx", index=False)
    print(df)


def run3():
    excel_file = load_input_file_xlsx()
    sort_by_name(excel_file)
    statistical_classification(excel_file)


# endregion

# region Scapy Example
def get_table_using_request():
    url = 'https://coinmarketcap.com/'

    response = requests.get(url)
    html_content = response.content

    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find('table', {'class': 'cmc-table'})

    for i in range(1, 6):
        params = {'start': str(i * 100), 'limit': '100'}
        response = requests.get(url, params=params)
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')
        table_rows = soup.find_all('tr')
        table.extend(table_rows)

    body = table.find('tbody')

    for tr in body.find_all('tr')[:10]:
        tr.append('\n')

    # in each first tr save td>p
    with open('assets/ex3/table.csv', 'w') as f:
        for tr in body.find_all('tr')[:10]:
            line = ''
            for td in tr.find_all('td')[:11]:
                for span in td.find_all('span'):
                    temp = span.text.replace(',', '.')
                    line += temp + ','
                for p in td.find_all('p'):
                    temp = p.text.replace(',', '.')
                    line += temp + ','
                for img in td.find_all('img'):
                    class_name = re.findall(r'class="(.+?)"', str(img))
                    if 'dZMNrj' in class_name[0]:
                        if 'isUp' in class_name[0]:
                            line += 'isUp'
                        else:
                            line += 'isDown'
                    line += ','

            # dirty code
            line = line[1:-1]
            line = line.replace(',,', ',')
            word = line.split(',')[7]
            line = line.replace(word, '')
            line = line.replace(',,', ',')
            word = line.split(',')[8]
            line = line.replace(word, '')
            line = line.replace(',,', ',')
            line = line.replace(',,', ',')
            word = line.split(',')[7]
            line = line.replace(word, '')
            line = line.replace(',,', ',')
            line = line.replace(',,', ',')
            f.write(line + '\n')

    with open('assets/ex3/table.csv', 'r') as f:
        lines = f.readlines()
    lines.insert(0, 'Name,Price,1h%,24h%,7d%,MarketCap,Volume(24h),Circulating Supply,Last 7 Days, Up/Down\n')
    with open('assets/ex3/table.csv', 'w') as f:
        f.writelines(lines)

    # using pandas dataframe
    df = pd.read_csv('assets/ex3/table.csv')
    pd.set_option('display.max_columns', None)
    print(df)


# endregion


if __name__ == '__main__':
    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            get_table_using_request()
            time.sleep(5)
        except KeyboardInterrupt:
            print("Exit")
            break
