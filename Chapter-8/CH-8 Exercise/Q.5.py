# def pattern(n):
#     for i in range(0,n):
#         print("*"*(n-i))
# pattern(6)


def pattern(n):
    if n == 0:
        return
    print("*"*n)
    pattern(n-1)
pattern(6)