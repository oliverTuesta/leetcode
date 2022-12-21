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
    map<TreeNode *, int> treesHeight;

    int getHeight(TreeNode *tree)
    {
        if (tree == nullptr)
        {
            return 0;
        }
        else if (treesHeight.find(tree) == treesHeight.end())
            treesHeight[tree] = max(getHeight(tree->left), getHeight(tree->right)) + 1;
        return treesHeight[tree];
    }

public:
    bool isBalanced(TreeNode *root)
    {
        if (root == nullptr)
            return true;
        int leftH = getHeight(root->left);
        int rightH = getHeight(root->right);

        if (root->left != nullptr)
        {
            printf("%d: %d\n", root->left->val, leftH);
        }
        if (root->right != nullptr)
        {
            printf("%d: %d\n", root->right->val, rightH);
        }
        return abs(leftH - rightH) <= 1 &&
               isBalanced(root->left) && isBalanced(root->right);
    }
};

int main()
{
    struct TreeNode *three = new TreeNode(3);
    struct TreeNode *two = new TreeNode(2, nullptr, three);
    struct TreeNode *one = new TreeNode(1, nullptr, two);

    Solution s;
    cout << s.isBalanced(one) << endl;
}