#include <stdlib.h>
#include <stdio.h>

int log2(unsigned long n) {
    n |= (n >> 1);
    n |= (n >> 2);
    n |= (n >> 4);
    n |= (n >> 8);
    n |= (n >> 16);
    n |= (n >> 32);
    return n - (n >> 1);
}

int charToBitPosition(char c) {
    if (c <= 'Z') {
        return c - 'A' + 26;
    }
    return c - 'a';
}

unsigned long stringToSet(char *s, const int len) {
    unsigned long set = 0;
    for (int i = 0; i < len; i++) {
        set |= 1 << charToBitPosition(s[i]);
    }
    return set;
}

