""" def pow2():
    a = int(input())
    return a**2 

print(pow2())

str1=input()
def OutputStr(str):
    print(str)

OutputStr(str1)


def SumFiveArguments(x, y, z, a = 1, b = 2):
    return x + y + z + a + b

print(SumFiveArguments(1, 2, 3, 4, 5))


def DevideHalf(x):
    return x/2

def Multiplication(y):
    return y*4

z=DevideHalf(int(input()))
print(Multiplication(z)) """

a = input()
def StrToFloat(str):
    try:
        print(float(str))
    except:
        print("this string could not convert to float")

StrToFloat(a)

