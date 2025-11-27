class Solution {
    public int minDeletionSize(String[] strs) {

        int cols = strs[0].length();

        int c=0;

        for (int j = 0; j < cols; j++) {
            for (int i = 0; i < strs.length; i++) {
                if (i > 0) {  
                    if (strs[i].charAt(j) < strs[i - 1].charAt(j)) {
                        c+=1;
                        break;  
                    }
                }
            }
        }
        return c;
    }
}
