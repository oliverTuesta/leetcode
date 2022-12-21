#include <bits/stdc++.h>

using namespace std;

class Solution
{

    struct Rod
    {
        bool red = false;
        bool green = false;
        bool blue = false;
    };

public:
    int countPoints(string rings)
    {
        struct Rod r;
        vector<struct Rod> rods;

        for (int i = 0; i < 10; i++)
        {
            rods.push_back(r);
        }

        for (int i = 0; i < rings.size(); i += 2)
        {

            switch (rings[i])
            {
            case 'R':
                rods[rings[i + 1] - '0'].red = true;
                break;
            case 'G':
                rods[rings[i + 1] - '0'].green = true;
                break;
            case 'B':
                rods[rings[i + 1] - '0'].blue = true;
                break;
            }
        }

        int count = 0;
        for (int i = 0; i < 10; i++)
        {
            if (rods[i].red && rods[i].green && rods[i].blue)
                count++;
        }
        return count;
    }
};

int main()
{
    Solution s;

    string data = "G4";
    cout << s.countPoints(data) << '\n';
    return 0;
}