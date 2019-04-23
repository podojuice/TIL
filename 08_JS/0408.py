# def my(arg1, arg2):
#     return arg1

# 위에 있는 함수 이렇게도 나타낼 수 있다. my = lambda arg, arg2: arg

# def arg():
#     return "i'm function"
#
# print(my(arg)())

def fco():
    return lambda n: n + 1

num_100 = 100

num_101 = fco()

print(num_101(num_100))