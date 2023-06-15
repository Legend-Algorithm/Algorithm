#include <string>
#include <vector>
using namespace std;

int solution(vector<int> arr)
{
    int answer = arr[0], tmp, cnt;
    for (int i : arr)
    {
        cnt = 0;
        tmp = answer;
        while (tmp % i)
            tmp = answer * (++cnt);
        answer = tmp;
    }

    return answer;
}