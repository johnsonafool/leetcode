// 167. Two Sum II - Input Array Is Sorted
// Medium
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int pl = 0;
        auto pr = numbers.size()-1;
        vector<int> ans;

        while (pl < pr) {
            if (numbers[pl]+numbers[pr] == target) {
                ans.push_back(pl+1);
                ans.push_back(pr+1);

                return ans;
            }

            else if (numbers[pl]+numbers[pr] > target) {
                pr--;
            }

            else {
                pl++;
            }
        }

        return ans;
    }
};