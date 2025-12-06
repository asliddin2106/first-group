ism=input("ismingizni kiriting:")
familya=input("familyangizni kiriting:")
yosh=int(input("yoshingizdi kiriting:"))
joriy_yil=int(input("Joriy yilni kiriting:"))

def yili(ism,familya,yosh):
    print(f"{familya}\n{ism} Siz  {joriy_yil-yosh}-yil tug'ilgansiz")

b=yili(ism,familya,yosh)
print(b)

#   2-misol

# n=int(input("Biron bir son kiriting:"))

# def kv_kb(n):
#     print(f"Kiritgan soningizni kvadrati: {n*n} ga teng")
#     print(f"Kiritgan soningizni kubi: {n*n*n} ga teng")

# d=kv_kb(n)
# print(d)

# 3-misol

# n=int(input("Biron bir son kiriting:"))

# def juft_toq(n):
#     if n%2==0:
#         print("Siz kiritgan son juft son")
#     else:
#         print("Siz kiritgan son toq son")

# a=juft_toq(n)
# print(a)

# 4-misol

# son1=int(input("Birinchi sonni kiriting:"))
# son2=int(input("Ikkinchi sonni kiriting:"))

# def kattasi(son1,son2):
#     if son1>son2:
#         print(f"{son1} {son2} dan katta")
#     elif son2>son1:
#         print(f"{son2} {son1} dan katta")
#     else:
#         print(f"{son1} {son2} ga teng")

# a=kattasi(son1,son2)
# print(a)

# 5-misol

# x=int(input("X sonini kiriting: "))
# n=int(input("X ning darajasini kiriting: "))

# def n_daraja(x,n):
#     print(f"{x} ning {n} chi darajasi {x**n}  ga teng ")

# d=n_daraja(x,n)
# print(d)

# 6-misol

# n=int(input("son kiriting: "))

# def son(n):
#     for i in range(2,10):
#         if n%i==0:
#             print(f"qoldiqsiz bulinuvchilar {i}")
#         else:
#             print(f"qoldiqli bulinuvchilar {i}")

# d=son(n)
# print(d)
 
# 7-misol

# n=int(input("son kiriting:"))

# def son(n):
#     while n:
#         print(n)
#         n=n-1


# a=son(n)
# print(a)

# n=int(input())

# def sa(n):
#     m=n
#     for i in range(1,n+1):
#         for j in range(m):
#             print(i,end=" ")
#         print(" ")
#         m=m-1
# sa(n)

# n=int(input(""))

# def a(n):
#     m=n
#     for i in range(1,n+1):
#         for j in range(m):
#             print(i,end=" ")
#         print(" ")
#         m=m-1

# d=a(n)
# print(d)

# n=int(input())

# def s(n):
#     m=n
#     for i in range(1,n+1):
#         for j in range(i+1):
#             print(i,end=" ")
#         print(" ")
        


# d=s(n)
# print(d)

