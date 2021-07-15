/*
 * @lc app=leetcode.cn id=17 lang=cpp
 *
 * [17] 电话号码的字母组合
 */

// @lc code=start
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        // 映射关系表
        map<char, string> digitNum;
        digitNum['2'] = "abc";
        digitNum['3'] = "def";
        digitNum['4'] = "ghi";
        digitNum['5'] = "jkl";
        digitNum['6'] = "mno";
        digitNum['7'] = "pqrs";
        digitNum['8'] = "tuv";
        digitNum['9'] = "wxyz";

        vector<string> result;
        while (!digits.empty()) {
            char c = digits[0];
            digits.erase(digits.begin());
            oneCharCombination(result, digitNum[c]);
        }
        return result;
    }

    // 迭代
    void oneCharCombination(vector<string>& result, string s) {
        int len = result.size();
        if (len == 0) {
            for (int i = 0; i < s.length(); i++) {
                string temp = "";
                temp.push_back(s[i]);
                result.push_back(temp);
            }
        } else {
            for (int i = 0; i < len; i++) {
                for (int j = 1; j < s.length(); j++) {
                    result.push_back(result[i] + s[j]);
                }
                result[i].push_back(s[0]);
            }
        }
    }
};

// @lc code=end


// Accepted
// 25/25 cases passed (0 ms)
// Your runtime beats 100 % of cpp submissions
// Your memory usage beats 98.84 % of cpp submissions (6.2 MB)
