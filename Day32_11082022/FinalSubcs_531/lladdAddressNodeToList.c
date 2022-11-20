#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<string.h>
#include "linkedListheader.h"

/******** Start: add_Address Function**********/
int add_AddressNode_To_List(char paramString[26])
{
    if(head == NULL){
        create_list(paramString);
        return 0;
    }
    struct address_t *addNode = (struct address_t *)malloc(sizeof(struct address_t));

    if(NULL == addNode){
        printf("Error while memory allocation to new node");
        return -1;
    }

    sscanf(paramString, "%d.%d.%d.%d %s", &addNode->octet[0], &addNode->octet[1], &addNode->octet[2], &addNode->octet[3], &addNode->alias);
    addNode->next = NULL;

    currNode->next = addNode;
    currNode = addNode;
    return 0;  
}
/******** End: add_Address Function**********/