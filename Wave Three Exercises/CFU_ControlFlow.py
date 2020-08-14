#Question: What type of loop should we use?
#You need to write a loop that takes the numbers in a given list named num_list:
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

#Your code should add up the odd numbers in the list, but only up to the first 5 odd numbers together. If there are more than 5 odd numbers, you should stop at the fifth. If there are fewer than 5 odd numbers, add all of the odd numbers.
odd_numbers = 0
sum_of_odd_numbers = 0
num_list_len = len(num_list)
i = 0
#Would you use a while or a for loop to write this code?
# while loop would be much more efficient as we do not need a break statement because we do not want to iterate over the whole list of numbers
while (odd_numbers < 5) and (num_list_len > i):
    if num_list[i] % 2 != 0:
        sum_of_odd_numbers += num_list[i]
        odd_numbers += 1
    i += 1
## Please use this space to test and run your code
print('There are {} odd numbers in the list '.format(odd_numbers))
print('Sum of odd numbers is: {}'.format(sum_of_odd_numbers))