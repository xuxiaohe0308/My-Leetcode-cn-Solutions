"""
功能要求，输出给定的字符串是否符合以下要求：
1.长度超过8位
2.包括大小写字母.数字.其它符号,以上四种至少三种
3.不能有相同长度超2的子串重复
说明:长度超过2的子串
输入描述:
一组或多组长度超过2的子符串。每组占一行
输出描述:
如果符合要求输出：OK，否则输出NG
例如：
输入
021Abc9000
021Abc9Abc1
输出
OK
NG
"""
class Solution:
    def __init__(self):
        self.s = input()
        self.flag_up = 0
        self.flag_low = 0
        self.flag_num = 0
        self.flag_oth = 0

    def main(self):
        s = self.s
        l = len(s)
        if l < 8:
            return "NG"
        
        hash_table = {}
        n1 = s[0]
        self.check(n1)
        n2 = s[1]
        self.check(n2)

        for i in range(2, l):
            n3 = s[i]
            self.check(n3)
            sub_s = n1 + n2 + n3
            if sub_s in hash_table.keys():
                if hash_table[sub_s] < i - 2:
                    return "NG"
            else:
                hash_table[sub_s] = i
            n1, n2 = n2, n3

        if self.flag_up + self.flag_low + self.flag_num + self.flag_oth < 3:
            return "NG"
        return "OK"

    def check(self, c):
        if "Z" >= c >= "A":
            self.flag_up = 1
        elif "z" >= c >= "a":
            self.flag_low = 1
        elif "9" >= c >= "0":
            self.flag_num = 1
        else:
            self.flag_oth = 1


if __name__ == "__main__":
    while True:
        try:
            s = Solution()
            print(s.main())
        except:
            break
        