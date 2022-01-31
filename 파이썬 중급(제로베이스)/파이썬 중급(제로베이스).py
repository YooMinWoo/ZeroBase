# #중첩함수(함수 안에 또 다른 함수!)

# def calculator(n1, n2, operator):
#     def addCal():
#         print(f"덧셈 연산 : {n1 + n2}")
#     def subCal():
#         print(f"뺄셈 연산 : {n1 - n2}")
#     def mulCal():
#         print(f"곱셈 연산 : {n1 * n2}")
#     def divCal():
#         print(f"나눗셈 연산 : {n1 / n2}")

#     if operator == 1:
#         addCal()
#     elif operator == 2:
#         subCal()
#     elif operator == 3:
#         mulCal()
#     elif operator == 4:
#         divCal()

# while True:
#     num1 = float(input("실수(n1) 입력 : "))
#     num2 = float(input("실수(n2) 입력 : "))
#     operatorNum = int(input("1. 덧셈, 2. 뺄셈, 3. 곱셈, 4. 나눗셈, 5.종료"))

#     if operatorNum == 5:
#         print("Bye~")
#         break

#     calculator(num1, num2, operatorNum)


# #lambda 함수
# # def calcuator(n1, n2):
# #     return n1 + n2

# # returnValue = calcuator(10, 20)
# # print(f"returnValue : {returnValue}")

# calcuator = lambda n1, n2 : n1 + n2
# returnValue = calcuator(10, 20)
# print(f"returnValue : {returnValue}")


# #모듈
# #0부터 100사이의 난수 10개 발생
# import random

# rNums = random.sample(range(1,101),10)
# print(f"rNums : {rNums}")



#모듈제작
#새 파일을 만든 후 함수를 선언하고
#import [파일명]을 한 뒤,
#파일 안에 있는 함수를 호출한다.



