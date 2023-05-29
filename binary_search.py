import random
import time

#function to generate random numbers
def generate_random_numbers(start, end, count):
    numbers = list(range(start, end+1))              #storing numbers in list
    random.shuffle(numbers)
    return numbers[:count]

start_number = 1
end_number = 10
count = 5

random_numbers = generate_random_numbers(start_number, end_number, count)
random_numbers.sort()
print(random_numbers)

#to search an element
key=int(input("Enter an element to search :"))

start_time = time.time()

low = 0
high = len(random_numbers) - 1
found=bool(False)

while low <= high:                 #to search element (binary search)
    mid = (low + high) // 2
    if random_numbers[mid] == key:
        found=bool(True)
        break
    elif random_numbers[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

if found==True :
    print(f"{key} element is present in {mid}")
else:
    print("element not present")

end_time = time.time()

execution_time = end_time - start_time

print(f"Execution time: {execution_time} seconds")