import java.util.*;
class Solution {
    public int solution(int[] citations) {
        // 총길이 10^3
        // 원소 10^4 ,
        // 총길이가 10^3이기때문에, 10^3을 넘을 수가 없다.

        int max = citations.length;
        int cnt = 0;
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int c : citations){
            if(c > max) {
                cnt++;
                continue;
            }
            if(!map.containsKey(c)){
                map.put(c, 1);
                continue;
            }
            map.put(c, map.get(c) + 1);
        }

        int answer = 0;
        for(int i = max; i >= 0; i--){
            if(map.containsKey(i)){
                cnt += map.get(i);
            }
            if(i <= cnt){
                answer = i;
                break;
            }
        }

        return answer;
    }
}