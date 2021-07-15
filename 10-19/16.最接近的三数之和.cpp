/*
 * @lc app=leetcode.cn id=16 lang=cpp
 *
 * [16] 最接近的三数之和
 */

// @lc code=start
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int len = nums.size();
        // 排序
        sort(nums.begin(), nums.end());
        // 初始化
        int dist, temp;
        int min_dist, result, result_temp;
        result = nums[0] + nums[1] + nums[len-1];
        min_dist = target - result;
        if (dist == 0) return target;
        min_dist = min_dist > 0 ? min_dist : 0-min_dist;
        int i = 0, j = 1, k = len - 1;
        while (i < len) {
            j = i + 1;
            k = len-1;
            while (j < k) {
                result_temp = nums[i] + nums[j] + nums[k];
                dist = target - result_temp;
                if (dist == 0) return target;
                else if(dist > 0) {
                    if (dist < min_dist) {
                        min_dist = dist;
                        result = result_temp;
                    }
                    temp = nums[j];
                    do {j++;} while(j < k && nums[j] == temp);
                } else {
                    if ((0-dist) < min_dist) {
                        min_dist = 0-dist;
                        result = result_temp;
                    }
                    temp = nums[k];
                    do {k--;} while(j < k && nums[k] == temp);
                }
            }
            temp = nums[i];
            do {i++;} while(i < len && nums[i] == temp);
        }
        return result;
    }
};
// @lc code=end

