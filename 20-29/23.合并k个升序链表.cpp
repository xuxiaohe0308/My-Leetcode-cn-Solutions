/*
 * @lc app=leetcode.cn id=23 lang=cpp
 *
 * [23] 合并K个升序链表
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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        vector<ListNode*> p;
        p = lists;
        int n_listnode = p.size();  // 链表个数
        if (!n_listnode) return nullptr;  // 输入为空直接返回，防止27行报错
        int i, min, min_idx;
        int count = 0;  // 计数器，计到达末尾的指针数量
        ListNode* result = p[0];
        ListNode* result_head;  // 保存头节点位置，用于返回
        // 初始化count
        for (i = 0; i < n_listnode; i++) if (p[i] == nullptr) count++;
        
        if (count >= n_listnode) return nullptr;

        //  -------第一次循环--------
        // 遍历所有链表，找到最小的节点
        min=200000;
        for (i = 0; i < n_listnode; i++)
            if (p[i] != nullptr && p[i]->val < min) {
                min = p[i]->val; 
                min_idx = i;
            }
        // 接在result链表中
        result = p[min_idx];
        result_head = result;  // 保存头节点位置
        // 前移（判断是否为末尾）
        if (p[min_idx]->next != nullptr)
            p[min_idx] = p[min_idx]->next;
        else {
            p[min_idx] = nullptr;
            count++;
        }
        // -------------------------

        while (count < n_listnode) {
            // 遍历所有链表，找到最小的节点
            min=200000;
            for (i = 0; i < n_listnode; i++)
                if (p[i] != nullptr) 
                    if (p[i]->val < min) {
                        min = p[i]->val; 
                        min_idx = i;
                    }
            // 接在result链表中
            result->next = p[min_idx];
            result = result->next;
            // 前移（判断是否为末尾）
            if (p[min_idx]->next != nullptr)
                p[min_idx] = p[min_idx]->next;
            else {
                p[min_idx] = nullptr;
                count++;
            }
        }  // 所有指针到达末尾则退出循环

        return result_head;
    }
};
// @lc code=end

