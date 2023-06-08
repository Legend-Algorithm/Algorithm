#include <string>
#include <vector>
#include <iostream>
using namespace std;

vector<int> solution(string s)
{
    vector<int> answer;
    int cnt0 = 0, cnt1 = 0, cnt3 = 0;
    while (cnt1 != 1 && s != "1")
    {
        // 0 제거
        ++cnt3;
        cnt1 = 0;
        for (char i : s)
        {
            if (i == '0')
                ++cnt0;
            else
                ++cnt1;
        }
        s = "";
        while (cnt1)
        {
            s = ((cnt1 & 1) ? "1" : "0") + s;
            cnt1 >>= 1;
        }
        cout << s << endl;
    }
    answer.push_back(cnt3);
    answer.push_back(cnt0);
    return answer;
}