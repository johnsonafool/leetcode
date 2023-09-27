class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> output(2);
        unordered_map<int, int> ht;

        for (int i = 0; i < nums.size(); ++i) {
            // check if the value in hashtable
            // before add into
            if (ht.find(nums[i]) == ht.end()) {
                ht[target-nums[i]] = i;
            }

            else {
                int index = ht[nums[i]];
                output[0] = index;
                output[1] = i;
            }
        }

        return output;
    }
};