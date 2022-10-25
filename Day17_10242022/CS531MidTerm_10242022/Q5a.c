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

    printf("s201= %c\n", s201[2]);
    printf("s202= %s\n", s202);
	s202[2] += 1; // Tring to access \0 thats why it is a error
    printf("s202[2]+1 = %s", s202[2]);

    return 0;
}