##등비수열
# a1 = int(input("첫 항 : "))
# r = int(input("공비 : "))
# n = int(input("항의 수 : "))


# valueN = 0
# N = 1

# while N <= n :
#     if N == 1:
#         valueN = a1
#         print(f"{n}번째 항의 값 : {valueN}")
#         N = N+1
#         continue
#     valueN = valueN *  r
#     print(f"{N}번째 항의 값 : {valueN}")
#     N = N+1

# print(f"{n}번째 항의 값 : {valueN}")

##등비수열 일반항

# a1 = int(input("첫 항 : "))
# r = int(input("공비 : "))
# n = int(input("항의 수 : "))

# print(f"{n}번째 항의 값 : {a1*(r**(n-1))}")


##등비수열의 합

# a1 = int(input("첫 항 : "))
# r = int(input("공비 : "))
# n = int(input("항의 수 : "))

# valueN = 0
# N = 1
# sum = 0

# while N <= n :
#     if N == 1:
#         valueN = a1
#         sum = valueN
#         print(f"{N}번째까지의 합 : {sum}")
#         N = N+1
#         continue
#     valueN = valueN *  r
#     sum = sum + valueN
#     print(f"{N}번째까지의 합 : {sum}")
#     N = N+1

# print(f"{n}번째까지의 값 : {sum}")


##등비수열의 합공식

# a1 = int(input("첫 항 : "))
# r = int(input("공비 : "))
# n = int(input("항의 수 : "))

# value = a1 * ((1-r**n) / (1-r))

# print(f"{n}번째 항까지의 합 : {int(value)}")


##시그마
##an = a1 + (n-1)d
##sn = n(a1 + an)/2
# inputN1 = int(input("a1 입력 : "))
# inputD = int(input("공차 입력 : "))
# inputN = int(input("n 입력 : "))

# valueN = inputN1 + (inputN - 1) * inputD
# sumN = inputN * (inputN1 + valueN) / 2
# print(f"{inputN}번째 항까지의 합 : {int(sumN)}")


##sn = a1 * (1-r^n)/(1-r)
# inputN1 = int(input("a1 입력 : "))
# inputR = int(input("공비 입력 : "))
# inputN = int(input("n 입력 : "))

# sumN = inputN1 * (1-inputR**inputN)/(1-inputR)

# print(f"{inputN}번째 항까지의 합 : {int(sumN)}")


##계차 수열
## an = {3, 7, 13, 21, 31, 43, 57}
## bn = {4, 6, 8, 10, 12, 14}

# inputAN1 = int(input("a1 입력 : "))
# inputAN = int(input("an 입력 : "))

# inputBN1 = int(input("b1 입력 : "))
# inputBN = int(input("bn 공차 입력 : "))

# valueAN = 0
# valueBN = 0

# n = 1
# while n <= inputAN:
#     if n ==1:
#         valueAN = inputAN1
#         valueBN = inputBN1
#         print(f"an의 {n}번째 항의 값은 : {valueAN}")
#         print(f"bn의 {n}번째 항의 값은 : {valueBN}")
#         n += 1
#         continue

#     valueAN = valueAN + valueBN
#     valueBN = valueBN + inputBN

#     print(f"an의 {n}번째 항의 값은 : {valueAN}")
#     print(f"bn의 {n}번째 항의 값은 : {valueBN}")
#     n += 1

# print(f"an의 {inputAN}번째 항의 값은 : {valueAN}")
# print(f"bn의 {inputAN}번째 항의 값은 : {valueBN}")


## an = n^2 + n + 1

# inputAN1 = int(input("a1 입력 : "))
# inputAN = int(input("an 입력 : "))

# valueAN = inputAN ** 2 + inputAN + 1
# print(f"an의 {inputAN}번째 항의 값은 : {valueAN}")


##피보나치 수열

# inputN = int(input("n 입력 : "))

# valueN = 0
# sumN = 0

# valuePreN2 = 0
# valuePreN1 = 0

# n = 1
# while n <= inputN:
#     if n == 1 or n == 2:
#         valueN = 1
#         valuePreN2 = valueN
#         valuePreN1 = valueN
#         sumN = sumN + valueN
#         n += 1

#     else:
#         valueN = valuePreN2 + valuePreN1
#         valuePreN2 = valuePreN1
#         valuePreN1 = valueN
#         sumN = sumN + valueN
#         n += 1

# print(f"{inputN}번째 항의 값 : {valueN}")
# print(f"{inputN}번째 항까지의 합 : {sumN}")


##팩토리얼

# inputN = int(input("n 입력 : "))

# result = 1
# for n in range(1, inputN+1):
#     result = result * n

# print(f"{inputN}! = {result}")



##군수열
##예) 1
# inputN = int(input("n항 입력 : "))

# flag = True
# n = 1; nCnt = 1; searchN = 0
# while flag:
#     for i in range(1,n+1):
#         print(f"{i} ", end = '')

#         nCnt += 1

#         if nCnt > inputN:
#             searchN = i
#             flag = False
#             break
#     print()
#     n += 1

# print(f"{inputN}항 : {searchN}")

##예)2
# inputN = int(input("n항 입력 : "))

# flag = True
# n = 1; nCnt = 1; searchNC = 0; searchNP = 0
# while flag:
#     for i in range(1,n+1):
#         print(f"{i}/{n - i + 1} ", end = '')

#         nCnt += 1

#         if nCnt > inputN:
#             searchNC = i
#             searchNP = n - i + 1
#             flag = False
#             break
#     print()
#     n += 1

# print(f"{inputN}항 : {searchNC}/{searchNP}")



##순열

# numN = int(input("n 입력 : "))
# numR = int(input("r 입력 : "))
# result = 1

# for n in range(numN, (numN-numR), -1):
#     print(f"n : {n}")
#     result = result * n

# print(f"result : {result}")

##원 순열
# n = int(input("친구 수 입력 : "))
# result = 1
# for i in range(1,n):
#     result *= i

# print(f"result : {result}")


##조합
# numN = int(input("n 입력 : "))
# numR = int(input("r 입력 : "))
# resultP = 1
# resultR = 1
# resultC = 1

# for n in range(numN, (numN-numR), -1):
#     print(f"n : {n}")
#     resultP = resultP * n
# print(f"resultP : {resultP}")

# for n in range(numR, 0, -1):
#     print(f"n : {n}")
#     resultR = resultR * n

# print(f"resultR : {resultR}")

# resultC = int(resultP/resultR)
# print(f"resultC : {resultC}")


##확률
# def proFun():
#     numN = int(input("n 입력 : "))
#     numR = int(input("r 입력 : "))

#     resultP = 1
#     resultR = 1
#     resultC = 1

#     for n in range(numN, (numN-numR), -1):
#         resultP = resultP * n
#     print(f"resultP : {resultP}")


#     for n in range(numR, 0, -1):
#         resultR = resultR * n
#     print(f"resultR : {resultR}")

#     resultC = int(resultP/resultR)
#     print(f"resultC : {resultC}")

#     return resultC

# sample = proFun()
# print(f"sample : {sample}")

# event1 = proFun()
# print(f"event1 : {event1}")

# event2 = proFun()
# print(f"event2 : {event2}")

# probability = (event1*event2)/sample
# print(f"probability : {round(probability * 100, 2)}%")