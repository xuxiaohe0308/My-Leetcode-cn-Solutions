/*
 * @lc app=leetcode.cn id=19 lang=cpp
 *
 * [19] 删除链表的倒数第 N 个结点
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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* node_before_n = head;  // 向前数第n个节点
        ListNode* p = head;  // 当前指向的节点
        for(int i=0; i<n; i++){
            if(p->next) p = p->next;
            else return head->next;
        } 
        // 目前node_before_n指向的是p的前n个节点
        // 当p跑到末尾时node_before_n->next为待删除的节点
        while(p->next){
            p = p->next;
            node_before_n = node_before_n->next;
        }
        node_before_n->next = node_before_n->next->next;

        return head;
    }
};
// @lc code=end

