def isFactorial(n) :
	i = 1;
	while(True) :
		
		if (n % i == 0) :
			n //= i;
			
		else :
			break;
			
		i += 1;

	if (n == 1) :
		return True;
	
	else :
		return False;


user_number = int(input ("Please Enter Your Number :"))

if (isFactorial(user_number)) :
    print("Yes");

else :
    print("No");

