#include <iostream>

using std::cout;
using std::endl;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* sortedHead;
        ListNode* sortedWorking;

        if (list1 == nullptr && list2 == nullptr) {
            return nullptr;
        }

        if (list1 == nullptr && list2 != nullptr) {
            return list2;
        }

        if (list2 == nullptr && list1 != nullptr) {
            return list1;
        }

        // make the first assignment
        if (list1->val < list2->val) {
            sortedHead = list1;
            list1 = list1->next;
        }
        else {
            sortedHead = list2;
            list2 = list2->next;
        }
        // iterate through the lists
        sortedWorking = sortedHead;

        while (list1 != nullptr && list2 != nullptr) {
            if (list1->val < list2->val) {
                sortedWorking->next = list1;
                sortedWorking = sortedWorking->next;
                list1 = list1->next;
            }
            else { // list2->val <= list1->val
                sortedWorking->next = list2;
                sortedWorking = sortedWorking->next;
                list2 = list2->next;
            }
        }

        // handle any remaining list (eg if list2 still has elts left)
        if (list1 != nullptr) {
            sortedWorking->next = list1;
        }
        else if (list2 != nullptr) {
            sortedWorking->next = list2;
        }

        return sortedHead;
    }
};

int main() {
    // list 1
    ListNode list1last = ListNode(5);
    ListNode list1middle = ListNode(3, &list1last);
    ListNode list1front = ListNode(1, &list1middle);

    // list 2
    ListNode list2last = ListNode(6);
    ListNode list2middle = ListNode(4, &list2last);
    ListNode list2front = ListNode(2, &list2middle);

    Solution s = Solution();
    ListNode* head = s.mergeTwoLists(&list1front, &list2front);
    while (head != nullptr) {
        cout << head->val << endl;
        head = head->next;
    }
    return 0;
}