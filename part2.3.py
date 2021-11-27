import random

def DisplayInstruction():
    print("Answer each addition question. (1 point each)")

def Answer1stQuestion():
    rNum1 = random.randint(0,100)
    rNum2 = random.randint(0,100)
    print(f"\n1. {rNum1} + {rNum2} =", end =" ")
    ans1 = int(input())
    correctAns1 = rNum1 + rNum2
    if ans1 == correctAns1:
        print("Correct!")
        score1 = 1
    else:
        print("Incorrect, Correct Answer:", correctAns1)
        score1 = 0
    return score1

def Answer2ndQuestion():
    rNum1 = random.randint(0,100)
    rNum2 = random.randint(0,100)
    print(f"2. {rNum1} + {rNum2} =", end =" ")
    ans2 = int(input())
    correctAns2 = rNum1 + rNum2
    if ans2 == correctAns2:
        print("Correct!")
        score2 = 1
    else:
        print("Incorrect, Correct Answer:", correctAns2)
        score2 = 0
    return score2

def Answer3rdQuestion():
    rNum1 = random.randint(0,100)
    rNum2 = random.randint(0,100)
    print(f"3. {rNum1} + {rNum2} =", end =" ")
    ans3 = int(input())
    correctAns3 = rNum1 + rNum2
    if ans3 == correctAns3:
        print("Correct!")
        score3 = 1
    else:
        print("Incorrect, Correct Answer:", correctAns3)
        score3 = 0
    return score3

def Answer4thQuestion():
    rNum1 = random.randint(0,100)
    rNum2 = random.randint(0,100)
    print(f"4. {rNum1} + {rNum2} =", end =" ")
    ans4 = int(input())
    correctAns4 = rNum1 + rNum2
    if ans4 == correctAns4:
        print("Correct!")
        score4 = 1
    else:
        print("Incorrect, Correct Answer:", correctAns4)
        score4 = 0
    return score4

def Answer5thQuestion():
    rNum1 = random.randint(0,100)
    rNum2 = random.randint(0,100)
    print(f"5. {rNum1} + {rNum2} =", end =" ")
    ans5 = int(input())
    correctAns5 = rNum1 + rNum2
    if ans5 == correctAns5:
        print("Correct!")
        score5 = 1
    else:
        print("Incorrect, Correct Answer:", correctAns5)
        score5 = 0
    return score5

def Answer6thQuestion():
    rNum1 = random.randint(0,100)
    rNum2 = random.randint(0,100)
    print(f"6. {rNum1} + {rNum2} =", end =" ")
    ans6 = int(input())
    correctAns6 = rNum1 + rNum2
    if ans6 == correctAns6:
        print("Correct!")
        score6 = 1
    else:
        print("Incorrect, Correct Answer:", correctAns6)
        score6 = 0
    return score6

def Answer7thQuestion():
    rNum1 = random.randint(0,100)
    rNum2 = random.randint(0,100)
    print(f"7. {rNum1} + {rNum2} =", end =" ")
    ans7 = int(input())
    correctAns7 = rNum1 + rNum2
    if ans7 == correctAns7:
        print("Correct!")
        score7 = 1
    else:
        print("Incorrect, Correct Answer:", correctAns7)
        score7 = 0
    return score7

def Answer8thQuestion():
    rNum1 = random.randint(0,100)
    rNum2 = random.randint(0,100)
    print(f"8. {rNum1} + {rNum2} =", end =" ")
    ans8 = int(input())
    correctAns8 = rNum1 + rNum2
    if ans8 == correctAns8:
        print("Correct!")
        score8 = 1
    else:
        print("Incorrect, Correct Answer:", correctAns8)
        score8 = 0
    return score8

def Answer9thQuestion():
    rNum1 = random.randint(0,100)
    rNum2 = random.randint(0,100)
    print(f"9. {rNum1} + {rNum2} =", end =" ")
    ans9 = int(input())
    correctAns9 = rNum1 + rNum2
    if ans9 == correctAns9:
        print("Correct!")
        score9 = 1
    else:
        print("Incorrect, Correct Answer:", correctAns9)
        score9 = 0
    return score9

def Answer10thQuestion():
    rNum1 = random.randint(0,100)
    rNum2 = random.randint(0,100)
    print(f"10. {rNum1} + {rNum2} =", end =" ")
    ans10 = int(input())
    correctAns10 = rNum1 + rNum2
    if ans10 == correctAns10:
        print("Correct!")
        score10 = 1
    else:
        print("Incorrect, Correct Answer:", correctAns10)
        score10 = 0
    return score10

def DisplayScore(score1, score2, score3, score4, score5, score6, score7, score8, score9, score10):
    totalScore = score1 + score2 + score3 + score4 + score5 + score6 + score7 + score8 + score9 + score10
    print(f"\nScore: {totalScore}/10")
    
DisplayInstruction()

score1 = Answer1stQuestion()
score2 = Answer2ndQuestion()
score3 = Answer3rdQuestion()
score4 = Answer4thQuestion()
score5 = Answer5thQuestion()
score6 = Answer6thQuestion()
score7 = Answer7thQuestion()
score8 = Answer8thQuestion()
score9 = Answer9thQuestion()
score10 = Answer10thQuestion()

DisplayScore(score1, score2, score3, score4, score5, score6, score7, score8, score9, score10)