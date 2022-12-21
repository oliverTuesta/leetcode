#include <bits/stdc++.h>
using namespace std;

class Solution
{

public:
    vector<int> decrypt(vector<int> &code, int k)
    {
        vector<int> decriptedCode(code.size(), 0);
        if (k == 0)
            return decriptedCode;

        int n = code.size();
        int sum = 0;

        int left;
        int right;
        if (k > 0)
        {
            left = 1;
            right = k + 1;
            for (int i = 1; i <= k; i++)
                sum += code[i];
        }
        else
        {
            left = n + k;
            right = 0;
            for (int i = n + k; i <= n - 1; i++)
                sum += code[i];
        }
        decriptedCode[0] = sum;
        for (int i = 1; i < n; i++)
        {
            if (right >= n)
                right = 0;
            if (left >= n)
                left = 0;
            sum -= code[left];
            sum += code[right];
            decriptedCode[i] = sum;
            left++;
            right++;
        }
        return decriptedCode;
    }
};

int main()
{
    vector<int> code = {2, 4, 9, 3};
    int k = 1;
    Solution s;
    vector<int> result = s.decrypt(code, k);
    for (int i : result)
    {
        cout << i << " ";
    }
    cout << endl;
}