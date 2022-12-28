def solution(number):
    try:
        number = int(number)
    except:
        return 0
    sum = 0
    if number < 1:
        return 0
    for n in range(1, number):
        if n % 3 == 0 or n % 5 == 0:
            sum += n
    return sum
       


x = input('Number:_')
xx = solution(x)
print(f"xx - {xx}")