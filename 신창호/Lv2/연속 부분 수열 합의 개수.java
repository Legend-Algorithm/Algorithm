import java.util.*;
class Solution {
    public int solution(int[] elements) {
        //  수열에서 나온 결과값 set으로 정리
        // 길이의 경우의 수 1~elements길이 만큼 계산 가능
        int num;
        Set<Integer> set = new HashSet<>();
        for(int l = 0; l < elements.length; l++){ // 길이
            for(int start = 0; start < elements.length; start++){ // 시작지점
                num = sum(start, start+l, elements);
                if(set.contains(num))continue;
                set.add(num);
            }
        }
        int answer = set.size();
        return answer;
    }


    private int sum(int start, int end, int[] elements){
        int sum = 0;
        int index;
        while(start <= end){
            index = start;
            if(start >= elements.length){
                index -= elements.length;
            }
            sum += elements[index];
            start++;
        }
        return sum;
    }


}