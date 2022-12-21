#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int minimumMoves(string s)
    {
        int count = 0;
        int i = 0;
        while (i < s.size())
        {
            if (s[i] == 'X')
            {
                i += 3;
                count++;
            }
            else
                i++;
        }
        return count;
    }
};

int main()
{
    string s = "XXXX";
    Solution sol;
    cout << sol.minimumMoves(s) << endl;
}