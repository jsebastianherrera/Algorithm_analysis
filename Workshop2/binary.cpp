#include <climits>
#include <iostream>
#include <algorithm>
#include <vector>
#include <stdlib.h>
#include <chrono>
#include <cmath>
using namespace std;
typedef std::chrono::high_resolution_clock::time_point TimeVar;
#define duration(a) std::chrono::duration_cast<std::chrono::nanoseconds>(a).count() * 0.000000001
#define timeNow() std::chrono::high_resolution_clock::now()
template <typename F, typename... Args>
double funcTime(F func, Args &&...args)
{
    TimeVar t1 = timeNow();
    func(std::forward<Args>(args)...);
    return duration(timeNow() - t1);
}
vector<int> binary(unsigned long long int n);
void reverse_rotate(string::iterator first, string::iterator last);
int main(int argc, char **argv)
{
    // exe min max step
    unsigned long long int min = 1;
    int max = 64;
  
    for (int i = 1; i <= max; i++)
    {
        vector<int> S = binary(min);
        std::string s;
        std::vector<int>::reverse_iterator it;
        for (it = S.rbegin(); it != S.rend(); it++)
            s += to_string(*it);
        std::cout << s << "," << min << "," << funcTime(binary, min) << "," << funcTime(reverse_rotate, s.begin(), s.end()) << endl;
        min = min * 2;
    }
}
vector<int> binary(unsigned long long int n)
{
    vector<int> vec;
    while (n / 2 > 0)
    {
        vec.push_back(n % 2);
        n = n / 2;
    }
    vec.push_back(n % 2);
    return vec;
}
void reverse_rotate(string::iterator first, string::iterator last)
{
    if ((first == last) || next(first) == last)
        return;
    string::iterator middle = first;
    advance(middle, distance(first, last) / 2);
    reverse_rotate(first, middle);
    reverse_rotate(middle, last);
    rotate(first, middle, last);
}