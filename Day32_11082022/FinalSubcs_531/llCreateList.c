#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<string.h>
#include "linkedListheader.h"
/******** Start: create_New_list Function**********/
int create_list(char paramString[26])
{
    struct address_t *newNode = (struct address_t *)malloc(sizeof(struct address_t));
    if(NULL == newNode){
        printf("Error while memory allocation to new node");
        return -1;
    }

    sscanf(paramString, "%d.%d.%d.%d %s", &newNode->octet[0], &newNode->octet[1], &newNode->octet[2], &newNode->octet[3], &newNode->alias);
    newNode->next = NULL;

    // Inserting the node in beginning
    head = newNode;
    currNode = newNode;
    return 0;
}
/******** End: create_New_list Function**********/