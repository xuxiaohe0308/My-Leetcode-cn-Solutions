/*
 * @lc app=leetcode.cn id=142 lang=cpp
 *
 * [142] 环形链表 II
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
    ListNode *detectCycle(ListNode *head) {
        ListNode* fast = head, * slow = head;
        while (fast && fast->next) {
            fast = fast->next->next;
            slow = slow->next;
            if (fast == slow) {
                fast = head;
                while (fast != slow) {
                    fast = fast -> next;
                    slow = slow -> next;
                }
                return fast;
            }
        }
        return nullptr;
    }
};
// @lc code=end

// Accepted
// 16/16 cases passed (8 ms)
// Your runtime beats 89.5 % of cpp submissions
// Your memory usage beats 44.11 % of cpp submissions (7.5 MB)
