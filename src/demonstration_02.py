"""
Demonstration #2

Given a non-empty array of integers `nums`, every element appears twice except except for one. Write a function that finds the element that only appears once.

Examples:

- single_number([3,3,2]) -> 2
- single_number([5,2,3,2,3]) -> 5
- single_number([10]) -> 10
"""
def single_number(nums):
    
    seen_numbers_dict = {}
    # Your code here
    
    # UPER
    # search for the only unique number
    # is a number unique?
    # use count function
    # loop over each items and compare it to the first one to see if it repeats
    
            # TIME COMPLEXITY IS O(N) * 0(N) = O(N**2)
            # for data in nums:
            #     if nums.count(data) == 1:
            #         return data
        
    # NOW TRY TO REDUCE TIME COMPLEXITY
    for data in nums:
        if data in seen_numbers_dict:
            seen_numbers_dict[data] += 1
            
        else:
            # Otherwise if first time seeing the number
            seen_numbers_dict[data] = 1
            
    print(seen_numbers_dict)
    # find the number thats only seen once
    for key, value in seen_numbers_dict.items():
        if value == 1:
            return key
        


print(single_number([3,3,2]))
print(single_number([5,2,3,2,3]))
print(single_number([10]))
