public static int binarySearch(int n, int[] arr){
    int left=0;
    int right=arr.length-1;
    int idx=0;

    while (left<=right){
        idx=(left+right)/2;
        if (arr[idx]==n) {
            return idx;
        }
        else if (arr[idx]<n) {
            left=idx+1;
        }
        else{
            right=idx-1;
        }
    }

    return idx;
}