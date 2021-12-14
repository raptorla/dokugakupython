""" a = ["ウォーキング・デッド", "アントラージュ", "ザ・ソプラノズ", "ヴァンパイア・ダイアリーズ"]
for index, i in enumerate(a) :
    print(i,index)
    

for i in range(25, 51):
    print(i) 

number = [1,2,3,4,5,6,7,8]
while True:
    a=input("Guess a number or type q to quit.")
    if "q" == a:
        break
    try:
        a = int(a)
    except ValueError:
        print("input type number or q to quit.")
    if a in number:
        print("ok")
    else:
        print("not ok")
""" 

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = []

for i in list1:
    for j in list2:
        list3.append(i * j)
print(list3)
