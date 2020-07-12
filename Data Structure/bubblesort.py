def sort(nums):

    for i in range(len(nums)-1,0,-1): #we substracted 1 from len(nums) because theres no index 6
        for j in range(i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]                

#nums=[5,3,8,6,2,7]
nums=[9,8,7,5,6,1,2,3]
sort(nums)
print(nums)

'''
temp=nums[j]
nums[j]=nums[j+1]
nums[j+1]=temp

'''