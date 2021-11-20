
def findPair(nums, target):
 
  
    for i in range(len(nums) - 1):
 
        
        for j in range(i + 1, len(nums)):
 

            if nums[i] + nums[j] == target:
                print('Pair found', (nums[i], nums[j]))
                return
 
    print('Pair not found')
 
 
if __name__ == '__main__':
 
    nums = [8, 7, 2, 5, 3, 1]
    target = 10
 
    findPair(nums, target)