#include <stdio.h>

#define BUFFER_SIZE 4096

typedef unsigned char bool;
#define true 1
#define false 0

bool isUnique(char *s, const int length) {
    unsigned int found = 0;
    for (int i = 0; i < length; i++) {
         // s[i] - 'a' gets us the 'index' of the bit we want.
         // we then shift 1 to the left that many times
         // to produce the bit mask for that bit
        int bit = 1 << (s[i] - 'a');
        // if the bit is already set, this string is not unique
        // (we have a repeat)
        if (found & bit) {
            return false;
        }
        found |= bit;
    }
    return true;
}

int main(int argc, char **argv) {
    FILE *f = fopen("6.txt", "r");
    char buffer[BUFFER_SIZE];
    int length = fread(buffer, 1, BUFFER_SIZE, f);
    fclose(f);
    char *p = buffer;
    length -= 4;
    int i;
    for (i = 0; i < length; i++, p++) {
        if (isUnique(p, 4)) {
            printf("Part 1: %d\n", i + 4);
            break;
        }
    }
    length -= 10;
    for (; i < length; i++, p++) {
        if (isUnique(p, 14)) {
            printf("Part 2: %d\n", i + 14);
            break;
        }
    }
}