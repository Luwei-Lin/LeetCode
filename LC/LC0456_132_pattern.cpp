#include <stack>
#include <vector>
#include <iostream>
using namespace std;

bool find132pattern_01(vector<int>& nums){
    int min_i = nums[0];
    for (size_t j = 0; j < nums.size(); j++) {
        min_i = min(min_i, nums[j]);
        for (size_t k = j + 1; k < nums.size(); k++) {
            if (nums[k] < nums[j] and min_i < nums[k]){ return true; }
        }
    }
    return false;
}
bool find132pattern_02(vector<int>& nums){
    stack<int> si;
    vector<int> mins(nums.size());
    mins[0] = nums[0];
    cout << "mins [";
    for (size_t i = 1; i < nums.size(); i++) {
        mins[i] = min(mins[i - 1], nums[i]);
        cout << mins[i] << " ";
    }
    cout << "]"<<endl;

    for (size_t j = nums.size() - 1; j >= 0; j--){
        //build mono stack
        while (!si.empty() && si.top() < nums[j]){
            if (si.top() > mins[j]){
                return true;
            }
            si.pop();
        }
        si.push(nums[j]);
    }
    return false;

}

int main(){
    vector<int> nums = {6, 12, 3, 4, 6, 11, 20};
    cout << find132pattern_01(nums) << endl;
    cout << find132pattern_02(nums) << endl;
    return 0;
}