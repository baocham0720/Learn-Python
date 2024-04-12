#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 11:11:01 2024

@author: user

Noi dung: Gioi thieu cua lenh Print

"""

#Cac loai Print
print(5)
print ("Hello world")

#viet tren mot dong thi ngat bang ;
print(6);print("hello")

#truyen nhieu doi tuowng cung luc ngan cach ,
print ("xin", "Chao", 1234)

#ngan cach bang sep=","
print ("Xin", "chao", 1234, sep=",")

#ket thuc bang dau : dung end=":"
print ("Xin", "chao", end=":")
print(1234)

#Dua du lieu xuong file
print ('Ten={0}, Ho={1}'.format('abc', 'vn'))


"""
Noi dung: Gioi thieu cau lenh nhap Input

"""

input ("Nhap vao mot con so:")

a = input ("Nhap vao a:")
print ("a={0}".format(a))

ho = input ("Nhap vao ho:");
ten = input("nhap vao ten:");
print("Xin chao", ho, ten)

"""
Noi dung:
Bien, hang so, tu khoa trong Python

"""

#Bien
x=5
print(x)

y=5
y=10
print(y)

x, y, z = 1, 2, "Xin chao"
print(x)
print(y)
print(z)

x = y = z = "Xin Chao"
print(x)
print(y)
print(z)

#Hang so : viet hoa 100%
PI = 3.14
print (PI)

PI = 3.1423
print (PI)

import math
print (math.pi)

#cach dat ten cho bien va hang so : (a-z)(A-z)(0-9) hoac _
content = "Hoc lap trinh Python"

ho_ten = "VAN A"

fullName = "VAN A"

#Cac tu khoa:


    
"""
Noi dung:

Kieu du lieu trong Python

"""

#Kiem tra du lien bien

x = 1
print (type(x)) #type(ten bien) la hien kieu du lieu cua bien

x = 1.0 
print (type(x))

x = 1 + 2j
print (type (x))

x = True
print (type(x))

x = 'abc'
print (type(x))

x = None
print (type(x))

e = 2.72
pi = "3.14"
text = "Hello world"
print ("kieu du lieu cua bien e:", type(e),
       "Kieu du lieu bien text:", type(text), 
       "Kieu du lieu cua bien pi:", type(pi))



"""
Noi dung:

Chuyen doi kieu du lieu

"""

a = 5
b = 2.0
c = a/b
print (c)
print ("Kieu du lieu cua a:", type(a))
print ("Kieu du lieu cua a:", type(b))
print ("Kieu du lieu cua a:", type(c))

#EX:
n = 100
m = 200
print (n + m)

#chuyen doi kieu ro rang bang ham co san

n = 100
m ="200"
#ep kieu dung int, float, str
print (str(n) + m)
print (n + int(m))



