class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        // tp
        int n=matrix.size();
        for(int i=0;i<n;i++){
            for(int j=0;j<=i;j++){
                swap(matrix[i][j],matrix[j][i]);
            }
        }

        // reverse
        for(int i=0;i<n;i++){
            int j=0;
            int k=n-1;
            while(j<=n/2 && k>=n/2){
                swap(matrix[i][j],matrix[i][k]);
                j++;
                k--;
            }
        }
    }
};