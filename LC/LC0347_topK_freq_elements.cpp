#include <iostream>
#include <vector>
#include <cassert>
#include <algorithm>
#include <map>
#include <queue>
using namespace std;

class Solution{
public:
    vector<int> topKFrrquent(vector<int>& nums, int k){
        if (k == nums.size()){
            
            return nums;
        }
        //1. build hashmap: element and frequence
        map<int, int> count_map;
        for(int n: nums){
            count_map[n]++;
        }
        //2. keep k top frequent elements in the heap (Max heap)
        auto comp = [&count_map](int n1, int n2) {
            return count_map[n1] >count_map[n2];};
        priority_queue<int, vector<int>, decltype(comp)> heap(comp);

        //3. keep k top frequent elements in the heap
        for(pair<int, int> p: count_map){        
            heap.push(p.first);
            if(heap.size() > k) heap.pop();
        }
        //4. build an output array
        vector<int> top(k);
        for (int i = k - 1; i >= 0; i--){
            top[i] = heap.top();
            heap.pop();
        }
        return top;
    }
};

int main(){
    vector<int> v;
    v = {1, 1, 1, 2, 2, 5, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3};
    int k = 2;

    Solution s;
    vector<int> res = s.topKFrrquent(v, k);
    for(auto &x: res){
        cout << x<< " ";
    }
    return 0;
}