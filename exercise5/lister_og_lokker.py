number_list = []
number_sum = 0
for x in range(0,100):
    number_list.append(x)
for e in number_list:
    if e%3==0:
        number_sum+=e
    elif e%10==0:
        number_sum+=e
for e in number_list:
    if e%2==0:
        number_list[e:e+2] = [e+1,e]
print(number_list)
reversed_list=[]
for e in number_list:
    reversed_list.append(number_list[len(number_list)-e-1])
print(reversed_list)