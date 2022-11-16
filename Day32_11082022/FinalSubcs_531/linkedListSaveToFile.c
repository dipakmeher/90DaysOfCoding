#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<string.h>
#include "linkedListheader.h"
/******** Start: save_To_File Function**********/
int save_To_File(){
    char fileName[20];
    struct address_t *tempPtr = head;

    printf("Enter filename: ");
    scanf("%s",fileName);
    strcat(fileName, ".txt");

    FILE *filePtr = fopen(fileName, "w");
    if(filePtr == NULL){
        printf("\n>>Error opening File");
        return -1;
    } 
    tempPtr = head;
    while(tempPtr != NULL){
        fprintf(filePtr, "%d.%d.%d.%d %s\n", tempPtr->octet[0], tempPtr->octet[1], tempPtr->octet[2], tempPtr->octet[3], tempPtr->alias);
        tempPtr = tempPtr->next;
    }
    printf("File Saved.");
    fclose(filePtr);
    return 0;

}
/******** End: save_To_File Function**********/