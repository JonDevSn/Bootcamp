# For Fixed Window Size

# window = sum(nums[:k])
# answer = window

# for right in range(k, len(nums)):

#     # add new element
#     window += nums[right]

#     # remove old element
#     window -= nums[right - k]

#     # update answer
#     answer = max(answer, window) 







# For Variable Window Size

# left = 0
# window = 0
# answer = 0

# for right in range(len(nums)):

#     # Add nums[right]
#     window += nums[right]

#     # Shrink while invalid
#     while window > k:
#         window -= nums[left]
#         left += 1

#     # Window is valid
#     answer = max(answer, right - left + 1)



