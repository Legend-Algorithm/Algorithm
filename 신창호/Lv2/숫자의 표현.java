class Solution {
    public int solution(int n) {
        //  n - 1 / 2  나머지가 없으면 가능
        //  n / 3
        //  n -2  / 4
        //  n / 5
        // n -3 / 6  0, 1, 2,3,4,5
        //
        // n - 5/10    -3, -2, -1, 0, 1,2,3 , 4,5,6
        int answer = 0;
        for(int i = 1; i <= n; i++){
            if(i%2 == 0){ // 짝수
                if((n - (i/2)) % i == 0 && ((n - (i/2)) / i) >= i/2 ){
                    answer++;
                }
            }
            else{// 홀수
                if(n%i == 0 &&  n/i > i/2){
                    answer++;
                }
            }
        }


        return answer;

    }
}