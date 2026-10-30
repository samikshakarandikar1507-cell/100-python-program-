answer = int(input("What is 7 * 8? "))

correct_answer = 7 * 8
difference = abs(answer - correct_answer)

print("Your answer:", answer)
print("Correct answer:", correct_answer)
print("Difference:", difference)
check_output("Your answer: 50\nCorrect answer: 56\nDifference: 6", inputs=["50"])
