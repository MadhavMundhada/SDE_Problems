"""
def next_permutation(L):
    '''
    Permute the list L in-place to generate the next lexicographic permutation.
    Return True if such a permutation exists, else return False.
    '''
     
    n = len(L)
 
    #------------------------------------------------------------
 
    # Step 1: find rightmost position i such that L[i] < L[i+1]
    i = n - 2
    while i >= 0 and L[i] >= L[i+1]:
        print(i,L[i],L[i+1])
        i -= 1
      
     
    if i == -1:
        return False
 
    #------------------------------------------------------------
 
    # Step 2: find rightmost position j to the right of i such that L[j] > L[i]
    j = i + 1
    while j < n and L[j] > L[i]:
        print(j)
        j += 1
    j -= 1
     
    #------------------------------------------------------------
 
    # Step 3: swap L[i] and L[j]
    L[i], L[j] = L[j], L[i]
     
    #------------------------------------------------------------
 
    # Step 4: reverse everything to the right of i
    left = i + 1
    right = n - 1
 
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1
             
    print(L) 

def example():
    L = list(map(int,input().split()))
 
    next_permutation(L)
 
 
#----------------------------------------------------------------
 
if __name__ == "__main__":
    example()

"""


"""
class Solution(object):
   def nextPermutation(self, nums):
      found = False
      i = len(nums)-2
      while i >=0:
         if nums[i] < nums[i+1]:
            found =True
            break
         i-=1
      if not found:
         nums.sort()
      else:
         m = self.findMaxIndex(i+1,nums,nums[i])
         nums[i],nums[m] = nums[m],nums[i]
         nums[i+1:] = nums[i+1:][::-1]
      return nums
   def findMaxIndex(self,index,a,curr):
      ans = -1
      index = 0
      for i in range(index,len(a)):
         if a[i]>curr:
            if ans == -1:
               ans = curr
               index = i
            else:
               ans = min(ans,a[i])
               index = i
      return index
ob1 = Solution()
m=list(map(int,input().split()))
print(ob1.nextPermutation(m))

"""
def sol(nums):
        n=len(nums)
        found = False
        i = len(nums)-2
        while i >=0:
            
            
            
            if nums[i] < nums[i+1]:
                found =True
                print(i,"braek")
                break
            i-=1
        if not found:          #jab koi breakpoint hi na ho jaise 3 2 1
            nums.sort()
            return nums
        else: 
            j=i+1
            print(i,j)
            while j<n and nums[j]>nums[i]:
                j+=1
            j-=1

            #Swap
            nums[i],nums[j]=nums[j],nums[i]

            #rightmost change
            nums[i+1:] = nums[i+1:][::-1]

            
        return nums

m=list(map(int,input().split()))
print(sol(m))