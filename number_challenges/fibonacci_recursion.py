def fibonacci_recur(num):

    if num <= 1:
        return num
    else:
        return fibonacci_recur(num-1) + fibonacci_recur(num-2)


num = 0

print(f"{fibonacci_recur(num)}")