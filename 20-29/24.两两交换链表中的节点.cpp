/*
 * @lc app=leetcode.cn id=24 lang=cpp
 *
 * [24] 两两交换链表中的节点
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
    ListNode* swapPairs(ListNode* head) {
        ListNode* now, * nextp;
        if (head == nullptr || head->next == nullptr) return head;
        // 初始化
        now = head;
        nextp = head->next;
        head = nextp;
        ListNode* pre = new ListNode(0, head);
        while (1) {
            now->next = nextp->next;
            nextp->next = now;
            pre->next = nextp;
            pre = now;
            if (now->next != nullptr) now = now->next;
            else break;
            if (now->next != nullptr) nextp = now->next;
            else break;
        }
        return head;
    }
};
// @lc code=end

