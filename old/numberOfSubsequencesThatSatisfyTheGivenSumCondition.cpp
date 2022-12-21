#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int numSubseq(vector<int> &nums, int target)
    {

        int min = 0;
        int max = 0;
        long subsequences = 0;
        for (int i = 0; i < nums.size() - 1; i++)
        {
            if (nums[i] > target)
                continue;
            else
                printf("num:%d\n", nums[i]);

            subsequences++;
            min = max = i;
            for (int j = i + 1; j < nums.size(); j++)
            {
                if (nums[j] > max)
                    max = j;
                else if (nums[j] < min)
                    min = j;
                if (nums[min] + nums[max] <= target)
                {
                    printf("min:%d max:%d\n", nums[min], nums[max]);
                    subsequences++;
                }
                else
                    break;
            }
        }

        return subsequences % 1000000007;
    }
};

int main()
{

    vector<int> nums = {3, 5, 6, 7};
    int target = 9;
    Solution s;
    cout << s.numSubseq(nums, target) << endl;
}