#include <bits/stdc++.h>

using namespace std;

#define ll long

class Solution
{
public:
    ll arithmeticProgression(int a, int n) { return (ll)n * (a + a - n + 1) / 2; }

    int maxProfit(vector<int> &inventory, int orders)
    {
        ll profit = 0;
        sort(inventory.begin(), inventory.end());

        int i = inventory.size() - 1;
        int n = 1;

        while (orders > 0)
        {
            while (i > 0 && inventory[i] == inventory[i - 1])
            {
                i--;
                n++;
            }
            if (i == 0 || ((inventory[i] - inventory[i - 1]) * n) > orders)
            {
                int result = orders / n;
                int residuo = orders % n;
                profit += arithmeticProgression(inventory[i], result) * n;
                orders -= result * n;
                inventory[i] -= result;
                profit += arithmeticProgression(inventory[i], 1) * residuo;
                orders -= residuo;
            }
            else
            {
                profit += arithmeticProgression(inventory[i], inventory[i] - inventory[i - 1]) * n;
                orders -= (inventory[i] - inventory[i - 1]) * n;
                inventory[i] = inventory[i - 1];
            }
        }
        return profit % 1000000007;
    }
};

int main()
{
    Solution s;
    vector<int> inventory = {497978859, 167261111, 483575207, 591815159};
    int orders = 836556809;
    cout << s.maxProfit(inventory, orders) << '\n';
}