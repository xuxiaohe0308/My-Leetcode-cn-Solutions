/*
 * @lc app=leetcode.cn id=202 lang=java
 *
 * [202] 快乐数
 */

// @lc code=start
import java.util.HashSet;

class Solution {
    public boolean isHappy(int n) {
        if (n == 1) return true;
        HashSet<String> s = new HashSet<String>();
        String num = Integer.toString(n);

        while (true) {
            if (s.contains(num)) return false;
            else {
                s.add(num);
                num = re(num);
                if (num.equals("1")) return true;
            }
        }
    }

    public String re(String num) {
        int sum = 0;
        for (int i = 0; i < num.length(); i++) {
            char item = num.charAt(i);
            sum += (Math.pow(Character.getNumericValue(item), 2));
        }
        return Integer.toString(sum);
    }
}
// @lc code=end

// Accepted
// 402/402 cases passed (2 ms)
// Your runtime beats 13.01 % of java submissions
// Your memory usage beats 5.73 % of java submissions (35.9 MB)