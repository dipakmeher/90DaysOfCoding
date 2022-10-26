// // Midterm True and False: typedef char * mystring;
//  	mystring s201 = "201"; 
// 	mystring s202 = s201;
// 	s202[2] += 1;
// A novice programmer writes the above code. What do you think the programmer is intending to do and what two problems might he/she suffer? [3 points] 
// status: Incomplete

#include<stdio.h>
int main(){
    typedef char *mystring;
 	mystring s201 = "201"; 
	mystring s202 = s201;

    printf("s201= %s\n", s201);
    printf("s201= %p\n", &s201);
    printf("s201= %p\n", &s201[0]);
    printf("s201= %p\n", (void *)&s201[1]);
    printf("s201= %p\n", (void *)&s201[2]);
    printf("s202= %p\n", (void *)&s202);
    printf("Use pointer for printing= %c\n", s202[2] + 1);
	//s202[2] += 1; // Tring to access \0 thats why it is a error. With this code, the attempt to change the address of s[202] is done, which is not possible. 
    printf("s202[2]+1 = %s\n", s202[2]);

    return 0;
}