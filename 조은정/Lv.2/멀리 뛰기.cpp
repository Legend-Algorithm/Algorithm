#include <string>
#include <vector>
#include <map>
using namespace std;
typedef long long ll;

map<pair<int, int>, ll> mp;

ll combination(int u, int v)
{
    if (mp[{u, v}])
        return mp[{u, v}];

    if (u == v || v == 0)
        return 1;
    else
        return mp[{u, v}] = (combination(u - 1, v - 1) + combination(u - 1, v)) % 1234567;
}

ll solution(int n)
{
    ll answer = 0;

    for (int i = 0; i <= n / 2; ++i)
    { // 2칸 i개, 1칸 (n - i * 2)개
        answer = (answer + combination(n - i, i)) % 1234567;
    }

    return answer;
}