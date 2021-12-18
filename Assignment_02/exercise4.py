def remove_space(str):
    return str.strip()

def set_list(list):
    return list

print("Convert To Second")    
print("-----------------------------")

Time = input ("Please Enter Your Time (example = 01:20:30) :")
Time = Time.split(":")

result = list(map(remove_space, Time))
print("-----------------------------")
print("second =" ,int(result[0])*3600 + int(result[1])*60 + int(result[2]) )

