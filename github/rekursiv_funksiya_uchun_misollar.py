import math
# def factorial_top(n):
    
#     if n == 0 :
#         return 1
#     elif n != 0 :
#         return math.factorial(n)
# print(factorial_top(5))


# def fibonanchi(n):
#     if n == 1 or n == 2 :
#         return 1
#     else:
#         return fibonanchi(n-1) + fibonanchi(n-2)
# print(fibonanchi(5))

# 3
# def raqamlar_yigindisi(n):
#     if n < 10 :
#         return n
#     else:
#         return n % 10 + raqamlar_yigindisi(n//10)


# 4 
# def ohirgi_son(n):
#     if n <= 10 :
#         return n
#     else:
#         return n % 10
# print(ohirgi_son(35))

# 5
# def raqamlar_soni(n):
    # if n == 1 :
        # return n
    # else:
        # return 1 + raqamlar_soni(n // 10)
# print(raqamlar_soni(145))

# 6
# def teskarilash(matn):
#     if len(matn) == 0 :
#         return " "
#     else :
#         return matn[-1] + teskarilash(matn[:-1])
# print(teskarilash('ulugbek'))

# 8
# def royhat_yigindisi(royhat):
#     if len(royhat) == 0 :
#         return 0
#     else: 
#         return royhat[0] + royhat_yigindisi(royhat[1:])
# print(royhat_yigindisi([10,20,30,40,50]))

# 9
# def royhatdagi_max(royhat):
#     if len(royhat) == 0 :
#         return 0 
#     else:
#         eng_katta = royhatdagi_max(royhat[1:])
#         if royhat[0] > eng_katta:
#             return royhat[0]
#         else:
#             return eng_katta
# print(royhatdagi_max([10,20,30,40,50,4,5,80]))




