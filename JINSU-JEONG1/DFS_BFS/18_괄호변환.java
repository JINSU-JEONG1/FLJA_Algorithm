import java.util.*;

class Solution {
    public String solution(String p) {
        if(p.length() == 0) return "";
        return recursion(p);
    }
    
    // 재귀함수
    public String recursion(String s){
        if(s.length() == 0 ) return "";
        
        
        char[] arr = s.toCharArray();
        String u = "";
        String v = "";
        int cnt = 0;
        
        for(int i = 0; i < arr.length; i++){
            if(arr[i] == '(') cnt++;
            else cnt--;
            
            // 균형잡힌 문자열 일때
            if(cnt == 0){
                u = s.substring(0, i + 1);  // 0부터 i까지
                v = s.substring(i + 1);     // i+1부터 끝까지
                break;
            }
        }
        
        // u가 올바른 괄호 문자열이면
        if (isCorrect(u)) {
            return u + recursion(v);
        }
        
        // u가 올바르지 않으면 
        StringBuilder sb = new StringBuilder();
        sb.append('(')
          .append(recursion(v))
          .append(')')
          .append(flip(u));

        return sb.toString();
    }
    
    
    public boolean isCorrect(String s) {
        int cnt = 0;

        for (char c : s.toCharArray()) {
            if (c == '(') {
                cnt++;
            } else { // ')'
                cnt--;
                if (cnt < 0) {// 닫는 괄호가 먼저 나오면
                    return false; 
                }
            }
        }

        return cnt == 0;
    }
    
    // 4-4 로직
    private String flip(String u) {
        StringBuilder sb = new StringBuilder();

        // 첫/마지막 문자 제거
        for (int i = 1; i < u.length() - 1; i++) {
            char c = u.charAt(i);
            sb.append(c == '(' ? ')' : '(');
        }

        return sb.toString();
    }
    
}