#include <iostream>
#include <cstdio>
void replaceSpaces(char *s, int length){
    if (s == nullptr || length <=0) {
        return;
    }
    int i = 0;
    int originalLength = 0;
    int numberOfBlank = 0;
    while (s[i] != '\0'){
        ++originalLength;

        if(s[i] == ' '){
            ++numberOfBlank;
        }
        ++i;
    }
    int newLength = originalLength + numberOfBlank * 2;
    if(newLength > length) 
        return;
    int indexOfOriginal = originalLength;
    int indexOfNew = newLength;
    while (indexOfOriginal >= 0 && indexOfNew > indexOfOriginal) {
        if (s[indexOfOriginal] == ' '){
            s[indexOfNew--] = '0';
            s[indexOfNew--] = '2';
            s[indexOfNew--] = '%';
        } else {
            s[indexOfNew--] = s[indexOfOriginal];//bug
        }
        --indexOfOriginal;
    }
}

int main (){
    char s[100] = "hi siri .";
    int len = 100;
    replaceSpaces(s, len);
    printf("%s\n", s);
    return 0;
}

