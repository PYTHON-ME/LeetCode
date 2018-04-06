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
    ListNode* reverseList(ListNode* head) {
        ListNode *p, *q, *pr;
        if(!head)  return head;
        p = head;
        q = NULL;
        while(p)
        {
            pr = p->next;
            p->next = q;
            q = p;
            p = pr;
        }
        return q;
    }
};
