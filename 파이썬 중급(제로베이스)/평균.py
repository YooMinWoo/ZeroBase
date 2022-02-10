# import random

# nums = random.sample(range(0,100),10)
# print(f"nums : {nums}")

# total = 0
# for n in nums:
#     total += n

# average = total / len(nums)
# print(f"average : {average}")


# import random
# nums = nums = random.sample(range(0,100),30)
# print(f"nums : {nums}")

# total = 0
# targetNums = []
# for n in nums:
#     if n >= 50 and n <= 90:
#         total += n
#         targetNums.append(n)

# average = total / len(targetNums)
# print(f"average : {round(average, 2)}")


# nums = [4, 5.12, 0, 5, 7.34, 9.1, 9, 3, 3.159, 1, 11, 12.789]
# print(f"{nums}")

# targetNums = []
# total = 0
# for n in nums:
#     if n - int(n) == 0: # 실수면 if n - int(n) != 0
#         total += n
#         targetNums.append(n)

# average = total / len(targetNums)
# print(f"average : {round(average, 2)}")



############실습################
import near
scores = [8.9, 7.6, 8.2, 9.2, 8.8, 8.1, 7.9, 9.4, 7.2, 8.7]
top5PlayerScores = [9.12, 8.95, 8.12, 7.90, 7.88]
print(f"top5PlayerScores : {top5PlayerScores}")

total = 0; average = 0
for n in scores:
    total += n

average = round(total / len(scores), 2)

print(f"total : {total}")
print(f"average : {average}")

tp = near.Top5Players(top5PlayerScores, average)
tp.setAlignScore()
top5PlayerScores = tp.getFinalTop5Scores()
print(f"top5PlayerScores : {top5PlayerScores}")