#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    string shortestCompletingWord(string licensePlate, vector<string> &words)
    {
        // deleting spaces and numbers, and converting characters to lower case
        string licenseP;
        for (char c : licensePlate)
            if (c < 48 && c != 32 || c > 57)
                licenseP += tolower(c);
        int minor = -1;
        for (int i = 0; i < words.size(); i++)
        {
            if (minor == -1 || words[i].size() < words[minor].size())
            {
                int word[26] = {0};
                for (char c : words[i])
                    word[c - 97]++;
                for (char c : licenseP)
                {
                    if (word[c - 97] == 0)
                        goto CONTINUE;

                    word[c - 97]--;
                }
                minor = i;
            }

        CONTINUE:
            continue;
        }
        return words[minor];
    }
};

int main()
{
    string licensePlate = "IE71146";
    vector<string> words = {"recognize", "student", "choice", "similar", "less", "feel", "room", "customer", "require", "course"};
    Solution s;
    cout << s.shortestCompletingWord(licensePlate, words) << endl;
}