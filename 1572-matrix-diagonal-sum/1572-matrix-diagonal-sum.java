class Solution {
    public int diagonalSum(int[][] mat) {
        Set<String> set = new HashSet<>();
        int sum=0;
        int n = mat.length;
        for(int i=0;i<n;i++){
            String p= i +"_"+i;
            if(!set.contains(p)){
                sum+=mat[i][i];
                set.add(p);
            }

            int j=n-i-1;
            String s= i+"_"+j;

            if(!set.contains(s)){
                sum+=mat[i][j];
                set.add(s);
            }
        }
        return sum;

        
    }
}