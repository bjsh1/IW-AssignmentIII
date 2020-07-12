def binary_search(search):
    nums=[3,5,8,10,12,16,25,45,90,120,190]
    
    l=0
    u=len(nums)-1
    

    while l<=u:
        mid=(l+u)//2 #it will give the int values, without the float

        if nums[mid]==search:
            print("{} found at {}th index which is {} position ".format(search,mid,(mid+1)))
            break
        else:                    
            if nums[mid]>search:
                u=mid-1
                    
            elif nums[mid]<search:
                l=mid+1
    
    if search not in nums:
        print("Not found") 
        

binary_search(1)
#print(binary_search(25))

