class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }

        unordered_map<char, int> ht;

        for (auto& sc : s) {          
            ht[sc]++;
        }

        for (auto& tc : t) {
            if (ht.find(tc) == ht.end() || ht[tc] == 0) {
                return false;
            }

            ht[tc]--;
        }

        return true;
    }
};