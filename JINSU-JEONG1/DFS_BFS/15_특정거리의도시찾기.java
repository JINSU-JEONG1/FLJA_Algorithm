import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // StringTokenizer 는 공백단위로 분리가능 
        StringTokenizer st = new StringTokenizer(br.readLine());

        // N: 도시의 개수 (1번 ~ N번)
        int N = Integer.parseInt(st.nextToken());

        // M: 도로의 개수
        int M = Integer.parseInt(st.nextToken());

        // K: 찾고자 하는 최단 거리
        int K = Integer.parseInt(st.nextToken());

        // X: 시작 도시 번호
        int X = Integer.parseInt(st.nextToken());

        // 인접 리스트 사용
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i <= N; i++) {
            graph.add(new ArrayList<>());
        }

        // 도로 정보
        for(int i = 0; i < M; i++){
            st = new StringTokenizer(br.readLine());
            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            //
            graph.get(from).add(to);
        }

        // 거리 배열 초기화
        int[] dist = new int[N+1];
        Arrays.fill(dist, -1);

        // 큐사용
        Queue<Integer> queue = new LinkedList<>();
        // 시작점 방문처리
        queue.offer(x);
        dist[X] = 0; 

        while (!queue.isEmpty()) {
            int now = queue.poll();

            // 현재 거리가 K면 더 갈 필요 없음
            if (dist[now] == K) continue;

            for (int next : graph.get(now)) {
                // 방문 안했으면 현재 도시거리 + 1
                if (dist[next] == -1) {
                    dist[next] = dist[now] + 1;
                    queue.offer(next);
                }
            }
        }

        // 결과 출력
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= N; i++) {
            if (dist[i] == K) {
                sb.append(i).append('\n');
            }
        }
    }
}