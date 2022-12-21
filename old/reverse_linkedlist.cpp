#include <bits/stdc++.h>
using namespace std;

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
  ListNode *reverseList(ListNode *head) {
    if (head == NULL || head->next == nullptr)
      return head;
    vector<int> values;
    ListNode *node = head;
    do {
      values.push_back(node->val);
      node = node->next;
    } while (node->next != nullptr);
    values.push_back(node->val);
    int i = values.size() - 1;
    node = head;
    do {
      cout << i << '\n';
      node->val = values[i];
      node = node->next;
      i--;
    } while (node->next != nullptr);
    node->val = values[i];

    return head;
  }
};

void agregarNodos(ListNode *node, int val) {
  if (val > 0) {
    ListNode *nuevoNodo;
    nuevoNodo->val = val;
    node->next = nuevoNodo;
    agregarNodos(nuevoNodo, val++);
  }
}

int main(int argc, char *argv[]) {

  ListNode *nodo;
  nodo->val = 10;
  agregarNodos(nodo, 9);

  while (nodo->next != nullptr) {
    cout << nodo->next->val << '\n';
    nodo = nodo->next;
  }
  return 0;
}
