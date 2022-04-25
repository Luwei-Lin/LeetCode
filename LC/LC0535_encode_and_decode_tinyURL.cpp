#include <iostream>
#include <map>
#include <stdio.h>
#include <time.h>


//#include <string>
using namespace std;

class Solution{
private:
    string alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    map<string, string> myMap;
    int count = 1;
    
public:
    string hashing(){
        string hashCode = "";
        int c = count;
        while (c > 0){
            c--;
            hashCode += alphabet.at(c % 62);
            c /= 62;
        }
        return hashCode;
    }
    string encode(string longUrl){
        string key = hashing();
        myMap.insert({key, longUrl});
        count++;
        string tinyUrl = "http://tinyurl.com/" ;
        
        return tinyUrl + key;
    }
    string decode(string shortUrl){
        string front = "http://tinyurl.com/";
        int size = front.size();
        string key = shortUrl.replace(shortUrl.begin(), shortUrl.begin() + size,  "");
        auto it = myMap.find(key);
        return it->second;
    }
};
int main(){
    string from = "https://leetcode.com/problems/design-tinyurl";
    string to = "https://leetcode.com/problems/design-tinyurl";
    Solution s;

    cout << from << endl;
    cout << s.encode(from) <<endl;
    
    string url = "https://leetcode.com/problems/design-tinyurl";
    cout<<s.decode(s.encode(url)) <<endl;
    return 0;
}