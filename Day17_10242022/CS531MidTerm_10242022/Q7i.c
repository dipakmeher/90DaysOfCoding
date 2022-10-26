// Midterm: Q7.
    // i) Identify three bugs in this function. [Total Points: 5]
	// char *reverse(char *input) {
    //  	       int len = strlen(input);
    //  	       char output[len];	
	//        for (int i = 0; i < len; i++) {
    //      		output[len - i - 1] = input[i];
    //   	      }
    //   	      return output;
    // 	}

// Refer: https://www.youtube.com/watch?v=E8Yh4dw6Diw
// Refer: https://stackoverflow.com/questions/19068643/dynamic-memory-allocation-for-pointer-arrays

// status: Incomplete

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
char *reverse(char*);

int main(){
    char* input = "Dipak";
    char* out = reverse(input);

    printf("Output= %c\n", *(out+5));
    return 0;
}
char *reverse(char *input) {
     	       int len = strlen(input);
     	       //char output[len];	
               char *output = malloc(sizeof(char*));

	       for (int i = 0; i < len; i++) {
         		output[len - i - 1] = input[i];
      	      }
      	      return output;
    	}