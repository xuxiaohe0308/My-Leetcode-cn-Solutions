#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        T = numRows * 2 - 2  # 周期
        half = int(T/2)  # 半周期
        l = len(s)
        total_T = l // T  # 共几个周期
        rest = l % T - 1  # 多余的部分
        result = list()
        if total_T == 0:
            if rest >= 0:
                result.append(s[0])
            for row in range(1, numRows-1):
                if row <= rest < T-row:  # 补一个
                        result.append(s[row])
                elif rest >= T-row:  # 补两个
                    result.append(s[row])
                    result.append(s[T - row])
            if rest >= half:  # 补一个
                result.append(s[half])
        else:
            # 首行
            for idx in range(total_T):
                result.append(s[idx*T])
            if rest >= 0:
                result.append(s[total_T * T])
            # 中间行
            for row in range(1, numRows-1):
                for idx in range(total_T):
                    result.append(s[idx * T + row])
                    result.append(s[(idx+1) * T - row])
                if row <= rest < T-row:  # 补一个
                    result.append(s[total_T * T + row])
                elif rest >= T-row:  # 补两个
                    result.append(s[total_T * T + row])
                    result.append(s[(total_T+1) * T - row])
            # 末尾行
            for idx in range(total_T):
                result.append(s[idx*T+half])
            if rest >= half:  # 补一个
                result.append(s[total_T*T+half])
        
        return ''.join(result)
# @lc code=end
