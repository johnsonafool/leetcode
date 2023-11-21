class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> sol;
        vector<int> lp;
        vector<int> rp;
        lp.push_back(1);
        rp.push_back(1);

        for (int i=0; i < nums.size(); i++) {
            int cur_l = nums[i];
            int cur_r = nums[nums.size()-i-1];

            if (i-1 >= 0) {
                cur_l *= lp[i];
                cur_r *= rp[i];
            }

            lp.push_back(cur_l);
            rp.push_back(cur_r);           
        }

        reverse(rp.begin(), rp.end());

        for (int i=0; i < nums.size(); i++) {
            int tmp = lp[i]*rp[i+1];
            sol.push_back(tmp);
        }
        
        return sol;
    }
};
