#include <string>
#include <iostream>
#include <queue>
using namespace std;

bool solution(string s)
{
    queue<bool> q;
    for (char i : s)
    {
        if (i == ')')
        {
            if (q.size())
                q.pop();
            else
                return 0;
        }
        else
            q.push(1);
    }
    return !(q.size());
}