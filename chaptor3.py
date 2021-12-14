age = float(input())

if age >= 25 :
    print("age>=25")

elif age >= 10 and age < 25:
    print("age < 25 and age >= 10")

else:
    print("age<10")

b = float(input())
c = float(input())

extra = b%c
quotient = b//c

print(extra)

print(quotient)