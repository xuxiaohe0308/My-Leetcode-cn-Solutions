/*
 * @lc app=leetcode.cn id=13 lang=cpp
 *
 * [13] 罗马数字转整数
 */

// @lc code=start
class Solution {
public:
    int romanToInt(string s) {
        // 先将字符串转为一串数字，用于表示数的大小
        int len = s.length();
        int * s_key = new int[len];
        int i;
        for (i = 0; i < len; i++) {
            char c = s[i];
            switch(c){
                case 'I': s_key[i] = 1; break;
                case 'V': s_key[i] = 5; break;
                case 'X': s_key[i] = 10; break;
                case 'L': s_key[i] = 50; break;
                case 'C': s_key[i] = 100; break;
                case 'D': s_key[i] = 500; break;
                case 'M': s_key[i] = 1000; break;
            }
        }
        // 存放结果
        int result = s_key[0];
        int temp = result;
        for (i = 1; i < len; i++) {
            if (s_key[i] > temp) {
                // 前一位比这一位小
                result -= (temp + temp);
            }
            result += s_key[i];
            temp = s_key[i];
        }

        delete[] s_key;
        return result;
    }
};
// @lc code=end

