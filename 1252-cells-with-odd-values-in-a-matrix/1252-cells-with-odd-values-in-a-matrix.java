class Solution {
    public int oddCells(int m, int n, int[][] indices) {

        int[][] arr = new int[m][n];

        int l = indices.length;   // number of row/col operations

        // Your approach: manually process each index
        for (int p = 0; p < l; p++) {

            int r1 = indices[p][0];   // row to increment
            int c1 = indices[p][1];   // column to increment

            // increment all cells in row r1
            for (int j = 0; j < n; j++) {
                arr[r1][j]++;
            }

            // increment all cells in column c1
            for (int i = 0; i < m; i++) {
                arr[i][c1]++;
            }
        }

        // Count odd cells
        int count = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (arr[i][j] % 2 != 0) {
                    count++;
                }
            }
        }

        return count;
    }
}
