class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> adam;
        unordered_map<char, int> carol;

        if(s.size() != t.size()) {
            return false;
        }

        for(int i = 0; i < s.size(); i++) {
            adam[s[i]] += 1;
            carol[t[i]] += 1;
        }

        for(int i = 0; i < s.size(); i++) {
            if(adam[s[i]] != carol[s[i]]) {
                return false;
            }
        }

        return true;
    }
    
};
