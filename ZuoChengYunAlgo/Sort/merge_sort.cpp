#include <iostream>
#include <cstdio>

void print(int *arr, int size){
    if(arr == nullptr){
        return;
    }
    for (int i = 0; i < size; i++){
        printf("%d\n", arr[i]);
    }
}
void merge(int arr[], int L, int M, int R){
    int p1 = L, p2 = M + 1;
    int *help = new int[R - L + 1];
    int index = 0;
    while (p1 <= M && p2 <= R){
        if ( arr[p1] < arr[p2]) {
            help[index++] = arr[p2++];
        } else {
            help[index++] = arr[p1++];
        }
    }
    while (p1 <= M){
        help[index++] = arr[p1++];
    }
    while (p2 <= R){
        help[index++] = arr[p2++];
    }
    for (int i = 0; i < R - L + 1; i++){
        arr[L + i] = help[i];
    }
    delete [] help;
}

void process(int arr[], int L, int R){
    if ( L == R ){// minimum num is 1;
        return;
    }
    int mid = L + (( R - L) >> 1);
    process(arr, L, mid);
    process(arr, mid + 1, R);
    merge(arr, L, mid, R);
    return;
}

void mergeSortMain(){
    int A[]  = {5, 4, 1, 3, 2, 7};
    int L = 0, R = sizeof(A)/sizeof(A[0]) - 1; //size - 1;
    process(A, L, R);
    for (int i = 0; i < 6; i++) {
        printf("%d\n", A[i]);
    }
}

int mergeSum(int arr[], int L, int M, int R){
    int p1 = L, p2 = M + 1; 
    int index = 0;
    int res = 0;//sum
    int *help = new int[R - L + 1];

    while (p1 <= M && p2 <= R){
        //this line to decide how many elements less than current need to be populated and added. 
        res += arr[p1] < arr[p2] ? (R - p2 + 1) * arr[p1] : 0;

        help[index++] = arr[p1] < arr[p2] ? arr[p1++] : arr[p2++];
    }
    while (p1 <= M){
        help[index++] = arr[p1++];
    }
    while (p2 <= R){
        help[index++] = arr[p2++];
    }
    for (int i = 0; i< R - L + 1; i++){
        arr[L + i] = help[i];
    }
    delete [] help;
    return res;
}
int processSum(int arr[], int L, int R){
    if (L == R) {
        return 0;
    }
    int mid = L + ((R - L) >> 1);
    return processSum(arr, L, mid) + processSum(arr, mid + 1, R) + mergeSum(arr, L, mid, R);
}

void smallSumMain(){
    // left less than the a[i], and addup.
    // 0 + 0 + 0 + 1 + 1 + 15 = 17
    int A[]  = {5, 4, 1, 3, 2, 7};
    int size = sizeof(A)/sizeof(A[0]);
    int L = 0, R =  size - 1; //size - 1;
    printf("small sum: %d\n", processSum(A, L, R));
    print(A, size);
}

int main(){
    //mergeSortMain();
    smallSumMain();
    return 0;
}