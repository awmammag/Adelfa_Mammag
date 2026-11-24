#ANGEL GRACE MAMMAG
#8-ADELFA
#11/24/26

scores = []

for i in range(5):
    scores.append(int(input(f"Enter quiz {i+1} Score: ")))

total = sum(scores)
average = total/len(scores)

print("=====QUIZ SCORE REPORT=====")
print(f"Quiz Scores: {scores}")
print(f"Number of quizzes: {len(scores)}")
print(f"Total score: {total}")
print(f"Average score: {average:.2f}")
print(f"Lowest score: {min(scores)}")
print(f"Highest score: {max(scores)}")

scores.sort()
print(f"Ascending scores: {scores}")

scores.reverse()
print(f"Descending scores: {scores}")
print(f"Original scores: {scores}")