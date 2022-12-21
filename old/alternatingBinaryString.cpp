#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  int minOperations(string s) {
    int cont = 0;
    bool binary = true;

    for (int i : s) {
      if (i - 48 != binary)
        cont++;
      binary = !binary;
    }
    return cont <= (s.size() / 2) ? cont : (s.size()) - cont;
  }
};

int main() {

  Solution s;
  string test = "1111";
  cout << s.minOperations(test) << '\n';
}
