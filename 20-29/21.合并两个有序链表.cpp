/*
 * @lc app=leetcode.cn id=21 lang=cpp
 *
 * [21] 合并两个有序链表
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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if(l1 == nullptr && l2 == nullptr) return nullptr;

        ListNode* p1 = l1;
        ListNode* p2 = l2;
        ListNode* result = new ListNode();
        ListNode* p = result;

        while(1){
            if(p1 == nullptr && p2 == nullptr) return result;
            else{
                
                if(p2 == nullptr || ((p1 != nullptr) && (p1->val < p2->val))){
                    p->val = p1->val;
                    if(p1->next) p1 = p1->next;
                    else p1 = nullptr;
                }else{
                    p->val = p2->val;
                    if(p2->next) p2 = p2->next;
                    else p2 = nullptr;
                }
            }
            if(!(p1 == nullptr && p2 == nullptr)){
                // 创建新节点
                p->next = new ListNode();
                p = p->next;
            }
        }
        return result;
    }
};
// @lc code=end
