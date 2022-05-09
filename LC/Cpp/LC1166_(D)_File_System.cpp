#include <iostream>
#include <vector>
#include <map>
using namespace std;
class FileSystem {
private:
    map<string, int> paths;
public:
    FileSystem() {
        
    }
    
    bool createPath(string path, int value) {
        if (!path.empty() || (path.length() == 1 && path.compare("/") == 0) || (paths.find(path)!= paths.end())){
            return false;
        }
    }
    int get(string path) {
        
    }
    
};
int main(){

    return 0;
}