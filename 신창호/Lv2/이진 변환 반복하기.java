class Solution {
    public static int[] solution(String s) {
        int len = 0;
        int replaceLen = 0;
        int cnt = 0;
        int[] answer = new int[2];

        while (!s.equals("1")) {
            len = s.length();
            s = s.replaceAll("0", "");
            replaceLen = s.length();
            s =  Integer.toBinaryString(replaceLen);
            cnt = len - replaceLen;
            answer[0]++;
            answer[1] += cnt;

        }

        return answer;
    }

}