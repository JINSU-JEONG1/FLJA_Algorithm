import java.io.*;
import java.util.*;

class Solution {

    public static void main(String[] args) throws Exception {

        int[] arr = new int[]{-90, -71, -21, -4, 0, 4, 5, 7, 11, 15, 26, 45, 67};

        int start = 0;
        int end = arr.length - 1;
        System.out.println("Fixed point: " + binarySearch(arr, start, end));

    }


    public static int binarySearch(int[] arr, int start, int end){

        if(start > end) return -1;

        while(start <= end){
            int mid = (start + end) / 2;

            if(arr[mid] > mid){
                // 값이 인덱스보다 크면 왼쪽으로
                end = mid - 1;
                continue;
            }

            if(arr[mid] < mid){
                // 값이 인덱스보다 작으면 오른쪽으로
                start = mid + 1;
                continue;
            }

            if(arr[mid] == mid){
                return mid;
            }
        }
        return -1;
    }
}