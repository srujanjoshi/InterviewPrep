def merge_lists(list_a, list_b):
    a_index=0
    b_index=0
    new_list=[]
    while(a_index<len(list_a) and b_index<len(list_b)):
        if(list_a[a_index]<list_b[b_index]):
            new_list.append(list_a[a_index])
            a_index+=1
        else:
            new_list.append(list_b[b_index])
            b_index+=1
    if(a_index==len(list_a)):
        new_list.extend(list_b[b_index:])
    else:
        new_list.extend(list_a[a_index:])
    return new_list

