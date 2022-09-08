sum_list = []
for n in range(1000):
    if n % 3 == 0 or n % 5 == 0:
        sum_list.append(n)
print(sum(sum_list))
