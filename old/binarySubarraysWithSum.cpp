#include <bits/stdc++.h>
using namespace std;

class Solution {

public:
  int numSubarraysWithSum(vector<int> &nums, int goal) {
    int count = 0;
    if (goal == 0) {
      int ceros = 0; // ceros in a row
      for (int i = 0; i < nums.size(); i++) {
        if (nums[i] == 1) {
          count += ceros * (ceros + 1) / 2;

          ceros = 0;
        }

        else
          ceros++;
      }
      if (!nums[nums.size() - 1])
        count += ceros * (ceros + 1) / 2;
      return count;
    }
    int left = 0;
    int right = -1;
    int sum = 0;
    while (sum < goal) {
      right++;
      sum += nums[right];
      if (right == nums.size() - 1 && sum < goal)
        return 0;
    }

    while (right < nums.size()) {
      int leftCeros = 1;
      int rightCeros = 1;
      while (nums[left] == 0) {
        leftCeros++;
        left++;
      }
      left++;
      right++;
      while (right < nums.size() && nums[right] == 0) {
        rightCeros++;
        right++;
      }
      count += leftCeros * rightCeros;

      // printf("l:%d r:%d  c:%d\n", left, right, count);
    }
    return count;
  }
};

int main() {
  vector<int> nums = {0, 0, 0, 0, 1, 0, 0, 0, 0, 0,
                      1, 1, 0, 0, 0, 0, 0, 1, 0, 0};
  int goal = 3;
  Solution s;
  cout << s.numSubarraysWithSum(nums, goal) << endl;

  cout << "ola" << endl;
}
