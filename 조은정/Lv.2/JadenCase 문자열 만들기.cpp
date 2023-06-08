#include <string>
#include <vector>

using namespace std;

string solution(string s)
{
    string answer = "";
    int chk = 0;
    for (char i : s)
    {
        if (i == ' ')
            chk = 0, answer += ' ';
        else if (chk)
        {
            if ('0' <= i && i <= '9')
                answer += i;
            else if ('a' <= i && i <= 'z')
                answer += i;
            else
                answer += ('a' + (i - 'A'));
        }
        else
        {
            chk = 1;
            if ('0' <= i && i <= '9')
                answer += i;
            else if ('A' <= i && i <= 'Z')
                answer += i;
            else
                answer += ('A' + (i - 'a'));
        }
    }
    return answer;
}