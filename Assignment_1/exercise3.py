def find_longest_brim(brim1 , brim2 , brim3):
    if   brim1 >= brim2 and brim1 >= brim3 :
         brims = [brim1, brim2, brim3]
         return brims

    elif brim2 >= brim1 and brim2 >= brim3 : 
         brims = [brim2, brim1, brim3]
         return brims
        
    elif brim3 >= brim1 and brim3 >= brim2 : 
         brims = [brim3, brim2, brim1]
         return brims



brim1 = float(input ("please enter lenghtg of first brim of triangle :"))
brim2 = float(input ("please enter lenghtg of second brim of triangle :"))
brim3 = float(input ("please enter lenghtg of third brim of triangle :"))

brims = find_longest_brim(brim1 , brim2 , brim3)


if   brims[0] >= brims[1] + brims[2]  :
    print("Cannot make a triangle !!")
       
else : 
     print("Can make a triangle :)")
        
        





  