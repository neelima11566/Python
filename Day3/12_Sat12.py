# Find the sum of numbers divisible by 5 from 1 to 100
sum = 0
for i in range (1,101):
    if i % 5 == 0:
        sum += i
print(sum)        
        