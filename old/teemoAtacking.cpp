#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int findPoisonedDuration(vector<int> &timeSeries, int duration)
    {

        int time = duration;
        for (int i = 0; i < timeSeries.size() - 1; i++)
        {
            time += min(duration, timeSeries[i + 1] - timeSeries[i]);
        }
        return time;
    }
};

int main()
{
    Solution s;
    vector<int> timeSeries = {1, 2};
    int duration = 2;
    cout << s.findPoisonedDuration(timeSeries, duration) << endl;
}