
#this code was automaticlly generated by chatGPT and it is buggy

def fibonacci(n):
    if n <= 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        sequence = fibonacci(n-1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence

result = fibonacci(5)
print(result)