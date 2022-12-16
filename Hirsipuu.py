import random
fil = open("kotus_sanat.txt")
raw = fil.readlines()
fil.close()
words =[]
for word in raw:
    words.append(word[:-1])
pit = len(words)-1
x = random.randint(0, pit)
word = words[x]
hp = 5
arv = 0
letters = ""
right = []
lenght = len(word)
j = 0
while lenght > 0:
    right.append("-")
    lenght -=1
while hp != 0:
    lenght2 = len(word)-1
    h = 0
    print(f"Arvauksia jäljellä {hp}")
    print(right)
    print(" ")
    quess =input("Arvaa kirjain ")
    if quess in right:
        print(" ")
        print(f"olet jo arvannut {quess}")
        print(" ")
    else:
        letters += quess + " "
    print(f"arvatut kirjaimet: {letters}")
    if quess in word:
        print("arvaamsi kirjain on sanassa")
        while h != len(word):
            if word[h]==quess:
                right[h] = quess
                h += 1
            elif word[h]!=quess:
                h += 1
    else:
        print("arvaamasi kirjain ei ole sanassa")
        hp -=1
    if "-" not in right:
        j = 1
        break
    h = 0
    arv += 1
if j == 1:
    print(f"Hi Hi Hiii! arvasit sanan {word}")
    print(f"Arvauksia kokonaisuudessaan {arv}")
else:
    print("hävisit pelin")
    print(f"Oikea sana oli {word}")
    print(f"Arvauksia kokonaisuudessaan {arv}")