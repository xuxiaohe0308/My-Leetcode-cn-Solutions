/*
 * @lc app=leetcode.cn id=206 lang=cpp
 *
 * [206] 反转链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        // 迭代
        if (!head || !head->next) return head;
        ListNode* p1 = head, * p2 = head->next, * p3;
        while (p3) {
            p3 = p2->next;
            p2->next = p1;
            p1 = p2;
            p2 = p3;
        }
        head->next = nullptr;
        return p1;
    }
};
// @lc code=end

// Accepted
// 28/28 cases passed (0 ms)
// Your runtime beats 100 % of cpp submissions
// Your memory usage beats 71.37 % of cpp submissions (8 MB)
