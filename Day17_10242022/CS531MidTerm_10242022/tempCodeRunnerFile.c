char *reverse(char *input) {
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