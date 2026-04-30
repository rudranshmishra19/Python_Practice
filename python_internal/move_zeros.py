# # Two pointer approach
# def moveZeroes(nums):
#     left=0
#     for right in range(len(nums)):
#         if nums[right]!=0:
#             nums[left],nums[right]=nums[right],nums[left]
#             left+=1

# Two pointer approach
def moves_zero(nums):
    left=0
    for right in range(len(nums)):
        if nums[right]!=0:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
    return nums        
nums=[0,1,3,0,12,4]
print(moves_zero(nums))
