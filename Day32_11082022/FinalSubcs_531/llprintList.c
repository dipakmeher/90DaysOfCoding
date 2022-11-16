#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<string.h>
#include "linkedListheader.h"
/******** Start: print_List() Function**********/
void print_List(){
    struct address_t *printPtr = head;

    while (printPtr != NULL)
    {
        printf("%d.%d.%d.%d %s\n", printPtr->octet[0], printPtr->octet[1], printPtr->octet[2], printPtr->octet[3], printPtr->alias);
        printPtr = printPtr->next;
    }
    return; 

}
/******** End: print_List() Function**********/