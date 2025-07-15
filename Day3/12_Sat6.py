# Count how many numbers between 1 and 100 are divisible by 3
count = 0
for i in range (1,101):
     if i % 3 == 0:
      count += 1

print("Count of numbers divisible by 3:", count)
         