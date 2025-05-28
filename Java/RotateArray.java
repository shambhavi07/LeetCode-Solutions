class Solution {
    // trying the simple way by ca;culating index
    public void rotate(int[] nums, int k){
        int n= nums.length;
        int[] rotated =  new int[n];
        k = k%n; // in case k exceed nums length

        for(int i=0; i<n; i++){
            int newIndex = (i+k)%n;
            rotated[newIndex]= nums[i];

        }
        for (int i=0; i<n;i++){
            nums[i]= rotated[i];
        }
    }
        
    }
