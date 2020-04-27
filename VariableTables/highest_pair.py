#################################################################
# Interview Question:
# Given a list of n numbers, find the highest pair of adjacent
# elements. That is, maximize a[i] + a[i+1] for some i.

# Variable Table:

# Variable : Value
# [7, 2, 5, 9, 3, 4]
#
#
#


# Variable table:
# 0.  1. 2. 3    0. 1. 2. 3 
# [1, 2, 3, 4], [1, 2, 7, 4]
# Variable : Value
# i = 2
# len = 4 
# array1 [i] = 3
# array2 [i] = 7
# continue, continue,False- function ends

def find_highest_pair(the_list):
  # Set it to lowest possible number
  highest_pair = float('-inf')
  
  # Loop over all indices in the list
  for i in range(len(the_list)):
    # For each index, see if the pair starting at index is higher
    # than highest we've seen so far
    if the_list[i] + the_list[i+1] > highest_pair:
      highest_pair = the_list[i] + the_list[i+1]
      
  return highest_pair
  

actual = find_highest_pair([7, 2, 5, 9, 3, 4])
expected = 14

print(f"Testing on {[7, 2, 5, 9, 3, 4]}")