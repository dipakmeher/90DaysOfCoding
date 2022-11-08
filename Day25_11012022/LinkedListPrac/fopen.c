#include<stdio.h>
#include<stdlib.h>

int main(){
    FILE *file_to_read = fopen("C:/Users/ME/Github/90DaysOfCoding/Day25_11012022/AssignmentLinkedListPrac/fopen.txt", "r");
    FILE *file_to_write = fopen("C:/Users/ME/Github/90DaysOfCoding/Day25_11012022/AssignmentLinkedListPrac/fopenwrite.txt", "w");
    
    if(file_to_read == NULL || file_to_write == NULL){
        printf("One file wouldn't open!\n");
        return -1;
    }

    char c;
    /*
    * fgetc reads one character at at time.
    */
    while((c=fgetc(file_to_read)) != EOF){
        if(c=='.'){
            c = '!';
        }
        fputc(c,file_to_write);
    }

    fclose(file_to_read);
    fclose(file_to_write);
    return 0;
}