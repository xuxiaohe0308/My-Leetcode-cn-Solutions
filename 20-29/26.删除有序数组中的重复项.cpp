/*
 * @lc app=leetcode.cn id=26 lang=cpp
 *
 * [26] 删除有序数组中的重复项
 */

// @lc code=start
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int len = nums.size(), now, count = 0;
        if (len == 0) return 0;
        // 使用迭代器遍历，方便erase操作
        now = nums[0];
        vector<int>::iterator itr = nums.begin()+1;
        while (itr != nums.end()) {
            if (*itr == now) {
                itr = nums.erase(itr);
                count++;
            } else {
                now = *itr;
                itr++; 
            }
        }
        return len-count;
    }
};
// @lc code=end

// Accepted
// 362/362 cases passed (540 ms)
// Your runtime beats 5.17 % of cpp submissions
// Your memory usage beats 10.39 % of cpp submissions (17.8 MB)
