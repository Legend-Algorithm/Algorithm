import java.util.*;

public class Solution {

    // *2 만큼 순간이동
    // K칸 만큼 점프 건전지 K사용
    public int solution(int n) {
        // 그리디 문제 같음
        // N이 홀수라면 -1 해주고,
        // N이 짝수면 순간이동으로 2나누고,
        // 이과정이 0이 될때까지 진행

        int ans = 0;

        while(n > 0){
            if(n%2 ==1){ //홀수
                n--;
                ans++;
                continue;
            }
            n /= 2;
        }
        return ans;
    }
}