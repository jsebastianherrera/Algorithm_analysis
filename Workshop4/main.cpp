#include <cstring>
#include <fstream>
#include <iostream>
#include <vector>
typedef std::vector<std::vector<int>> vec;
void print(vec M) {
  for (int i = 0; i < M.size(); i++) {
    std::cout << std::endl;
    for (int j = 0; j < M[0].size(); ++j) {
      std::cout << M[i][j] << '\t';
    }
  }
  std::cout << std::endl;
}
unsigned int max(unsigned int a, unsigned int b) {
  if (a > b)
    return a;
  else
    return b;
}
vec read_file(std::string);
unsigned int naive(vec, unsigned int, unsigned int);
unsigned int aux_naive(vec);
unsigned int aux_memo(vec, vec &);
unsigned int memo(vec, vec &, unsigned int, unsigned int);
unsigned int bottom_up(vec);
int main(int argc, char **argv) {

  if (argc == 2) {
    std::string path = argv[1];
    vec T = read_file(path);
    print(T);
    std::cout << std::endl;
    vec M(T.size(), std::vector<int>(T[0].size(), 0));
    std::cout << "Naive:";
    std::cout << aux_naive(T) << std::endl;
    std::cout << "Memo:";
    std::cout << aux_memo(T, M) << std::endl;
    print(M);
    std::cout << std::endl;
    bottom_up(T);

  } else {
    std::cout << "1 parameter is needed" << std::endl;
  }

  return 0;
}
unsigned int aux_naive(vec T) {
  unsigned int q = 0;
  for (int i = 0; i < T.size() - 1; ++i) {
    for (int j = 0; j < T.size() - 1; ++j) {
      q = max(q, naive(T, i, j));
    }
  }
  return q;
}
unsigned int aux_memo(vec T, vec &M) {
  unsigned int q = 0;
  for (int i = 0; i < T.size() - 1; ++i) {
    for (int j = 0; j < T.size() - 1; ++j) {
      q = max(q, memo(T, M, i, j));
    }
  }
  return q;
}
unsigned int bottom_up(vec T) {
  vec M(T.size(), std::vector<int>(T.size(), 0));
  unsigned int q;
  for (int i = 0; i < T.size(); ++i) {
    q = 0;
    for (int j = 0; j < T.size(); ++j) {
      if (i < T.size() - 1 and T[i][j] + 1 == T[i + 1][j])
        q = max(q, M[i + 1][j]);
      if (j < T.size() - 1 and T[i][j] + 1 == T[i][j + 1])
        q = max(q, M[i][j + 1]);
      if (i > 0 and T[i][j] - 1 == T[i - 1][j])
        q = max(q, M[i - 1][j]);
      if (j > 0 and T[i][j] - 1 == T[i][j - 1])
        q = max(q, M[i][j - 1]);
      M[i][j] = q + 1;
    }
  }
  print(M);
  std::cout << std::endl;
  return 0;
}
unsigned int naive(vec T, unsigned int i, unsigned int j) {
  unsigned int q = 0;
  if (T.empty())
    return 0;
  else {
    if (i > 0 and T[i][j] + 1 == T[i - 1][j])
      q = max(q, naive(T, i - 1, j));
    if (i < T.size() - 1 and T[i][j] + 1 == T[i + 1][j])
      q = max(q, naive(T, i + 1, j));
    if (j > 0 and T[i][j] + 1 == T[i][j - 1])
      q = max(q, naive(T, i, j - 1));
    if (j < T.size() - 1 and T[i][j] + 1 == T[i][j + 1])
      q = max(q, naive(T, i, j + 1));
  }
  return q + 1;
}
unsigned int memo(vec T, vec &M, unsigned int i, unsigned int j) {
  unsigned int q = 0;
  if (T.empty())
    return 0;
  if (M[i][j] != 0)
    return M[i][j];
  else {
    if (i > 0 and T[i][j] + 1 == T[i - 1][j])
      q = max(q, memo(T, M, i - 1, j));
    if (i < T.size() - 1 and T[i][j] + 1 == T[i + 1][j])
      q = max(q, memo(T, M, i + 1, j));
    if (j > 0 and T[i][j] + 1 == T[i][j - 1])
      q = max(q, memo(T, M, i, j - 1));
    if (j < T.size() - 1 and T[i][j] + 1 == T[i][j + 1])
      q = max(q, memo(T, M, i, j + 1));
    M[i][j] = q + 1;
  }
  return M[i][j];
}
vec read_file(std::string path) {
  std::ifstream f;
  unsigned rows, cols;
  vec M;
  f.open(path);
  if (f.is_open()) {
    std::string line;
    int k = -1;
    while (f) {
      std::getline(f, line);
      if (k == -1) {
        rows = atoi(std::strtok((char *)line.c_str(), ","));
        cols = atoi(std::strtok(NULL, ","));
        vec m(rows, std::vector<int>(cols, 0));
        M = m;
        k = 0;
      } else {
        std::vector<int> col;
        char *pnt = std::strtok((char *)line.c_str(), ",");
        while (pnt != NULL) {
          col.push_back(atoi(pnt));
          pnt = std::strtok(NULL, ",");
        }
        if (!col.empty()) {
          for (int j = 0; j < cols; ++j) {
            M[k][j] = col[j];
          }
        }
        ++k;
      }
    }
  } else {
    std::cout << "File not found" << std::endl;
  }
  return M;
}
