import random
import time

#function to generate random numbers
def generate_random_numbers(start, end, count):
    numbers = list(range(start, end+1))              #storing numbers in list
    random.shuffle(numbers)
    return numbers[:count]

start_number = 1
end_number = 100
count = 50

random_numbers = generate_random_numbers(start_number, end_number, count)
print(random_numbers)

#to search an element

key=int(input("Enter an element to search :"))

start_time = time.time()

for index, element in enumerate(random_numbers):
        if element == key:                            #compares each element with key (linear search)
            found=bool(True)
            break 
         

if found==True:
    print(f"The element {key} is present in {index} index")
else:
     print("{key} not found ") 

end_time = time.time()

execution_time = end_time - start_time

print(f"Execution time: {execution_time} seconds")

