import random
from timeit import default_timer as timer

#function to generate random numbers
def generate_random_numbers(start, end, count):
    numbers = list(range(start, end+1))              #inserting numbers in list
    random.shuffle(numbers)     #shuffle
    return numbers[:count]

start_number = 1
end_number = 1000050
count = 1000000

random_numbers = generate_random_numbers(start_number, end_number, count)
random_numbers.sort()     #sorting numbers                    
print(random_numbers)

#to search an element

#linear search
key=int(input("Enter an element to search :"))

start_time = timer()
for index, element in enumerate(random_numbers):
        if element == key:                            #compares each element with key (linear search)
            found=bool(True)
            break 
end_time = timer()        

#binary search
start_time1 = timer()

low = 0
high = len(random_numbers) - 1
flag=bool(False)

while low <= high:                 #to search element (binary search)
    mid = (low + high) // 2
    if random_numbers[mid] == key:
        flag=bool(True)
        break
    elif random_numbers[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

end_time1 = timer()


if found==True:
    print(f"The element {key} is present in {index} index")
else:
    print(f"{key} not found ") 


if flag==True :
    print(f"the element {key} is present in {mid} index")
else:
    print("element not present")

#time for linear search
execution_time =(end_time - start_time)

print(f"Execution time for linear search : {execution_time*10**3:.03f} ms")

#time for binary search
execution_time1 =(end_time1 - start_time1)

print(f"Execution time for binary search : {execution_time1*10**3:.03f} ms")

