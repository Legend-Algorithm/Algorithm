class Solution {
    public int solution(int[] arr) {
        // 두개씩 최소공배수를 구해간다.
        // 최소공배수 공식은  a *b/a,b의 최대공약수

        if(arr.length == 1) return arr[0];
        int answer = arr[0];
        for(int i = 1; i< arr.length; i++){
            int gcb = maxdivide(answer, arr[i]);
            answer = (answer * arr[i]) / gcb;
        }

        return answer;
    }
    private int maxdivide(int a, int b){
        int tmp = a;
        if(a < b){
            tmp = a;
            a = b;
            b = tmp;
        }
        while(b!=0){
            tmp = a%b;
            a = b;
            b = tmp;
        }
        return a;
    }


}