#include <bits/stdc++.h>

using namespace std;

// Definition for a binary tree node.
struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution
{

private:
    set<int> values;

    void makeSet(TreeNode *root)
    {
        values.insert(root->val);
        if (root->left != nullptr)
            makeSet(root->left);
        if (root->right != nullptr)
            makeSet(root->right);
    }

public:
    bool findTarget(TreeNode *root, int k)
    {
        makeSet(root);
        for (int i : values)
        {
            if (values.find(k - i) != values.end() && k - i != i)
                return true;
        }
        return false;
    }
};

int main()
{
}