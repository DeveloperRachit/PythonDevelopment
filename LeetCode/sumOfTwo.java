class Solution {
    public int[] twoSum(int[] nums, int target) {
     
        
        for (int i=0;i<nums;i++)
        {
            for(int j=0; j<nums;j++)
            {
             int temp;
                
            temp =nums[i]+nums[j];
                if(temp==target)
                {
                    return {i,j}
                }
                    
                
            }
            
            
        }
        
        
    }
}