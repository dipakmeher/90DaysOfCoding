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
// Refer: https://stackoverflow.com/questions/22709997/allocating-memory-for-one-dimensional-array-in-c

// status: Incomplete

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
char *reverse(char*);

int main(){
    char* input = "Dipak";
    char* out = reverse(input);

    printf("Output= %s\n", out);
    return 0;
}
char* reverse(char *input) {
     	       int len = strlen(input);
               printf("len: %d\n",len);
     	       //char output[len];	
               char *output = (char*)malloc(sizeof(char*));

	       for (int i = 0; i < len; i++) {
         		output[len - i - 1] = input[i];
      	      }
              output[len] = '\0';
      	      return output;
    	}   

// void *reverse(char *input) {
//      	       int len = strlen(input);
//      	       char output[len];	
// 	       for (int i = 0; i < len; i++) {
//          		output[len - i - 1] = input[i];
//       	      }
//       	      printf("%c", output[0]);
//     	}