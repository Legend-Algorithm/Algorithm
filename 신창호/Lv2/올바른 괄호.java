
class Solution {
    boolean solution(String s) {

        boolean answer = true;
        // 하나씩 탐방, '(' 일경우와 ')' 일경우를 체크
        int openCnt = 0;
        for(int i = 0; i < s.length(); i++){
            if(openCnt < 0){
                answer = false;
                break;
            }
            if(s.charAt(i) == '('){
                openCnt++;
            }
            else{
                openCnt--;
            }

        }
        if(openCnt != 0) answer = false;
        return answer;
    }
}