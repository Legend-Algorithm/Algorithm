import java.util.*;
class Solution {
    public int solution(String s) {
        // 완전탐색 10^3
        // []
        int answer = 0;
        Stack<Character> stack;
        boolean check;
        int index;
        for(int start = 0;start < s.length(); start++){
            stack = new Stack<>();
            index = 0;
            check = true;
            while(index < s.length()){
                int l = start+index;
                if(l >= s.length()){
                    l -= s.length();
                }
                Character c= s.charAt(l);
                index++;
                if(c == '[' ||c == '{' || c == '(' ){
                    stack.add(c);
                }
                if(c == ']'){
                    if(!stack.isEmpty() && stack.peek() == '['){
                        stack.pop();
                        continue;
                    }
                    check = false;
                    index = s.length(); // 종료
                }
                if(c == '}'){
                    if(!stack.isEmpty() && stack.peek() == '{'){
                        stack.pop();
                        continue;
                    }
                    check = false;
                    index = s.length(); // 종료
                }
                if(c == ')'){
                    if(!stack.isEmpty() && stack.peek() == '('){
                        stack.pop();
                        continue;
                    }
                    check = false;
                    index = s.length(); // 종료
                }


            }
            if(stack.isEmpty() && check){
                answer++;
            }
        }
        return answer;
    }
}