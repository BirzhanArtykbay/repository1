def spy_game(nums):
    flag_0 = False
    flag_1 = False
    flag_2 = False

    for num in nums:
        if num == 0 and not flag_0:
            flag_0 = True
        elif num == 0 and flag_0 and not flag_1:
            flag_1 = True
        elif num == 7 and flag_0 and flag_1:
            flag_2 = True
            break 
    
    return flag_0 and flag_1 and flag_2


print(spy_game([1,2,4,0,0,7,5]))  
print(spy_game([1,0,2,4,0,5,7]))  
print(spy_game([1,7,2,0,4,5,0]))  