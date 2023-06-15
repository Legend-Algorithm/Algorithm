class Solution {
    public long solution(int n) {
        // 1칸, 2칸 - >DP 문제
        long[] dp = new long[n+1];

        if(n >= 1) dp[1] = 1L ;
        if(n >= 2) dp[2] = 2L;
        for(int i = 3; i<= n; i++){
            dp[i] = (dp[i-1] + dp[i-2])%1234567;
        }

        long answer = dp[n];
        return answer;
    }
}