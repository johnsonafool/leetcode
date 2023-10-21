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
    ListNode* find_mid (ListNode* head) {
        ListNode* fast = head;
        ListNode* slow = head;
        while (fast && fast->next) {
            fast = fast->next->next;
            slow = slow->next;
        }
        return slow;
    }

    ListNode* reverse_r (ListNode* slow) {
        ListNode* curr = slow;
        ListNode* next = slow->next;
        curr->next = NULL;
        while (next != NULL) {
            ListNode *temp = next->next;
            next->next = curr;
            curr = next;
            next = temp;
        }
        return curr;
    }

    void reorderList(ListNode* head) {                
        if(!head || !head ->next) return;
        auto M = find_mid(head);
        auto R = reverse_r(M);
        auto L = head->next;

        for(int i = 0; L != R; i++, head = head->next) {    
            if(i & 1) {                              
                head->next = L;
                L = L->next;
            }
            else {
                head->next = R;
                R = R->next;
            }
        }
    }
};