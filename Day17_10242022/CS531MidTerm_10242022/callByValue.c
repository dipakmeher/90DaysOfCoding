#include <stdio.h>  
void swapTheValues(int , int); //prototype of the function   
int main()  
{  
    int var1 = 10;  
    int var2 = 20;   

    // printing the value of a and b in main function
    printf("Before swapping, the values in main var1 = %d, var2 = %d\n",var1,var2);   

    //Swapping the values of var1 and var2
    swapTheValues(var1,var2);  

    // The value of actual parameters do not change by changing the formal parameters in call by value, var1 = 10, var2 = 20
    printf("After swapping, the values in main var1 = %d, var2 = %d\n",var1,var2);   
}  
void swapTheValues (int var1, int var2)  
{  
    int temp;   
    temp = var1;  
    var1=var2;  
    var2=temp;  

    // Formal parameters, var1 = 20, var2 = 10   
    printf("After swapping, the values in function var1 = %d, var2 = %d\n",var1,var2); 
}  