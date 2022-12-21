#include <bits/stdc++.h>
using namespace std;

class Solution {
private:
public:
  Solution() {}
  ~Solution() {}

  void rotate(vector<vector<int>> &matrix) {
    int size = matrix.size();

    vector<vector<int>> rotated;
    for (int i = 0; i < size; i++) {
      vector<int> v(size, 0);
      rotated.push_back(v);
    }
    for (int i = 0; i < size; i++) {
      for (int j = 0; j < size; j++) {
        rotated[j][size - 1 - i] = matrix[i][j];
      }
    }
    matrix = rotated;
  }
};

int main(int argc, char *argv[]) {
  Solution s;
  vector<vector<int>> matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};

  s.rotate(matrix);
  for (auto arr : matrix) {
    for (int i : arr) {
      cout << i << " ";
    }
    cout << '\n';
  }
  return 0;
}
