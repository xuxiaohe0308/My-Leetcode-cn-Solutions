/*
 * @lc app=leetcode.cn id=22 lang=java
 *
 * [22] 括号生成
 */

// @lc code=start
import java.util.ArrayList;
class Solution {
    public List<String> generateParenthesis(int n) {
        ArrayList<String> ret = new ArrayList<String>();
        backtrack(n, 0, 0, "", ret);
        return ret;
    }

    public void backtrack(int n, int n_left, int n_right, String s, ArrayList<String> ret) {
        if (n == n_left && n == n_right) {
            ret.add(s);
            return;
        }

        if (n_left < n) backtrack(n, n_left+1, n_right, s+"(", ret);
        if (n_right < n_left) backtrack(n, n_left, n_right+1, s+")", ret);
    }
}

// @lc code=end

// Accepted
// 8/8 cases passed (1 ms)
// Your runtime beats 74.12 % of java submissions
// Your memory usage beats 98.08 % of java submissions (38 MB)