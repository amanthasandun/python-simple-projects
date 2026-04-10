questions  = ("How many boys in the class : ",
             "How many legs have to dogs : ",
             "what main food in the sri lanka ",
             "why we should learn ",
             "what is the main language in the sri lanka : ",
             )
options = (("A. 12","B. 34","C. 32 ","D. 45","E. 43") , 
           ("A. 4","B. 2 ","C. 6","D. 5 ","E. 2") ,
           ("A. rice","B. watalappan","C. kottu","D. parata","E. those") ,
           ("A. earn","B. handle","C. protect","D. buy","E. funck") ,
           ("A. Urdu ","B. Tamil","C. English","D. Burgar","E. sinhala"))

answers = ("B","A","A","C","E")
guesses = []
score = 0
question_num = 0


for question in questions :
    print("---------------------------------------------------")
    print(question)
    for option in options[question_num] : 
        print (option)
    guess = input("Ehter the answer (A , B , C , D ) : ").upper()
    guesses.append(guess)

    if guess == answers[question_num] :
        score += 1
        print( " Answer is correct ")
    else :
        print("Answer is incorrect")
        print(f"correct answer is {answers[question_num]}")
    question_num += 1


print("-------------------")
print("Results")
for answer in answers : 
    print(answer , end = "")

for guess in guesses : 
    print(guess , end="")

score = int(score/len(questions)*100)
print(f"Your score is the : {score}%")