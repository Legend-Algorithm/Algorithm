#include <string>
#include <vector>
#include <stack>
using namespace std;

int solution(string s)
{
    int answer = s.size(), chk;
    char c;
    stack<char> st;

    for (int i = 0; i < s.size(); ++i)
    {
        chk = 1;
        for (int j = i; j < s.size(); ++j)
        {
            c = s[j];
            if (c == ')' || c == '}' || c == ']')
            {
                if (!st.size() || (c == ')' && st.top() != '(') ||
                    (c == '}' && st.top() != '{') || (c == ']' && st.top() != '['))
                {
                    chk = 0;
                    --answer;
                    break;
                }
                st.pop();
            }
            else
                st.push(c);
        }
        for (int j = 0; j < i && chk; ++j)
        {
            c = s[j];
            if (c == ')' || c == '}' || c == ']')
            {
                if (!st.size() || (c == ')' && st.top() != '(') ||
                    (c == '}' && st.top() != '{') || (c == ']' && st.top() != '['))
                {
                    --answer;
                    break;
                }
                st.pop();
            }
            else
                st.push(c);
        }
        if (chk && st.size())
            --answer;
        st = {};
    }

    return answer;
}