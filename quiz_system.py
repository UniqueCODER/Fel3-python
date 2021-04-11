print("Quiz system \n")


def quiz_system(quiz, correct):
    print(quiz)
    answer = input("Choice :")
    score = 0
    if answer.upper() == correct:
        score += 1
        print("correct")
    else:
        print("wrong")
    return score


question = ["Question 1: 87+9 \n [A] 90\t [B]96\n[C] 100\t[D]-90",
            "Question 2: 35-45 \n [A] 10\t [B]80\n[C] -10\t [D] 0",
            "Question 3: 49/7 \n [A] 7\t [B]8\n C] 9\t [D]10"]

a = quiz_system(question[0], "B") + quiz_system(question[1], "C") + quiz_system(question[2], "A")
print("Score", a, "out of", len(question))
