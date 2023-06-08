#include <string>
#include <vector>
#include <iostream>
using namespace std;

int solution(int n)
{
    int answer = 0;
    long long md, st, en, sum;
    for (int i = 1; i <= n; ++i)
    {
        md = n / i;
        if ((i & 1) && md <= i / 2)
            break;
        if (!(i & 1) && md < i / 2)
            break;
        if (i & 1)
        { // 홀수개
            sum = i * md;
            if (sum == n)
                ++answer;
        }
        else
        { // 짝수개
            sum = (i - 1) * md;
            if (sum + md + i / 2 == n)
                ++answer;
            if (sum + md - i / 2 == n)
                ++answer;
        }
    }
    return answer;
}