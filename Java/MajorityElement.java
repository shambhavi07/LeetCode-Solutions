// class Solution {
//     public int majorityElement(int[] nums) {
//         // initialize hashmap
//         HashMap<Integer, Integer> countMap= new HashMap<>();
//         // majority element check
//         int majorityCount = nums.length/2;

//         for (int num: nums){
//             // add or update count for each number
//             countMap.put(num, countMap.getOrDefault(num, 0)+1);

//             // check if count exceeds majorityelement if yes return it
//             if (countMap.get(num) > majorityCount) {
//                 return num;
//             }
//         }
//         return 0;
//     }
// }

// -------------- Boyer Moore Algorithm-------------------

class Solution {
    public int majorityElement(int[] nums) {
        int count =0; // voting tracker for each num
        int res = 0; // result number

        // iterate through nums
        for (int num: nums){
            if (count ==0){
                res= num;
            }
            if (num == res){
                count++;
            } else{
                count--;
            }
        }
        return res;

    }
}
