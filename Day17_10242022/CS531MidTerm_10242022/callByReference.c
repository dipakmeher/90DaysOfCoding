#include<stdio.h>  
void change(int *x) {    
    printf("Before adding value inside function x=%d \n",*x);    
    (*x) += 100;    
    printf("After adding value inside function x=%d \n", *x);    
}      
int main() {    
    int x=100;    
    printf("Before function call x=%d \n", x);    
    change(&x);//passing reference in function    
    printf("After function call x=%d \n", x);    
return 0;  
} 