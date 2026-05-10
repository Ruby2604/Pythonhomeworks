#`txt` nomli string saqlovchi o'zgaruvchi berilgan. `txt`dagi har uchinchi belgidan keyin pastgi chiziqcha
#  (underscore) qo'yilsin. Agar belgi unli harf yoki orqasidan ostki chiziqcha qo'yilgan harf bo'lsa, ostki 
# chiziqcha keyingi harfdan keyin qo'yilsin. Agar belgi satrdagi oxirgi belgi bo'lsa chiziqcha qo'yilmasin.


word = input("Enter a word: ")
result = ""
vowels = "aeiou"
count = 0
for i in range(len(word)):
    result += word[i]
    count += 1
    if count == 3:
        if (i + 1) < len(word):
            vvl = word[i] in vowels
            wwl = word[i + 1] == "_"
            if not vvl and not wwl:
                result += '_'
                count = 0 
            else: 
                count = 2
        else:
            count = 0
print(result)