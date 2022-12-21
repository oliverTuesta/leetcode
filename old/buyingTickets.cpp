#include <bits/stdc++.h>

using namespace std;
class Solution
{
public:
    int timeRequiredToBuy(vector<int> &tickets, int k)
    {
        int time = 0;
        for (int i = 0; i < tickets.size(); i++)
        {

            if (tickets[i] >= tickets[k])
            {
                time += tickets[k];
                if (i > k)
                    time--;
            }
            else
                time += tickets[i];
        }
        return time;
    }
};

int main()
{
    Solution s;
    vector<int> tickets = {5, 1, 1, 1};
    cout << s.timeRequiredToBuy(tickets, 0) << '\n';
}