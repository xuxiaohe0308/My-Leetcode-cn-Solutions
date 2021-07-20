/*
 * @lc app=leetcode.cn id=215 lang=cpp
 *
 * [215] 数组中的第K个最大元素
 */

// @lc code=start
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<int>> max_k;
        int len = nums.size();
        for (int i = 0; i < len; i++) {
            max_k.push(nums[i]);
            if (max_k.size() > k) max_k.pop();
        }
        return max_k.top();
    }
};
// @lc code=end

