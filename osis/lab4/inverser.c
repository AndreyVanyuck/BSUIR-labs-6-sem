#include "inverser.h"

char *strrev(char *src){
    int i, srcLen = 0;
    char temp;
    srcLen = strlen(src) - 1;
    for(i = 0; i < strlen(src)/2; i++){
        temp = src[i];
        src[i] = src[srcLen];
        src[srcLen--] = temp;
    }
    return src;
}