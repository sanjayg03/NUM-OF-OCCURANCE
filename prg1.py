def find_count(my_list, element):
    count=0
    for i in my_list:
        if i == element:
            count = count + 1
            
    return(count) 
      
input_list= num = [1, 5, 2, 5, 3, 5, 7] 
    
result = find_count(input_list, 5)

print ('Original List :', input_list)
 
print ('Element 5 Occurs %i Times In This List.' %(result))