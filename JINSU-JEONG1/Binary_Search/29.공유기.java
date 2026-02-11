import java.io.*;
import java.util.*;

class Solution {

    public static void main(String[] args) throws Exception {

        // N : 집 개수
        // C : 공유기 개수
        // 가장 인접한 두 공유기 사이의 최대 거리를 출력
        // - 경계값 문제
        // start 일단 하나 설치
        // start 부터 가능한 최대거리 찾음


        int[] arr = new int[]{1, 2, 8, 4, 9, 3, 13, 15, 20, 23, 25, 11, 30};

        int N = 13;
        int C = 4;

        Arrays.sort(arr);

        int start = 1;
        int end = arr[N - 1] - arr[0];
        int answer = 0;

        while (start <= end) {
            int mid = (start + end) / 2;

            if (canInstall(arr, C, mid)) {
                answer = mid;
                start = mid + 1;     // 더 큰 최소 거리 도전
            } else {
                end = mid - 1;
            }
        }

    }


    private static boolean canInstall(int[] arr, int C, int mid) {
        int cnt = 1;
        int last = arr[0];

        for (int i = 1; i < arr.length; i++) {
            if (arr[i] - last >= mid) {
                cnt++;
                last = arr[i];
            }
        }

        return cnt >= C;
    }
}