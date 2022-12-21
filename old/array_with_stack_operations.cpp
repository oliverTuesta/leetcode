#include <bits/stdc++.h>
using namespace std;

class Solution {
private:
public:
  Solution() {}
  ~Solution() {}

  vector<string> buildArray(vector<int> &target, int n) {
    int i = 1;
    vector<string> result;
    int opeartions = 0;
    for (int value : target) {
      if (i == value)
        result.push_back("Push");
      else {
        for (int x = 0; x < value - i; x++) {
          result.push_back("Push");
          result.push_back("Pop");
        }
        result.push_back("Push");
      }
      opeartions += value - i - 1;
      i = value + 1;
    }
    return result;
  }
};

int main(int argc, char *argv[]) {

  Solution s;
  vector<int> target = {1, 2, 3};
  for (auto i : s.buildArray(target, 3)) {
    cout << i << '\n';
  }

  return 0;
}
