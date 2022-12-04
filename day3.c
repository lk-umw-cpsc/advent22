#include <stdio.h>
#include <string.h>

int score(long n) {
    return __builtin_ffsll(n);
}

int charToBitPosition(char c) {
    if (c <= 'Z') {
        return c - 'A' + 26;
    }
    return c - 'a';
}

long stringToSet(char *s, const int len) {
    long set = 0;
    for (int i = 0; i < len; i++) {
        set |= (long) 1 << charToBitPosition(s[i]);
    }
    return set;
}

int main(int argc, char **argv) {
    int p1score = 0;
    int p2score = 0;
    FILE *f = fopen("3.txt", "r");
    char buffer[256];
    int elf = 1;
    long p2set;
    while (fgets(buffer, 256, f)) {
        int len = strlen(buffer) & (~1); // unset bit 0 to ignore newline character if it exists
        int half =  len / 2;
        unsigned long setA = stringToSet(buffer, half);
        unsigned long setB = stringToSet(buffer + half, half);
        p1score += score(setA & setB);
        if (elf == 1) {
            p2set = stringToSet(buffer, len);
        } else {
            p2set &= stringToSet(buffer, len);
            if (elf == 3) {
                p2score += score(p2set);
            }
        }
        elf++;
        if (elf > 3) {
            elf = 1;
        }
    }
    printf("Part 1: %d\n", p1score);
    printf("Part 2: %d\n", p2score);
    fclose(f);
}