# First, we will take the input:
# we will take 1 as a lower value
lower_value = int(input("Please, Enter the Lowest Range Value: "))
# we will take 100 as a upper value
upper_value = int(input("Please, Enter the Upper Range Value: "))

print("The Prime Numbers in the range are: ")
for number in range(lower_value, upper_value + 1):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            print(number)
            
