class Solution {
    public String solution(String s) {

        // 첫글자가 숫자인지 아닌지를 파악한다.
        // 숫자인 경우 그대로 진행하며, 영어인 경우 대문자로 만들어 준다.
        // 공백문자가 연속해서 나올 수 있다. split() 으로 해결하기 어려움
        boolean sw = true;
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < s.length(); i++) {

            if (s.charAt(i) == 32) {
                sw = true;
                sb.append((char) s.charAt(i));
                continue;
            }

            if (sw) { // 대문자 체크
                if (s.charAt(i) >= 97 && s.charAt(i) <= 122) {
                    sb.append((char) (s.charAt(i) - 32));
                } else {
                    sb.append((char) s.charAt(i));
                }
                sw = false;
            } else { // 소문자로 진행
                if (s.charAt(i) >= 65 && s.charAt(i) <= 90)
                    sb.append((char) (s.charAt(i) + 32));
                else {
                    sb.append((char) s.charAt(i));
                }
            }
        }
        return sb.toString();

    }

}