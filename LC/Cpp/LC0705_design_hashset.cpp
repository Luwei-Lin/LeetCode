#include <map>
#include <iostream>
using namespace std;

class MyHashSet {
private:
    map<int, int> myMap;
    map<int, int>::iterator it;
public:
    MyHashSet() {
        
    }
    
    void add(int key) {
        if(contains(key)) return;
        myMap.insert({key, 1});
    }
    
    void remove(int key) {
        if (!contains(key)) return;
        myMap.erase(key);
    }
    
    bool contains(int key) {
        it = myMap.find(key);
        if (it != myMap.end()){
            return true;
        }
        return false;
    }
};

int main(){
    MyHashSet* obj = new MyHashSet();
    int key = 1;
    obj->add(key);

    obj->remove(key);
    //bool param_3 = obj->contains(key);
    obj->add(2);
    obj->add(3);
    obj->add(4);
    obj->add(5);
    obj->add(6);
    cout << obj->contains(2) << endl;
    cout << obj->contains(3) << endl;
    cout << obj->contains(4) << endl;
    cout << obj->contains(5) << endl;
    cout << obj->contains(6) << endl;
    cout << obj->contains(1) << endl;

    
    return 0;
}