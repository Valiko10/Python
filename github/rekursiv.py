# def ngacha(n):
#  if n == 1 or n == 2 :
#     return 1
#  else:
#    return ngacha(n-1) + ngacha(n - 2)
 

# for i in range(1,50):
#     print(ngacha(i))


# def hisobla(n):
#    if n == 0 :
#       return 0
#    else: return n+ hisobla(n-1)
# print(hisobla(10))














# 1
# def faktorial(n):
#    if n == 1 :
#       return 1
#    else: return faktorial(n-1)*n
# print(faktorial(5))
    
# 2
# def son_chiqar(n) :
#    if n == 1 :
#       return 
#    print(n)
#    son_chiqar(n-1)
# print(son_chiqar(100))

# 3
# def fibonanchi(n):
#    if n == 1 or n == 2 :
#       return 1
#    else:
#       return fibonanchi(n-1) + fibonanchi(n - 2)
# print(fibonanchi(5))






# 11
# def salom_chiqar():
#     ism = input('ismingizni kiriting:').title().strip()
#     print(f"Salom, <{ism}>!")
# salom_chiqar()




# 12
# def kvadrat_top(a) :
#     s = a**2
#     return s
# print(kvadrat_top(10))

# 13
# def kattasini_top(a,b):
#     s = max(a,b)
#     return s 
# print(kattasini_top(5,8))

# 14
# royhat = [1,3,4,7,6]
# def yigindi_top():
#     s = sum(royhat) 
#     return s 
# print(yigindi_top())

# 15
# def unli_aniqla():
#     soz = input('soz:').lower().strip()
#     unlilar = 0
#     for i in range(len(soz)):
#         if 'e' == soz[i] or 'u' == soz[i] or 'i' == soz[i] or 'o' == soz[i] or  'a' == soz[i] :
#             unlilar +=1
#     return unlilar
# print(unli_aniqla())
            

# 18
# def kichchisini_top(a,b,c):
#     s = min(a,b,c)
#     return s 
# print(kichchisini_top(5,8,6))

# soz = ', '.join(base_words)

# 19
# def son_ajrat():
#     matn = str(input(':'))
#     sonlar = []
#     for i in range(len(matn)):
#         if matn[i] == '0' or matn[i] == '1' or matn[i] == '2' or matn[i] == '3' or matn[i] == '4' or matn[i] == '5' or matn[i] == '6' or matn[i] == '7' or matn[i] == '8' or matn[i] == '9':
#             sonlar.append(matn[i])
#     soz = ' , '.join(sonlar)
#     return soz
# print(son_ajrat())


# 20
# def parolni_bahola(parol):
#     if len(parol ) >= 8:
#         return 'kuchli parol'
#     else : return 'kuchsiz parol'
# print(parolni_bahola('asd'))


def teskari_sanash(son):
    if son == 0:
        return
    print(son)
    teskari_sanash(son-1)

teskari_sanash(10)