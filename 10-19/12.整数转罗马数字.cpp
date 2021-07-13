/*
 * @lc app=leetcode.cn id=12 lang=cpp
 *
 * [12] 整数转罗马数字
 */

// @lc code=start
class Solution {
public:
    string intToRoman(int num) {
        string result = "";
        // 千位
        int th = num / 1000;
        if(th > 0){  
            for(int i=0; i<th; i++) result.push_back('M');
        }
        num = num % 1000;
        // 百位
        int hund = num / 100;
        result.append(intToRomanByNum(hund, 'C', 'D', 'M'));
        num = num % 100;
        // 十位
        int ten = num / 10;
        result.append(intToRomanByNum(ten, 'X', 'L', 'C'));
        num = num % 10;
        // 个位
        result.append(intToRomanByNum(num, 'I', 'V', 'X'));
        return result;
    }


    string intToRomanByNum(int num, char one, char five, char ten) {
        string result = "";
        if(num > 0 && num < 4){ 
            for(int i=0; i<num; i++) result.push_back(one);
        }else if(num >= 5 && num < 9){
            result.push_back(five);
            for(int i=0; i<num-5; i++) result.push_back(one);
        }else if(num == 4){
            result.push_back(one);
            result.push_back(five);
        }else if (num == 9){
            result.push_back(one);
            result.push_back(ten);
        }
        return result;
    }
};
// @lc code=end

