#include <string>
#include <vector>
#include <algorithm>
using namespace std;

string solution(string s)
{
    string answer = "";
    int check = 0, num = 0;
    vector<int> v;
    for (char i : s)
    {
        if (i == ' ')
        {
            v.push_back(num * (check ? -1 : 1));
            num = check = 0;
        }
        else if (i == '-')
            check = 1;
        else
            num = num * 10 + (i - '0');
    }
    v.push_back(num * (check ? -1 : 1));

    sort(v.begin(), v.end());
    answer = to_string(v[0]) + " " + to_string(v.back());
    return answer;
}