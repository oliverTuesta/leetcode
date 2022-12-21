#include <algorithm>
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  bool find(vector<int> &nums, int target) {
    int n = nums.size();
    int a = 0, b = n - 1;
    while (a <= b) {
      int mid = (a + b) / 2;
      if (nums[mid] == target)
        return true;
      if (target > nums[mid])
        a = mid + 1;
      else
        b = mid - 1;
    }
    return false;
  }

  int findFinalValue(vector<int> &nums, int original) {

    sort(nums.begin(), nums.end());
    for (int i = 0; i < nums.size(); i++) {
      if (find(nums, original))
        original *= 2;
      else
        break;
    }
    return original;
  }
};

int main() {
  vector<int> arr = {5, 3, 6, 1, 12};

  sort(arr.begin(), arr.end());
  Solution s = Solution();

  return 0;
}
