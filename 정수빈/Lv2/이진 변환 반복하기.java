import java.util.*;

class Solution {

  public int[] solution(String s) {
    int[] answer = {0, 0};
    int cnt = 0;
    int zero = 0;
    String[] temp = {s};

    while (!temp[0].equals("10") && !temp[0].equals("1")) {

      cnt++;

      zero += temp[0].chars().filter(ch -> ch == '0').count();
      temp[0] = temp[0].replaceAll("0", "");

      String binary = Integer.toBinaryString(temp[0].length());
      temp[0] = binary;

    }

    if (temp[0].equals("10")) {
      zero++;
      cnt++;
    }
    ;

    answer[0] = cnt;
    answer[1] = zero;

    return answer;
  }
}