import csv

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
#Sorting data to get the height of the people
new_data=[]
for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(n_num)

#Getting the mmedian
n = len(new_data)
new_data.sort()

#Floor division is shown by two forward slashes (//) if you didn't know you dumbo:-11
if n % 2 == 0:
    # Getting the first number
    median1 = float(new_data[n//2])
    # Getting the second number
    median2 = float(new_data[n//2 - 1])
    median = (median1+median2)/2
else:
    median = new_data[n//2]
    print(n)
print("Median is: " + str(median))
