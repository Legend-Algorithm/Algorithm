import java.util.*;
class Solution {
    public int solution(int k, int[] tangerine) {
        // 해당 귤의 크기 갯수를 세기 위한 HashMap
        // 갯수가 많은 것부터 정렬하여, k에서 차감
        // k가 0이거나 0보다 작으면 종료

        HashMap<Integer, Integer> map = new HashMap<>();
        for(int t : tangerine){
            if(!map.containsKey(t)){
                map.put(t,1);
            }
            else{
                map.put(t, map.get(t)+1);
            }
        }
        // 값으로 정렬된 HashMap 생성
        LinkedHashMap<Integer, Integer> sortedMap = new LinkedHashMap<>();
        map.entrySet()
                .stream()
                .sorted(Map.Entry.comparingByValue(Comparator.reverseOrder()))
                .forEachOrdered(x -> sortedMap.put(x.getKey(), x.getValue()));
        int answer = 0;
        // 내림차순으로 정렬된 HashMap 출력
        for (Map.Entry<Integer, Integer> entry : sortedMap.entrySet()) {
            k -= entry.getValue();
            answer++;
            if(k <= 0){
                break;
            }
        }

        return answer;
    }
}