#include <stdio.h>
#include <stdlib.h>
#include "inverser.h"

int main() {
    int input_size = 100;
    char string[input_size];

    while (fgets(string, input_size, stdin) != NULL) {
        printf("%s", strrev(string));
    }

    return 0;
}