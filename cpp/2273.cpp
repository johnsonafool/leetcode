class Solution {
public:
    vector<string> removeAnagrams(vector<string>& words) {
   
        for(int i = 0; i != words.size()-1; i++) {           
            string cur_word = words[i];
            string nex_word = words[i+1];             
            sort(cur_word.begin(), cur_word.end());
            sort(nex_word.begin(), nex_word.end());
            if (cur_word == nex_word) {
                words.erase(words.begin() + i+1);
                i--; // if not set index after erase will cause overflow
            }
        }

        return words;
    }
};