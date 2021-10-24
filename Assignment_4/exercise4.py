def fibonacci_of(n):
        if n in {0, 1}:
          return n
        return fibonacci_of(n - 1) + fibonacci_of(n - 2) 


user_num = int(input ("Please Enter Your Number:"))
fibo_list = [fibonacci_of(n) for n in range(user_num)]
print(fibo_list)