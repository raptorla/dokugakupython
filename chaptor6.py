""" str = "カミュ"

for i in range(len(str)):
        print(str[i])

str1 = input()
str2 = input()

strsum = "I wrote " + str1 + " yesterday and sent to " + str2
print(strsum) 

print("aldous Huxley was born in 1894.".capitalize())

print("Where? Who? When?".split(" "))

words = ["The", "fox", "jumped", "over", "the", "fence", "."]
print(" ".join(words))

words = "A screaming comes across the sky."
words = words.replace("s", "$")
print(words)

words = "Hemingway"
print(words.index("m"))

print("three "*3)
"""

words = "A screaming, comes across the sky."

print(words[:11])