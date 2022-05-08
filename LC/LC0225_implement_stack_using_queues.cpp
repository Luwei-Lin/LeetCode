#include <iostream>
#include <queue>
using namespace std;
class MyStack {
private:
    queue <int> q;
public:
    MyStack() {
    }
    void push(int x) {
        q.push(x);
        int n = q.size();
        while (n > 1) {
            q.push(q.front());
            q.pop();
            n--;
        }
    }
    int pop() {
        int value = top();
        q.pop();
        return value;
    }
    int top() {
        return q.front();
    }
    bool empty() {
        return q.empty();
    }
};
int main(){
    MyStack s;
    s.push(1);
    s.push(2);
    s.push(3);

    cout << s.pop() << endl;
    cout << s.pop() << endl;
    cout << s.pop() << endl;
    cout << s.top() << endl;

    return 0;
}