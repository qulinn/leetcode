// cf. Implementation example in Editorial
class Solution {
public:
    bool confusingNumber(int n) {
        unordered_map<char, char> invertMap = {{'0','0'}, {'1', '1'}, {'8','8'}, {'6','9'}, {'9','6'}};
        string rotatedNumber;

        // c++: to_string() -> python: str()
        for(auto ch : to_string(n)){
            if(invertMap.find(ch) == invertMap.end()){
                return false;
            }
            rotatedNumber += invertMap[ch];
        }

        reverse(begin(rotatedNumber), end(rotatedNumber));
        return stoi(rotatedNumber) != n;
    }
};