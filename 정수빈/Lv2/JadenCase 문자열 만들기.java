import java.util.*;

class Solution {

  public String solution(String s) {
    String words[] = s.split(" ");
    String answer = "";

    for (int i = 0; i < words.length; i++) {
      String word = words[i];

      words[i] =
          word.substring(0, 1).toUpperCase() + word.substring(1, word.length()).toLowerCase();
    }

    for (int i = 0; i < words.length; i++) {
      String str = words[i];
      if (i == words.length - 1) {
        answer += str;
      } else {
        answer += str + " ";
      }
    }
    return answer;
  }
}