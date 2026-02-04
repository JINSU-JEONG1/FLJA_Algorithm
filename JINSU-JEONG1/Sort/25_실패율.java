import java.util.*;

class Solution {
    public int[] solution(int N, int[] stages) {
        int[] answer = new int[N];
        double[] failPercent = new double[N];
        boolean[] calculated = new boolean[N];

        Arrays.sort(stages);

        // 예외: stages 비어있는 경우
        if (stages.length == 0) {
            for (int i = 0; i < N; i++) answer[i] = i + 1;
            return answer;
        }

        int current = stages[0];          // 현재 스테이지
        int numerators = stages.length;   // 도전자 수
        int denominators = 0;             // 실패자 수

        for (int i = 0; i < stages.length; i++) {

            // 스테이지 변경 시
            if (stages[i] > current) {
                // 이전 스테이지 실패율 계산
                if (current <= N) {
                    double percent = (double) denominators / numerators;
                    failPercent[current - 1] = percent;
                    calculated[current - 1] = true;
                }

                // 다음 스테이지로 이동
                numerators -= denominators;
                denominators = 1;
                current = stages[i];
            } else {
                // 동일 스테이지 실패자 수 증가
                denominators++;
            }

            // 마지막 index 처리
            if (i == stages.length - 1) {
                if (current <= N) {
                    double percent = (double) denominators / numerators;
                    failPercent[current - 1] = percent;
                    calculated[current - 1] = true;
                }
            }
        }

        // 등장하지 않은 스테이지 실패율 = 0
        for (int i = 0; i < N; i++) {
            if (!calculated[i]) {
                failPercent[i] = 0.0;
            }
        }

        // index 정렬
        Integer[] idx = new Integer[N];
        for (int i = 0; i < N; i++) idx[i] = i;

        Arrays.sort(idx, (i, j) -> {
            int cmp = Double.compare(failPercent[j], failPercent[i]);
            if (cmp != 0) return cmp;
            return Integer.compare(i, j);
        });

        for (int i = 0; i < N; i++) {
            answer[i] = idx[i] + 1;
        }

        return answer;
    }
}


// 정답 버전
/*
class Solution {
    public int[] solution(int N, int[] stages) {
        int[] answer = new int[N];

        // 각 스테이지에 머무른 사람 수
        int[] count = new int[N + 2];
        for (int s : stages) {
            count[s]++;
        }

        double[] failRate = new double[N];
        int total = stages.length; // 해당 스테이지 이상에 도달한 사람 수

        for (int stage = 1; stage <= N; stage++) {
            if (total == 0) {
                failRate[stage - 1] = 0;
            } else {
                failRate[stage - 1] = (double) count[stage] / total;
            }
            total -= count[stage];
        }

        Integer[] idx = new Integer[N];
        for (int i = 0; i < N; i++) idx[i] = i;

        Arrays.sort(idx, (i, j) -> {
            int cmp = Double.compare(failRate[j], failRate[i]); // 실패율 내림차순
            if (cmp != 0) return cmp;
            return Integer.compare(i, j); // 스테이지 번호 오름차순
        });

        for (int i = 0; i < N; i++) {
            answer[i] = idx[i] + 1;
        }

        return answer;
    }
}
 */