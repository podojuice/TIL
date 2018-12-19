# 1. 평균을 구하시오



my_score = [79, 84, 66, 93]

my_average = sum(my_score, 0.0)/len(my_score) #이거 타입은 float여야함.

print(my_average)


your_score ={
    '수학':87,
    '국어':83,
    '영어':76,
    '도덕':100
}
# your_average #얘 역시 float 클래스여야.

your_average = sum(your_score.values())/len(your_score)

print(your_average)
