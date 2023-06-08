class Solution {
    public String solution(String s){
        // 문자열 이다.
        // 매번 최솟값과 최댓값을 확인해보자.
        String[] strArray = s.split(" ");
        int max = Integer.MIN_VALUE;
        int min =  Integer.MAX_VALUE;
        for(String str : strArray){
            int j = strtoInt(str);
            max = Math.max(max, j);
            min = Math.min(min, j);
        }


        String answer = min +" " + max;
        return answer;
    }

    private int strtoInt(String s){
        int a = Integer.parseInt(s);
        return a;
    }


}