#include <iostream>
#include <string>
using namespace std;
class Solution {
public:
    
    
    bool backspaceCompare(string s, string t) {
        //two pointers
        /*
        "ab##"
        | 
        "A#B#"
        |
        */
        int i = s.size() - 1, j = t.size() - 1;
        int skipS = 0, skipT = 0;
        // While there may be chars in build(S) or build (T)
        while (i >= 0 || j >= 0) {
            // Find position of next possible char in build(S)
            while(i >= 0) {
                if (s[i] == '#') { skipS++; i--; }
                else if (skipS > 0) {skipS--; i--; }
                else break;
            }
            // Find position of next possible char in build(T)
            while(j >= 0) {
                if (t[i] == '#') { skipT++; j--; }
                else if (skipT > 0) {skipT--; j--; }
                else break;
            }
            // If two actual characters are different
            if (i >= 0 && j >= 0 && s[i] != t[j])
                return false;
            // If expecting to compare char vs nothing
            if ((i >= 0) != (j >= 0))
                return false;
            i--; 
            j--;
        }
        return true;
    }
};
int main(){
    string s = "ab##";
    string t = "A#B#";
    Solution newSolution;
    cout << newSolution.backspaceCompare(s,t) <<endl;
    return 0;
}