#include <string>
#include <vector>
#include <map>
using namespace std;

map<pair<int, int>, int> mp;
int sz[10000010];

int solution(int k, vector<int> tangerine)
{
    int answer = 0, cnt = tangerine.size();
    for (int i : tangerine)
        ++sz[i];
    for (int i : tangerine)
        mp[{sz[i], i}] = sz[i];

    answer = mp.size();
    if (cnt > k)
    {
        for (auto i : mp)
        {
            cnt -= i.second;
            --answer;
            if (cnt <= k)
            {
                if (cnt < k)
                    ++answer;
                break;
            }
        }
    }

    return answer;
}