#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    string reverseVowels(string s)
    {
        set<char> vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
        int j = s.size() - 1;
        int i = 0;

        while (i < j)
        {
            if (vowels.find(s[i]) == vowels.end())
                i++;
            if (vowels.find(s[j]) == vowels.end())
                j--;
            if (vowels.find(s[i]) != vowels.end() && vowels.find(s[j]) != vowels.end())
            {
                char aux = s[i];
                s[i] = s[j];
                s[j] = aux;
                i++;
                j--;
                if (j <= i)
                    break;
            }
        }
        return s;
    }
};

int main()
{
    Solution s;
    string test = "ai";
    cout << s.reverseVowels(test) << '\n';
}