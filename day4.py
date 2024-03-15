'''
i = 20
while i < 31:
     if i==27:
        continue
     print(i)
     i=i+1
'''
'''
i = 20
while 1<31:
    if i==27:
      i+=1
    print(i)
    break
'''
'''
i = 20
while 1<31:
    if i==27:
        print(i)
        break
    i+=1
'''
'''
num1 = 12
num2 = 22

total_sum = num1 + num2

print("The sum of", num1, "and", num2, "is:", total_sum)
'''
'''
start_num = 20
end_num = 25
total = 0
count = 0

current_num = start_num
while current_num <= end_num:
    total += current_num
    count += 1
    current_num += 1

average = total / count

print("The average of numbers between", start_num, "and", end_num, "is:", average)
'''
i = 20
sum=0
count =0
while i<= 30:
     sum= sum+1
     count+=1
     i+=1
print(sum/count)
