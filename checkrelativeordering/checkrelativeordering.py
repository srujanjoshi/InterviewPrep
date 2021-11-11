def checkrelativeordering(list_a, list_b, combined_list): 
    list_a_index=0
    list_b_index=0
    combined_list_index=0
    while(combined_list_index<len(combined_list)):
        if(list_a_index <len(list_a)):
            if(list_a[list_a_index]==combined_list[combined_list_index]):
                list_a_index+=1
                combined_list_index+=1
                continue
        if(list_b_index<len(list_b)):
            if(list_b[list_b_index]==combined_list[combined_list_index]):
                list_b_index+=1
                combined_list_index+=1
                continue
        return False
    return True 

print(checkrelativeordering([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8]))
    