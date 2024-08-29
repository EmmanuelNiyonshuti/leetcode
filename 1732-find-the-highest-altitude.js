#!/usr/bin/env node

/**
 * @param {number[]} nums
 * @return {number}
 */
const pivotIndex = function(nums) {
    total_sum = 0;
    left_sum = 0;
    nums.forEach(num => total_sum += num);
    for(let i = 0; i < nums.length; i++){
        let num = nums[i]
        right_sum = total_sum - left_sum - num;
        if (right_sum === left_sum) return i;
        left_sum += num;
    }
    return -1;
}

// const nums = [1,7,3,6,5,6];
const nums = [1,2,3];
// const nums = [2,1,-1];
const p = pivotIndex(nums)
console.log(p);
