/*
 * @lc app=leetcode.cn id=25 lang=cpp
 *
 * [25] K 个一组翻转链表
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
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (k == 1) return head;
        ListNode* dummyHead = new ListNode(-1, head);
        // 保存需要翻转区间的前一个节点和区间内最后一个节点
        ListNode* front, * first, * rear;
        // 初始化两个指针
        front = dummyHead;
        first = head;
        rear = dummyHead;
        for (int i = 0; i < k; i++) rear = rear->next;
        while (rear != nullptr) {
            // 翻转front rear内的区间
            ListNode* newFront;
            newFront = first;
            front->next = rear;
            if (k == 2) {
                first->next = rear->next;
                rear->next = first;
            } else {
                reverse(first, rear, k);
                if (first->next == nullptr) break;
            }
            front = newFront;
            first = front->next;
            rear = front;
            // 指针往后走
            for (int i = 0; i < k && rear != nullptr; i++) rear = rear->next;
        }
        return dummyHead->next;
    }

    void reverse(ListNode* first, ListNode* rear, int k) {
        ListNode* t1, * t2, * t3;
        t1 = first;
        t2 = t1->next;
        t3 = t2->next; 
        first->next = rear->next;
        int i = 1;
        while (1) {
            t2->next = t1;
            i++;
            if (i >= k) break;
            t1 = t2;
            t2 = t3;
            t3 = t3->next;
        }
    }

};
// @lc code=end

// Accepted
// 62/62 cases passed (16 ms)
// Your runtime beats 87 % of cpp submissions
// Your memory usage beats 77.09 % of cpp submissions (11.1 MB)
