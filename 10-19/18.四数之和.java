/*
 * @lc app=leetcode.cn id=18 lang=java
 *
 * [18] 四数之和
 */

// @lc code=start
import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> ret = new ArrayList<>();
        Arrays.sort(nums);
        int l = nums.length;
        if (l < 4) return ret;
        int p1, p2, p3, p4;
        for (p1 = 0; p1 < l-3; ) {
            for (p2 = p1 + 1; p2 < l-2; ) {
                int t = target - nums[p1] - nums[p2];
                for (p3 = p2 + 1, p4 = l-1; p3 < p4; ) {
                    int tmp = nums[p3] + nums[p4];
                    if (tmp > t) {
                        int n4 = nums[p4];
                        do {
                            p4--;
                        }while (p4 > p3 && nums[p4] == n4);
                    }
                    else if (tmp < t) {
                        int n3 = nums[p3];
                        do {
                            p3++;
                        }while (p3 < p4 && nums[p3] == n3);
                    }
                    else {
                        int n4 = nums[p4];
                        List<Integer> result = new ArrayList<>();
                        result.add(nums[p1]); result.add(nums[p2]); 
                        result.add(nums[p3]); result.add(nums[p4]); 
                        ret.add(result);
                        do {
                            p4--;
                        }while (p4 > p3 && nums[p4] == n4);
                        int n3 = nums[p3];
                        do {
                            p3++;
                        }while (p3 < p4 && nums[p3] == n3);
                    }
                }
                int n2 = nums[p2];
                do {
                    p2++;
                }while (p2 < l-2 && nums[p2] == n2);
            }
            int n1 = nums[p1];
            do {
                p1++;
            }while (p1 < l-3 && nums[p1] == n1);
        }
        return ret;
    }
}
// @lc code=end

// Accepted
// 286/286 cases passed (20 ms)
// Your runtime beats 28.2 % of java submissions
// Your memory usage beats 54.94 % of java submissions (38.7 MB)