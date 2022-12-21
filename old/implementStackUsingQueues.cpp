#include <bits/stdc++.h>
using namespace std;

class MyStack
{
private:
    int *queue;
    int n;

public:
    MyStack()
    {
        queue = new int[0];
        n = 0;
    }

    void push(int x)
    {
        int *newQueue = new int[n + 1];
        for (int i = 0; i < n; i++)
        {
            newQueue[i] = queue[i];
        }
        newQueue[n] = x;
        delete[] queue;
        queue = newQueue;
        n++;
    }

    int pop()
    {
        int aux = queue[n - 1];
        int *newQueue = new int[n - 1];
        for (int i = 0; i < n - 1; i++)
        {
            newQueue[i] = queue[i];
        }
        n--;
        queue = newQueue;
        return aux;
    }

    int top()
    {
        return queue[n - 1];
    }

    bool empty()
    {
        return n == 0;
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */

int main()
{
    MyStack *myStack = new MyStack();
    myStack->push(1);
    myStack->push(2);
    cout << myStack->pop() << endl; // return 2
    cout << myStack->top() << endl; // return 2
    // cout << myStack->empty() << endl; // return False
}