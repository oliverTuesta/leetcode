#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    string firstPalindrome(vector<string> &words)
    {
        for (int i = 0; i < words.size(); i++)
        {
            for (int j = 0; j < words[i].size() / 2; j++)
            {
                if (words[i][j] != words[i][words[i].size() - 1 - j])
                {
                    goto END;
                }
            }
            return words[i];
        END:
            continue;
        }
        return "";
    }
};

int main()
{
    Solution s;
    vector<string> words = {"def", "ghi"};
    cout << s.firstPalindrome(words) << '\n';
    return 0;
}