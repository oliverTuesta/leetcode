#include <bits/stdc++.h>
using namespace std;

class Solution
{
private:
    bool cmp(pair<string, int> &a,
             pair<string, int> &b)
    {
        return a.second < b.second;
    }

public:
    vector<int> relativeSortArray(vector<int> &arr1, vector<int> &arr2)
    {
        vector<int> result;
        map<int, int> aux; // element, times that repeats
        int x = 0;
        for (int j = 0; j < arr1.size(); j++)
        {
            if (aux.find(arr1[j]) == aux.end())
                aux[arr1[j]] = 1;
            else
                aux[arr1[j]]++;
        }
        for (int i : arr2)
        {
            while (aux[i] > 0)
            {
                result.push_back(i);
                aux[i]--;
                x++;
            }
            aux.erase(i);
        }
        for (auto const &entry : aux)
            while (entry.second > 0)
            {
                result.push_back(entry.first);
                aux[entry.first]--;
            }

        return result;
    }
};

int main()
{
    vector<int> arr1 = {2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19};
    vector<int> arr2 = {2, 1, 4, 3, 9, 6};
    Solution s;
    vector<int> result = s.relativeSortArray(arr1, arr2);
    for (int i : result)
        cout << i << " ";
    cout << '\n';
}