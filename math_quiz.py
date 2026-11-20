# Math Quiz Program
# Developed for practice and learning

print("==================================")
print("        MATH QUIZ")
print("==================================")
print("Instructions:")
print("1. There are 5 questions.")
print("2. Enter your answer and press Enter.")
print("3. Each correct answer = 10 Marks")
print("==================================\n")

name = input("Enter Your Name: ")
print(f"\nWelcome, {name}! Let's begin.\n")

score = 0

# Question 1
print("Question 1: What is 12 + 18 ?")
ans1 = int(input("Your Answer: "))
if ans1 == 30:
    print("Correct!\n")
    score += 10
else:
    print("Incorrect. Correct Answer is 30.\n")

# Question 2
print("Question 2: What is 25 - 9 ?")
ans2 = int(input("Your Answer: "))
if ans2 == 16:
    print("Correct!\n")
    score += 10
else:
    print("Incorrect. Correct Answer is 16.\n")

# Question 3
print("Question 3: What is 7 * 8 ?")
ans3 = int(input("Your Answer: "))
if ans3 == 56:
    print("Correct!\n")
    score += 10
else:
    print("Incorrect. Correct Answer is 56.\n")

# Question 4
print("Question 4: What is 100 / 4 ?")
ans4 = int(input("Your Answer: "))
if ans4 == 25:
    print("Correct!\n")
    score += 10
else:
    print("Incorrect. Correct Answer is 25.\n")

# Question 5
print("Question 5: What is 15 + 15 + 10 ?")
ans5 = int(input("Your Answer: "))
if ans5 == 40:
    print("Correct!\n")
    score += 10
else:
    print("Incorrect. Correct Answer is 40.\n")

# Final Result
print("==================================")
print("          RESULT")
print("==================================")
print(f"Name: {name}")
print(f"Total Score: {score} / 50")

if score == 50:
    print("Remarks: Excellent! Outstanding Performance.")
elif score >= 30:
    print("Remarks: Very Good! Keep Practicing.")
else:
    print("Remarks: Good Attempt. Practice More.")
print("==================================")
