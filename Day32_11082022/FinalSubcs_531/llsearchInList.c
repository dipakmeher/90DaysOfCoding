#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<string.h>
#include "linkedListheader.h"
/******** Start: search_In_list Function**********/
struct address_t *search_In_List(char paramAlias[11]){
    struct address_t *tempPtr = head;
    bool flagFound = false;

    while(tempPtr != NULL){
        if(!(strcmp(tempPtr->alias,paramAlias))){
            flagFound = true;
            return tempPtr;
        }else{
            tempPtr = tempPtr->next;
        }
    }
    return NULL;
}
/******** End: search_In_list Function**********/