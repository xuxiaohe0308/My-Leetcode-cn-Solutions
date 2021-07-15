/*
 * @lc app=leetcode.cn id=15 lang=cpp
 *
 * [15] 三数之和
 */

// @lc code=start
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int len = nums.size();
        vector<vector<int>> result;
        // nums = quickSort(nums);  // 快排
        sort(nums.begin(), nums.end());
        int n, temp, count;
        // 去重，0剩3，其余剩2
        /*
        for (int i = 0; i < len; i++) {
            n = nums[i];
            if (n == temp) {
                count++;
                if ((count > 1 && n != 0) || (count > 2 && n == 0) ){
                    nums.erase(nums.begin()+i);
                    i--;
                    len--;
                }
            } else {
                count = 0;
                temp = n;
            }
        }
        */
        // 两层循环
        int i, j, k, ni;
        i = 0;
        while(i < len) {
            j = i + 1;
            k = len - 1;
            while (j < k) {
                temp = nums[i] + nums[j] + nums[k];
                if (temp == 0) {
                    vector<int> r = {nums[i], nums[j], nums[k]};
                    result.push_back(r);
                    n = nums[j];
                    do {
                        j++;
                    } while(j < k && nums[j] == n);
                } else if (temp < 0) {
                    n = nums[j];
                    do {
                        j++;
                    } while(j < k && nums[j] == n);
                } else {
                    n = nums[k];
                    do {
                        k--;
                    } while(j < k && nums[k] == n);
                }
            }
            ni = nums[i];
            do {
                i++;
            } while (i < len && nums[i] == ni);
        }

        return result;
    }
    
    // 快速排序，从小到大
    vector<int> quickSort(vector<int> nums) {
        int len = nums.size();
        if (len <= 1) return nums;
        // 分为左右两部分
        vector<int> left, right;
        int base = nums[0];  // 基准
        for (int i = 1; i < len; i++) {
            if (nums[i] < base) left.push_back(nums[i]);
            else right.push_back(nums[i]);
        }
        // 递归排序
        left = quickSort(left);
        right = quickSort(right);
        // 返回
        left.push_back(base);
        left.insert(left.end(), right.begin(), right.end());
        return left;
    } 
};

// @lc code=end

