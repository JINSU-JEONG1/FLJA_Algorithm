import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(st.nextToken());
        System.out.println(n);

        // 테스트 케이스
        int t = Integer.parseInt(br.readLine());

        // N 명 받아서 객체 리스트에 저장
        List<people> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {4
            st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            int kor = Integer.parseInt(st.nextToken());
            int eng = Integer.parseInt(st.nextToken());
            int math = Integer.parseInt(st.nextToken());
            list.add(new people(name, kor, eng, math));
        }

        Collections.sort(list, new Comparator<people>() {
            @Override
            public int compare(people o1, people o2) {
                if (o1.kor != o2.kor) {
                    return o2.kor - o1.kor; // 1.국어점수가 감소하는순서
                } else if (o1.eng != o2.eng) {
                    return o1.eng - o2.eng; // 2.국어점수가 같으면 영어점수가 증가하는순서
                } else if (o1.math != o2.math) {
                    return o2.math - o1.math; // 3.국어점수와 영어점수가 같으면 수학점수가 감소하는순서
                } else {
                    return o1.name.compareTo(o2.name); // 4.모든점수가 같으면 이름이 사전순으로 증가하는순서
                }
            }
        });

        // 정렬 후 출력
        for (people p : list) {
            System.out.println(p.name);
        }
    }
}

private class people {
    String name;
    int kor;
    int eng;
    int math;
    
    public people(String name, int kor, int eng, int math) {
        this.name = name;
        this.kor = kor;
        this.eng = eng;
        this.math = math;
    }
}