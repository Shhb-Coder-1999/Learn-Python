def Pascal_triangle (row):
 list = [[1]] 
 if row == 1:
        return list  
 elif row == 2:
        list.append([1,1]) 
        return list 
 else:
    list.append([1,1])         
    for i in range(1, row):
      temp_list = []
      for j in range(0,len(list)-1):
        if j+1 < len(list):     
            sum = list[i][j] + list[i][j+1]
            temp_list.append(sum)
      temp_list.insert(0, 1) 
      temp_list.append(1) 
      list.append(temp_list)         
    return list

x = int(input("Enter number of rows : "))
result = Pascal_triangle(x-1)
for i in range(0, len(result)):
    print(result[i])


    

