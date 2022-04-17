#include <cstdio>
#include <iostream>

int haveCommonSUbstr(const char s1[], const char s2[]){
    int arr[26];
    for (int i = 0; i < 26; i++){
        arr[i] = 0;
    }
    //calucalte the element occurency
    
    for (int i = 0; i < sizeof(s1)/sizeof(s1[0]); i++){
        arr[s1[i] - 'a'] += 1;
    }

    for (int i = 0; i < sizeof(s2)/sizeof(s2[0]); i++){
        if (arr[s2[i] - 'a'] > 0){
            return 1;
        }
    }
    return 0;
}

int main(){
    const char s1[] = "hello";
    const char s2[] = "world";
    printf("%d\n", haveCommonSUbstr(s1, s2));
    return 0;
}