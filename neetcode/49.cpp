class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> sol;        
        unordered_map<string, vector<string>> ht;
        for (auto& s: strs) {
            string tmp = s;
            sort(tmp.begin(), tmp.end());
            ht[tmp].push_back(s);
        }          

        for (auto& h: ht) {
            sol.push_back(h.second);
        }

        return sol;
    }
};