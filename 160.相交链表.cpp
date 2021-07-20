/*
 * @lc app=leetcode.cn id=160 lang=cpp
 *
 * [160] 相交链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        // 双指针，交叉遍历
        ListNode* a = headA, * b = headB;
        while (a != b) {
            if (a) a = a->next; else a = headB;
            if (b) b = b->next; else b = headA;
        }
        cout << a << endl;
        return a;
    }
};
// @lc code=end

// Accepted
// 39/39 cases passed (56 ms)
// Your runtime beats 46.98 % of cpp submissions
// Your memory usage beats 58.39 % of cpp submissions (14.3 MB)
