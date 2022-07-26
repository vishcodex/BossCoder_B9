class Solution {
    public int maxChunksToSorted(int[] arr) {
        
        int max=0, count=0;
        for(int i=0; i<arr.length; i++){
            System.out.println("max before :" + i + " " + max);
            max = Math.max(arr[i],max);
            System.out.println("max after :" + i + " " + max);
            if(i==max) count++;
        }return count;
    }
}