/*
 * @lc app=leetcode.cn id=10 lang=cpp
 *
 * [10] 正则表达式匹配
 */

// @lc code=start
class Solution {
public:
    bool isMatch(string s, string p) {
        int p1, p2;
        int len_s = s.length();
        int len_p = p.length();
        vector< vector<int> > f(len_s+1, vector<int> (len_p+1));
        f[0][0] = true;
        for (p1 = 1; p1 <= len_s; p1++) f[p1][0] = false;
        for (p2 = 1; p2 <= len_p; p2++) {
            if (p[p2-1] == '*' && p2 > 1) f[0][p2] = f[0][p2-2];
            else f[0][p2] = false;
        }
        for (p1 = 1; p1 <= len_s; p1++) 
            for (p2 = 1; p2 <= len_p; p2++) {
                if (p[p2-1] != '*') {
                    if (charMatch(s[p1-1], p[p2-1])) f[p1][p2] = f[p1-1][p2-1];
                    else f[p1][p2] = false;
                } else {
                    if (charMatch(s[p1-1], p[p2-2])) f[p1][p2] = f[p1-1][p2] || f[p1][p2-2];
                    else f[p1][p2] = f[p1][p2-2];
                }
            }
        return f[len_s][len_p];
    }

    bool charMatch(char a, char b) {
        return (b == '.' || a == b) ? true : false;
    }
};
// @lc code=end

