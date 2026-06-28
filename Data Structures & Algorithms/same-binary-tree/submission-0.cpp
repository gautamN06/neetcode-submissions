/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:

    bool height(TreeNode* p, TreeNode* q)
    {   
        if(p == nullptr && q != nullptr)
            return false;
        else if(q == nullptr && p != nullptr)
            return false;
        else if(q == nullptr && p == nullptr)
            return true;
        if(p->val != q->val)
            return false;


        bool check = height(p->left, q->left);
        bool checkright = height(p->right, q->right);
        
            
        if(check && checkright)
            return true;
        else
            return false;
       
       
        
    }

    bool isSameTree(TreeNode* p, TreeNode* q) {

       return height(p,q);
        
    }
};
