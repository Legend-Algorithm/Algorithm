#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<int> A, vector<int> B)
{
    int answer = 0, sz = A.size();
    sort(A.begin(), A.end());
    sort(B.begin(), B.end());
    for (int i = 0; i < sz; ++i)
        answer += A[i] * B[sz - 1 - i];
    return answer;
}