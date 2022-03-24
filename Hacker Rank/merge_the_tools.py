def merge_the_tools(string, k):
    times = int(len(string) / k)
   
    init = 0
    final = k 
    arr = ["s" ] * times
    for i in range(0, times):          
        str_complete = string[init:final]
        str_2 = ""
        for i in str_complete:
            
            if i in str_2:
                pass
            else:
                str_2 += i
            
        init = final
        final = init + k
        print(str_2)
    
        

s = 'AABCAAADA'
k = 3

merge_the_tools(s, k)
    
    

