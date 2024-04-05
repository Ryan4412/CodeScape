time: list = [[1, 0],[2, 720]]
count = 2
for i in range(2, 99):
    time.append([i+1, 720*i + time[i-1][1]])
    count += 1
print(count)

for x in time:
    print(str(x[0]) + ": " + str(x[1]) + ", ")

sum: int = 0
for i in range (1, 100):
    sum += i
    # print(i)
print(sum)