struct Solution;
use std::collections::HashSet;

impl Solution {
    pub fn three_sum(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
        nums.sort();
        let mut result = Vec::new();
        let mut seen = HashSet::new();
        for i in 0..nums.len()-2{
            let mut l = i + 1;
            let mut r = nums.len() - 1;

            while l < r {
                let curr_sum = nums[i] + nums[r] + nums[l];

                if curr_sum == 0 {
                    let triplet =vec![nums[i], nums[l], nums[r]]; 
                    if seen.insert(triplet.clone()){
                        result.push(triplet);
                    }
                    l += 1;
                    r -= 1;
                } else if curr_sum < 0 {
                    l += 1;
                } else {
                    r -= 1;
                }
            }
        }
        result
    }
}

pub fn run(){
    let nums = vec![-1, 0, 1, 2, -1, -4];
    let result = Solution::three_sum(nums);
    println!("{:?}", result);
    assert_eq!(result, vec![[-1,-1,2],[-1,0,1]]);
}