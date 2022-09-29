#include <cstring>
#include <fstream>
#include <iostream>
#include <utility>
#include <vector>
typedef std::vector<std::vector<int>> vec;
typedef std::vector<std::vector<std::pair<unsigned int, unsigned int>>> tup;
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
unsigned int aux(vec T, vec &M, tup &B, unsigned int i, unsigned int j);
unsigned int naive(vec, unsigned int, unsigned int);
unsigned int aux_naive(vec);
unsigned int aux_memo(vec, vec &);
std::vector<unsigned int> backtracking(vec matrix);
unsigned int memo(vec, vec &, unsigned int, unsigned int);
int main(int argc, char **argv) {

  if (argc == 2) {
    std::string path = argv[1];
    vec T = read_file(path);
    vec M(T.size(), std::vector<int>(T[0].size(), 0));
    std::cout << std::endl;
    std::vector<unsigned int> rt = backtracking(T);
    for (int i : rt)
      std::cout << i <<",";
  } else {
    std::cout << "1 parameter is needed" << std::endl;
  }

  return 0;
}
unsigned int aux(vec T, vec &M, tup &B, unsigned int i, unsigned int j) {
  if (T.empty())
    return 0;
  if (M[i][j] != 0)
    return M[i][j];
  else {
    unsigned int q = 0;
    if (i > 0 and T[i][j] + 1 == T[i - 1][j]) {
      q = max(q, aux(T, M, B, i - 1, j));
      if (q == M[i - 1][j])
        B[i][j] = std::make_pair(i - 1, j);
    }
    if (i < T.size() - 1 and T[i][j] + 1 == T[i + 1][j]) {
      q = max(q, aux(T, M, B, i + 1, j));
      if (q == M[i + 1][j])
        B[i][j] = std::make_pair(i + 1, j);
    }
    if (j > 0 and T[i][j] + 1 == T[i][j - 1]) {
      q = max(q, aux(T, M, B, i, j - 1));
      if (q == M[i][j - 1])
        B[i][j] = std::make_pair(i, j - 1);
    }
    if (j < T.size() - 1 and T[i][j] + 1 == T[i][j + 1]) {
      q = max(q, aux(T, M, B, i, j + 1));
      if (q == M[i][j + 1])
        B[i][j] = std::make_pair(i, j + 1);
    }
    M[i][j] = q + 1;
  }
  return M[i][j];
}
tup fillB(vec T) {
  tup B(T.size(),
        std::vector<std::pair<unsigned int,unsigned int>>(T.size(), std::make_pair(0, 0)));
  for (int i = 0; i < T.size(); ++i)
    for (int j = 0; j < T.size(); ++j)
      B[i][j] = std::make_pair(i, j);
  return B;
}
std::vector<unsigned int> backtracking(vec T) {
  vec M(T.size(), std::vector<int>(T.size()));
  tup B(
      T.size(),
      std::vector<std::pair<unsigned int, unsigned int>>(T.size()));

 B =fillB(T); 

  unsigned int q = 0;
  std::pair<unsigned int, unsigned int> current;
  for (unsigned int i = 0; i < T.size(); i++) {
    for (unsigned int j = 0; j < T[0].size(); j++) {
      q = std::max(q, aux(T, M, B, i, j));
      if (q == M[i][j]) {
        current = std::make_pair(i, j);
      }
    }
  }

  std::vector<unsigned int> rt;
  while (B[current.first][current.second] != current) {
    rt.push_back(T[current.first][current.second]);
    current = B[current.first][current.second];
  }
  rt.push_back(T[current.first][current.second]);
  return rt;
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
