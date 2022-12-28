def get_count_0(sentance):
    count = 0
    words = 'aeiou'
    for i in sentance:
        if i in words:
            count += 1
    return count

def get_count(sentance):
    return sum(1 for i in sentance if i in 'aeiou')
    

count = get_count('fffff')
print(count)