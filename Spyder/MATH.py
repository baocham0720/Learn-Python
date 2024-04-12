# -*- coding: utf-8 -*-
"""
Nội dung: 
    
    Phép toán học trong Python
    &
    Thư viện toán học MATH
"""

#Phép toán cơ bản
a = input ("Nhập vào số a:")
print ("kiểu dữ liệu của a: ", type(a))
a = float(a)
print ("kiểu dữ liệu của a: ", type(a))

b = input ("Nhập vào số b:")
print ("kiểu dữ liệu của a: ", type(b))
b = float(b)
print ("kiểu dữ liệu của a: ", type(a))


print("{0}+{1} = {2}".format(a, b, a+b))
print("{0}-{1} = {2}".format(a, b, a-b))
print("{0}*{1} = {2}".format(a, b, a*b))
print("{0}/{1} = {2}".format(a, b, a/b))
print("{0}%{1} = {2}".format(a, b, a%b)) #chia lấy phần dư: %
print("{0}**{1} = {2}".format(a, b, a**b)) #mũ: **
print("{0}//{1} = {2}".format(a, b, a//b)) #chia lấy phần nguyên: //

#Toán tử so sánh
x = int(input("x")) 
y = int(input("y"))

#True or false
print("{0}>{1} là {2}".format(x, y, x>y))
print("{0}<{1} là {2}".format(x, y, x<y))
print("{0}=={1} là {2}".format(x, y, x==y)) #bằng: ==
print("{0}!={1} là {2}".format(x, y, x!=y))#khác, không bằng: !=
print("{0}>={1} là {2}".format(x, y, x>=y))
print("{0}<={1} là {2}".format(x, y, x<=y))


#Toán Logic
z = int(input("z"))
print ((x<y) and (y<z))
print ((x<y) or (y<z))
print (not(x>z))


#Toán tử gán
#ex: a=5, a+=5 ~ a=a+5


#Thư viện toán học MATH
"""
- math.ceil(x): trả về giá trị trần của x, số nguyên nhỏ nhất >= x
- math.fabs(x): trả vè giá trị tuyệt đối của x
- math.floor(x): trả về sàn của x, sô nguyên lớn nhất <= x
- math.exp(x): trả về e luỹ thừa x, trong đó e = 2.718281...là cơ số của logarit tự nhiên
- math.log(x [,base]): với một đối số, trả về logarit tự nhiên của x (cơ số e)
- math.pow(x,y): trả về x luỹ thừa 
- math.pi
- math.e

"""

import math
x = float(input("x: "))

print ("pi = ", math.pi)

print ("|x|= ", math.fabs(x)) #giá trị tuyệt đối

print ("sqrt(x)= ", math.sqrt(x))  #căn bậc 2

print ("ceil(x)= ", math.ceil(x))

print ("floor(x)= ", math.floor(x))


#Toán tử điều kiện, toán tử ba ngôi
"""
Cú pháp:
    [trả về điều kiện đúng]
    if [điều kiện] #5>3
    else [trả về điều kiện sai] 
    
"""

x = input("Nhập vào số nguyên: ")
x = int(x)

kq = "Chẵn" if (x%2==0) else "lẻ"
 
print (x, "là số", kq)


#Câu lệnh rẻ nhánh if...elif...else
x = input("Nhập số nguyên x: ")
x = int(x)

#Dạng 1: if
if x>=0:
    print(x, "X là số dương")
    
#Dạng 2: if...else
if x%2==0:
    print(x, "là số chẵn")
else:
    print(x, "là số lẻ")

print("Kết thúc chương trình")

#Dạng 3: if...elif...else
if x>=9:
    print("Xuất sắc")
elif x >=8:
    print("Giỏi")
elif x >=7:
    print("Khá")
elif x >=5:
    print("Trung Bình")
else:
    print("yếu")
    
print("Kết thúc chương trình")
    
    
#Homework
#Giải phương trình bậc 2: ax^2 + bx + c = 0

import math

#Nhập dữ liệu
print ("Giải pt: ax^2 + bc + c = 0")

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

print ("{0}x^2+{1}x+{2}=0".format(a,b,c))

if(a != 0):
    delta = b**2 - 4*a*c
    if(delta<0):
        print("PT vô nghiệm")
    elif(delta==0):
        x =-b/(2*a)
        print("Có nghiệm kép x1=x2=", x)
    else:
        x1 = (-b-math.sqrt(delta))/(2*a)
        x2 = (-b+math.sqrt(delta))/(2*a)
        print("có nghiệm kép x1={0} và x2={1}".format(x1, x2))
else:
    print("Không phải phương trình bậc 2")


#Tính diện tích và chu vi tam giác 
"""
Đề: Nhập 3 diểm trên hệ truc toạ độ Oxy.
1. Xác định 3 điểm có tạo thành tam giác không?
2. Nếu tạo thành tam giác:
    - Xuất ra chu vi của tam giác
    - Xuất ra diện tích của tam giác

"""

#Nhập dữ liệu
xA = float(input("Nhập vào xA: "))
yA = float(input("Nhập vào yA: "))
xB = float(input("Nhập vào xB: "))
yB = float(input("Nhập vào yB: "))
xC = float(input("Nhập vào xC: "))
yC = float(input("Nhập vào yC: "))

ab = math.sqrt((xB-xA)**2 + (yB-yA)**2)
bc = math.sqrt((xC-xB)**2 + (yC-yB)**2)
ac = math.sqrt((xC-xA)**2 + (yC-yA)**2)

#Kiểm tra
if (ab+bc > ac) and (ab+ac > bc) and (bc+ac > ab):
    
    cv = ab+bc+ac
    print("chu vi = ", cv)
    
    p = cv/2
    s = math.sqrt(p*(p-ab)*(p-bc)*(p-ac))
    print("Diện tích = ", s)
    
else:
    print("Không tạo thành tam giác")


