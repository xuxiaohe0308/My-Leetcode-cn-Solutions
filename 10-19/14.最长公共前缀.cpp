/*
 * @lc app=leetcode.cn id=14 lang=cpp
 *
 * [14] 最长公共前缀
 */

// @lc code=start
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string result;
        int len = strs.size();
        // 边界条件
        if (len == 0) return "";
        else if (len == 1) return strs[0];

        result = longestFromTwo(strs[0], strs[1]);
        for (int i = 2; i < len; i++) {
            result = longestFromTwo(result, strs[i]);
            if (result == "") return "";
        }
        return result;
    }

    string longestFromTwo(string str1, string str2) {
        int l1 = str1.length();
        int l2 = str2.length();
        int min_l = l1 > l2 ? l2 : l1;
        if (l1 == 0 || l2 == 0) return "";
        int idx = 0;
        string result = "";
        while(idx < min_l) {
            if (str1[idx] == str2[idx]){
                result.push_back(str1[idx]);
                idx++;
            }else break;
        }
        return result;
    }
};
// @lc code=end

