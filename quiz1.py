print("Welcome to quiz ")

playing = input("DO you want to play? ")

if playing.lower() != "yes":
    quit()

print("okay ! lets play:) ")

score = 0 

answer = input("what does CPU stans for ? ")     # 1st question #
if answer.lower() == "central processing unit": 
    print("Sahi Jawab")
    score += 1 
else:
    print("Galat jawab <<< sahi dhundho..........")

answer = input("who own instagram ? ")     # 2nd question #
if answer.lower() == "meta": 
    print("Sahi Jawab")
    score += 1
else:
    print("Galat jawab <<< sahi dhundho..........")

answer = input("best processor ? ")     # 3rd question #
if answer.lower() == "ryzen": 
    print("Sahi Jawab")
    score += 1
else:
    print("Galat jawab <<< sahi dhundho..........")

answer = input("language which is easy to learn & understand ? ")     # 4th question #
if answer.lower() == "python": 
    print("Sahi Jawab")
    score += 1
else:
    print("Galat jawab <<< sahi dhundho..........")

'''answer = input("Harst languag to learn & understand ? ")     # 5th question #
if answer.lower() == "java":
    print("Sahi Jawab")
    score += 1
else:
    print("Galat jawab <<< sahi dhundho..........")'''

print("You got the " + str(score) + "questions correct ! ")
print("You got the " + str((score /4)* 100) + " %")     #kbhi 5th question ad krna rhaa to ye ad krk multiply by 5 kreneka #

