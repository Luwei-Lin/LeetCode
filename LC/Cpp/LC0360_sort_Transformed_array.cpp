//sorted transformed array
#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

class Solution {
public:
    void process(vector<int> &nums, int L, int R){
        if ( L == R ) {
            return;
        }
        int M = L + ((R - L)>>1);

        process(nums, L, M);
        process(nums, M + 1, R);
        merge(nums, L, R, M);
    }
    void merge(vector<int> &nums, int L, int R, int M){
        vector<int> help (R - L + 1, 0);
        int p1 = M, p2 = M + 1;
        int index = 0;
        while (p1 <= M && p2 <= R){
            help[index++] = nums[p1] < nums[p2]? nums[p1++] : nums[p2++];
        }
        while (p1 <= M){
            help[index++] = nums[p1++];
        }
        while (p2 <= R){
            help[index++] = nums[p2++];
        }
        for (int i = 0; i < help.size(); i++){
            nums[L + i] = help[i];
        }
        return;
    }
    vector<int> sortTransformedArray(vector<int> &nums, int a, int b, int c) {
        for (int i = 0 ; i < nums.size(); i++) {
            //int x = nums[i];
            //nums[i] = a * x * x + b * x + c;
        }
        process(nums, 0, nums.size() - 1);
        return nums;
    }
};
int main(){
    Solution s;
    vector<int> nums;
    nums.push_back(-4);
    nums.push_back(-2);
    nums.push_back(2);
    nums.push_back(4);
    s.sortTransformedArray(nums, 1, 3, 5);
    for (int i = 0; i < nums.size(); i++) {
        printf("%d", nums[i]);
    }
}