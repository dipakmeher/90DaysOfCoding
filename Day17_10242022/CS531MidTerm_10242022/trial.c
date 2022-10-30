#include<stdio.h>
#include<string.h>
int main(void) {
 char s[] = "abcde";
 int len = strlen(s);
 for (int i = 0; i < len; i++)
 s[i] += 1;
 return printf("'%s' is %d characters long\n", s, len);
}