import java.util.Arrays;
import java.util.stream.Stream;

class Solution {

  public String solution(String s) {
    String words[] = s.split(" ");

    int[] values = Stream.of(words)
        .mapToInt(Integer::parseInt)
        .toArray();

    int max = Arrays.stream(values).max().getAsInt();
    int min = Arrays.stream(values).min().getAsInt();

    return min + " " + max;
  }
}