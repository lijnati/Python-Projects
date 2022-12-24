getName = input("Enter Your Name: ")
print( getName + ",Welcome to Quizzy!")

playing = input("Do you want play? type 'YES': ")
if playing.lower() != "yes":
    quit()

print("Okay! Let's play:)")
score = 0
print("Here is first question :")

question_one = input("What is the capital city of Egypt? ")
if question_one.lower() == "cairo":
    print("Correct!")
    score += 1
else:
  print("Incorrect! It's: cairo")

question_two = input("What does AI stand for ")
if question_two.lower() == "artificial intelligence":
    print("Correct!")
    score += 1
else:
  print("Incorrect! It's: Artificial Intelligence")

question_three = input("Who is the former president of USA ")
if question_three.lower() == "trump":
    print("Correct!")
    score += 1
elif question_three.lower() == "donald trump":
    print("Correct!")
else:
  print("Incorrect! It's: donald trump")

question_four = input("Who is the CEO of Tesla ")
if question_four.lower() == "elon musk":
    print("Correct!")
    score += 1
elif question_four.lower() == "musk":
        print("Correct!")
else:
  print("Incorrect! It's: elon musk")

question_five = input("Where World Cup 2022 was hosted ")
if question_five.lower() == "qatar":
    print("Correct!")
    score += 1
else:
  print("Incorrect! It's: qatar")

question_six = input("What Planet is closest to the sun ")
if (question_six).lower() == "mercury":
    print("Correct!")
    score += 1
else:
  print("Incorrect! It's: Mercury")

question_seven = input("What country have the largest population ")
if question_seven.lower() == "china":
    print("Correct!")
    score += 1
else:
  print("Incorrect! It's: china")

question_eight = input("What is the capital city of Canada? ")
if question_eight.lower() == "ottawa":
    print("Correct!")
    score += 1
else:
  print("Incorrect! It's: Ottawa")

question_nine = input("What Country never gets dark ")
if question_nine.lower() == "norway":
    print("Correct!")
    score += 1
else:
  print("Incorrect! It's: Norway")

question_ten = input("What country were never colonized in africa ")
if question_ten.lower() == "ethiopia":
    print("Correct!")
    score += 1
else:
  print("Incorrect! It's: Ethiopia")

  #Getting Score
print("You got " +str(score) + " questions correct!")
print("You got " +str((score/10) * 100) + "%.")

if score > 5 :
  print("Good Job!!")

else : 
  print("Not Bad:) Try again")