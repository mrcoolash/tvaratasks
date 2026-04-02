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
        
        // Create two pointers
        // slow moves 1 step at a time
        // fast moves 2 steps at a time
        ListNode *slow = head;
        ListNode *fast = head;

        // Traverse the linked list until fast reaches end
        // If fast becomes NULL, no cycle exists
        while (fast != NULL && fast->next != NULL) {
            
            // Move slow by 1 node
            slow = slow->next;

            // Move fast by 2 nodes
            fast = fast->next->next;

            // If slow and fast meet, cycle exists
            if (slow == fast) {
                
                // Create another pointer starting from head
                ListNode *temp = head;

                // Move both temp and slow one step at a time
                // They will meet at the starting node of the cycle
                while (temp != slow) {
                    temp = temp->next;
                    slow = slow->next;
                }

                // Return the node where cycle begins
                return temp;
            }
        }

        // If no cycle is found, return NULL
        return NULL;
    }
};