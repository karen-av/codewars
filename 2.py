def filter_list_0(l):
    new_list = []
    for n in l:
        if type(n) is int:
            new_list.append(n)
    return new_list

    
def filter_list(l):
    return [i for i in l if isinstance(i, int)]
       


list_old_0 = [1,2,'a','b']
list_old_1 = [1,'a','b',0,15]
list_old_2 = [1,2,'aasf','1','123',123]

new_list_0 = filter_list(list_old_0)
new_list_1 = filter_list(list_old_1)
new_list_2 = filter_list(list_old_2)
print(new_list_0, new_list_1, new_list_2)
