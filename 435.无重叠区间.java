/*
 * @lc app=leetcode.cn id=435 lang=java
 *
 * [435] 无重叠区间
 */

// @lc code=start
import java.util.Arrays;
import java.util.Comparator;
class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        int len = intervals.length;
        int count = 0;
        // 二维数组根据第二列进行排序
        Arrays.sort(intervals, new Comparator<int[]>() {
            @Override
            public int compare(int[] n1, int[] n2) {
                return n1[1] - n2[1];
            }
        });
        int end = intervals[0][0];
        for (int i = 0; i < len; i++) {
            int[] event = intervals[i];
            if (event[0] >= end) {
                count++;
                end = event[1];
            }
        }
        return len-count;
    }
}
// @lc code=end
// Accepted
// 58/58 cases passed (49 ms)
// Your runtime beats 61.44 % of java submissions
// Your memory usage beats 47.15 % of java submissions (94.5 MB)
