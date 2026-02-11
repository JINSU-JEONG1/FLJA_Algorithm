import java.io.*;
import java.util.*;

class Main {
    public void solution(){

        int answer = 0;
        int cnt = 0;

        int[] array = new int[]{1,1,2,2,2,2,2,2,2,3,3,3,4,4,4,4,5,5,5,5,5,5,6,6,7,8,9,9};

        int start = 0;
        int end = array.length - 1;

        int x = 2;

        int xIdx = binarySearch(array, start, end, x);

        System.out.println("target == " + x);

        for(int i = xIdx; i < array.length; i++){
            if(array[i] == x){
                cnt++;
            }else{
                break;
            }
        }

        for(int i = xIdx - 1; i >= 0; i--){
            if(array[i] == x){
                cnt++;
            }else{
                break;
            }
        }

    }

    public int binarySearch(int[] array, int start, int end, int x){
        
        int mid = (start + end)/2;

        while(start <= end){

            if(array[mid] > x){
                end = mid -1;
                mid = (start + end)/2;
                continue;
            }
            if(array[mid] < x){
                start = mid + 1;
                mid = (start + end)/2;
                continue;
            }

            if(array[mid] == x) return mid;

        }
        return -1;
    }
}