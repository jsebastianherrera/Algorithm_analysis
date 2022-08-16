#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
vector<int> binary(int n);
void reverse_rotate(string::iterator first, string::iterator last);
int main()
{
    int n = 309;
    vector<int> S = binary(n);
    std::string s;
    // Print inverted binary
    cout << "ITE: ";
    for (int i = 0; i < S.size(); i++)
        cout << S[i];
    // Invert inverted_binary
    std::vector<int>::reverse_iterator it;
    for (it = S.rbegin(); it != S.rend(); it++)
        s += to_string(*it);
    reverse_rotate(s.begin(), s.end());
    cout << "\nREC: " << s << endl;
}
vector<int> binary(int n)
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