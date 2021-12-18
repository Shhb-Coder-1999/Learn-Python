import random
results = []
boys = ['ali', 'reza', 'yasin', 'benyamin', 'mehrdad', 'sajjad', 'aidin', 'shahin']
girls = ['sara', 'zari', 'neda', 'homa', 'eli', 'goli', 'mary', 'mina']
random.shuffle(boys)
random.shuffle(girls)
for i in range(0, 8):
    results.append((boys[i] , girls[i]))
print(results)    


