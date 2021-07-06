/*
 * @lc app=leetcode.cn id=11 lang=cpp
 *
 * [11] 盛最多水的容器
 */

// @lc code=start
class Solution {
public:
    int maxArea(vector<int>& height) {
        int len = height.size();
        int i = 0, j = len-1;
        int max = 0;
        int temp, left, right;
        while(1){
            if(i == j) break;
            left = height[i];
            right = height[j];
            // 计算容积并缩减两端距离
            if(left < right){
                temp = left * (j-i);
                i++;
            }
            else{
                temp = right * (j-i);
                j--;
            }
            if(temp > max) max = temp;
        }

        return max;
    }
};
// @lc code=end
