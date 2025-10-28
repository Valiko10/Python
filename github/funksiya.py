import math
from sozlar import base_words
royhat = [1,2,-3,4,5,6,-7,-8,9,10]
# print(royhat[::-1])

# soz = input(':')



# def bosh_harf_top():
#     soni = 0
#     for i in soz :
#         if i.lower() != i :
#             soni +=1
#     return soni
# print(bosh_harf_top())

# def bosh_harf_top():
#     for i in soz :
#         if i.lower() != i :
#             print(i)

# print(bosh_harf_top())


# def salomber():
#     print('salom')

# salomber()


# def tub_or_tubemas(son):
#     if son%2==1:
#         if son % 3 != 1 and son % 5 != 1 and son % 7 != 1:
#             print('tub son')
#     else: print('tub emas')
    
# tub_or_tubemas(159)
# print("salom")





# import random 
# from sozlar import base_words
# print(base_words)




# def kavadrat_kotar(a) :
#     print(a**2)
# kavadrat_kotar(5,)

# 2
# def kub_kotar(a) :
#     print(a**3)
# kavadrat_kotar(5)

# def factoriyal_kotar(n):
#     print(math.factorial(n))
# factoriyal_kotar(13)

# def tok_juft(n):
#     if n % 2 == 0 :
#         print('juft son')
#     else:print('toq son')
# tok_juft(2)

# def ildiz(n) :
#     m = math.sqrt(n)
#     return m
# print(ildiz(17))

# def kattani_top(n,m):
#     if n > m :
#         print(f'{n} {m} dan katta')
#     elif n < m :
#         print(f'{m} {n} dan katta')
#     else:print(f'{n} {m} ular teng')
# kattani_top(5,9)

# def orta_qiymat(a,b):
#     print((a+b)/2)
# orta_qiymat(5,3)



# def sonlarni_qosh():
#     yigindi =0
#     for i in royhat :
#         yigindi += i
#     return yigindi
# print(sonlarni_qosh())

# def katta_son():
#     katta = max(royhat)
#     return katta
# print(katta_son())

# def kichik_son():
#     kichik = min(royhat)
#     return kichik
# print(kichik_son())

# 11
# def soz_soni():
#     soni = len(base_words)
#     return soni
# print(soz_soni())

# def harf_soni() :
#     soni = 0
#     for i in soz :
#         if i != ' ':
#             soni +=1
#     return soni
# print(harf_soni())

# def uzun_soz():
#     uzun = sorted(base_words , key=len)
#     return uzun[-1]
# print(uzun_soz())

# def teskari_soz():
#     return soz[::-1]
# print(teskari_soz())

# def orta_arifmetik():
#     javob = 0 
#     soni = 0
#     for i in royhat :
#         javob +=i
#         soni +=1
#     return javob / soni
# print(orta_arifmetik())

# def ndan_gacha():
#     n = int(input(':'))
#     soni = 0
#     for i in range(1,n+1):
#         soni +=i
#     return soni
# print(ndan_gacha())

# def ndan_gacha():
#     n = int(input(':'))
#     soni = 1
#     for i in range(1,n+1):
#         soni *=i
#     return soni
# print(ndan_gacha())

# def juf_chiqar():
#     sonlar = []
#     for i in royhat :
#         if i % 2 == 0 :
#             sonlar.append(i)
#     return sonlar
# print(juf_chiqar())

# def toq_chiqar():
#     sonlar = []
#     for i in royhat :
#         if i % 2 == 1 :
#             sonlar.append(i)
#     return sonlar
# print(toq_chiqar())

# def musbat_top():
#     musbat = []
#     for i in royhat:
#         if i > 0 :
#             musbat.append(i)
#     return musbat
# print(musbat_top())

# 21
# def manfiy_top(sonlar):
#     manfiy = []
#     for i in sonlar:
#         if i < 0 :
#             manfiy.append(i)
#     return manfiy
# print(manfiy_top([1,2,3,5,6,-7,-5,-6,-12]))

# 22
# def tekror_ochir():
#     soz = int(input('qancha soz kiritmoqchisiz:'))
#     n = []
#     for i in range(1,soz+1):
#         n.append(input('soz:')) 
#     return set(n)
# print(tekror_ochir())

# 23
# def teskari_soz():
#     soz = int(input('soz:'))
#     sozlar = []
#     for i in range(1,soz+1):
#         sozlar.append(input(f'{i} soz:'))
#     return sozlar[::-1]
# print(teskari_soz())

# 24
# def tub_top(a):
#     if a % 3 != 1 and a % 5 != 1 and a % 7 != 1 :
#         print(f'{a} tub son') 
#     else:print(f'{a} tub emas')
# tub_top(17)

# 25
# def tublikini_aniqla(son) :
#     tublar= []
#     murakkablar = []

#     for n in range(2, son + 1 ):
#         tubmi = True
#         for m in range(2, int(n ** 0.5) + 1 ) :
#             if n % m == 0 :
#                 tubmi = False
#                 break
#         if tubmi :
#             tublar.append(n)
#         else:
#             murakkablar.append(n)
        
#     return tublar , murakkablar 

# print(tublikini_aniqla(1999))

# 26
# def ekub_top(a,b):
#     son = []

#     for i in range(1,a+1):
#         if a % i == 0 :
#             son.append(i)

#     sonn = []
#     for m in range(1,b+1):
#         if b % m == 0 :
#             sonn.append(m)
#     if i > m : 
#         for l in range(len(son)) :
#             if sonn == son[l] :
#                 print(l)
#             # print(l)

# print(ekub_top(40,30))


# 30
# def katta_harf():
#     soz = input('soz:').upper()
#     return soz
# print(katta_harf())

# 31
# def kichik_harf():
#     soz = input('soz:').lower()
#     return soz
# print(kichik_harf())




# import math
# def ekub_top(a,b):
#     ekub = math.gcd(a,b)
#     return ekub
# print(ekub_top(30,45))


# def ekub_top(a,b):
#     eng_kichik = min(a,b)
#     ekub = []
#     for i in range(1,eng_kichik+1 ):
#         if a%i == 0 and b % i == 0 :
#             ekub.append(i)
#     ekubi = max(ekub)
#     return ekubi 
# print(ekub_top(20,45))
  
# 34
# def katta_harfqil():
#     soz = input('soz:').title()
#     return soz
# print(katta_harfqil())


# 35
# def yigindi_top():
#     soni = int(input('necha son kiritasiz :'))
#     l = 0

#     for i in range(1 , soni + 1):
#         son = int(input(f'{i}-son:'))
#         l += son    
#     return l 
# print( yigindi_top())

# 36
# def kopaytma_top():
#     soni = int(input('necha son kiritasiz :'))
#     l = 1

#     for i in range(1 , soni + 1):
#         son = int(input(f'{i}-son:'))
#         l *= son    
#     return l 
# print( kopaytma_top())

# 37
# def palidrom_top():
#     son = int(input(':')).strip()
#     sonlar = []
#     sonlar.append(son)
#     if sonlar == sonlar[::-1] :
#         return f'siz kiritgan {sonlar}- son palidrom son'
#     return 'bu son palidrom emas'
# print(palidrom_top())

# 38
# def palidrome_soz_top() :
#     soz = input(':').strip()
#     if soz == soz[::-1]:
#         return f'siz kiritgan {soz} sozi palidrome'
# print(palidrome_soz_top())


# 39
# def soz_sonini_top():
#     soni = len(base_words)
#     return soni
# print(soz_sonini_top())

# 40
# def str_aylantir():
#     soz = ', '.join(base_words)
#     return soz
# print(str_aylantir())

# 41
# def son_tartibla():
#     tartib = sorted(royhat , )
#     return tartib
# print(son_tartibla())

# 42
# def juft_top():
#     son = []
#     for i in range(len(royhat)):
#         if i % 2 == 0 :
#             son.append(i)
#     return son
# print(juft_top())

# 43
# def manfiy_top():
#     n = int(input(':'))
#     son = []
#     for i in range(1,n+1):
#         s = int(input(f'{i}- son'))
#         if s <= 0  :  
#             son.append(s)
#     return son
        
# print(manfiy_top())

# 44
# def kopaytma_top(a,b):
#     s = a**b
#     return s 
# print(kopaytma_top(10, 2))

# 45
# def teskari_soz(matnlar):
#     sozlar = []
#     for i in enumerate(matnlar):
#          sozlar.insert(0,i)
#     return sozlar
# print(teskari_soz(base_words ))



# 46
# def kabisa_top(a):
#     if a % 4 == 0 and a % 100 != 0 or a % 400 == 0 :
#         return f'siz kiritgan {a}- yil kabisa yili'
#     return f'{a}-yil kabisa yili emas'
# print(kabisa_top(2025))
# print(kabisa_top(2024))
# print(kabisa_top(2023))
# print(kabisa_top(2022))
# print(kabisa_top(2021))
# print(kabisa_top(2020))
# print(kabisa_top(2019))


# 47
# def kvadrat_top(a) :
#     s = a**2
#     return s
# print(kvadrat_top(10))


# 48
# def kub_top(a) :
#     s = a**3
#     return s
# print(kub_top(10))

# son = 0
# n = int(input(":"))
# for i in range(1,n+1,1):
#     son += math.factorial(i)
#     # print(math.factorial(i))
# print(son)


      











































































































































































































