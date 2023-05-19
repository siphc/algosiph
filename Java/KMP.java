import java.util.Arrays;

// ignore lines 2-6, they only exist to debug
public class KMP{
    public static void main(String[] args) {
        System.out.println(Arrays.toString(kmp("abcdabca")));
        System.out.println(Arrays.toString(kmp("abaaabab")));
    }

    // method kmp() is the actual code.
    public static int[] kmp(String s){
        int n = s.length();
        int[] ar = new int[n];
        
        for (int i = 1; i < n; i++) {
            if (s.charAt(i) == s.charAt(ar[i-1])) {
                ar[i] = ar[i-1] + 1;
                continue; // leaving this here saves O(n) runtime, lol
            }
            if (ar[i-1] > 0) {
                int j = ar[ar[i-1]-1]; // j is just recursive ar[i-1]
                while (ar[i] == 0) {
                    if (s.charAt(i) == s.charAt(j)) {
                        ar[i] = j + 1;
                        break; // so it doesnt oobe at l36
                    }
                    else if (j == 0) { // smallest value of j possible. ar[i] would either be 0 or 1
                        if (s.charAt(0) == s.charAt(i)) {
                            ar[i] = 1;
                        }
                        else {
                            break;
                        }
                    }
                    j = ar[j-1];
                }
            }
        }
        return ar; // ok start praying that this works
    }

    // thanks https://cp-algorithms.com/string/prefix-function.html i would never write such a good implementation on god
    public static int[] _kmp(String s) {
        int n = s.length();
        int[] ar = new int[n];

        for (int i = 1; i < n; i++) {
            int j = ar[i-1];
            while (j>0 && s.charAt(i)!=s.charAt(j)) {
                j = ar[j-1];
            }
            if (s.charAt(i) == s.charAt(j)) {
                j++;
            }
            ar[i] = j;
        }
        return ar;
    }
}