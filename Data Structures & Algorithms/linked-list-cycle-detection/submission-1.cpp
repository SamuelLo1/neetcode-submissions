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

 /* 
 simple sol: can have a set keep track of visited nodes
 */ 

class Solution {
public:
    bool hasCycle(ListNode* head) {
        std::unordered_set<ListNode*> visited_nodes;  
        while (head != NULL ){
            if(visited_nodes.contains(head)){
                return true;
            }

            visited_nodes.insert(head);
            head = head->next;

        }
        return false;
    }
};
