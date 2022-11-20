#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<string.h>
#include "linkedListheader.h"
/******** Start: delete_From_List() Function**********/
int delete_From_List(){
    char enteredAlias[10];
    char consentDelete;
    struct address_t *delNode = NULL;
    printf("Enter alias: ");
    scanf("%s", enteredAlias);

    struct address_t *tempPtr = head;
    struct address_t *prevNode = NULL;

    while(tempPtr != NULL){
        if(!(strcmp(tempPtr->alias,enteredAlias))){
            delNode = tempPtr;
            break;
        }else{
            prevNode = tempPtr; 
            tempPtr = tempPtr->next;
        }
    }

    if (delNode == NULL)
    {
        printf("\n>>Error:%s does not exist.\n", enteredAlias);
        print_List();
        return -1;
    }
    else
    {
        printf("Delete %s %d.%d.%d.%d? (y/n) ", delNode->alias, delNode->octet[0], delNode->octet[1], delNode->octet[2], delNode->octet[3]);
        scanf("%s", &consentDelete);
        if(consentDelete == 'y'){
            if(prevNode!=NULL){
                prevNode->next = delNode->next;
            }

            //if head  =  del node
            if (!strcmp(delNode->alias, head->alias))
            {
                head = delNode->next;
            }
            printf("%s deleted\n", delNode->alias);
        }else{
            return 0;
        }
    }
    free(delNode);
    delNode = NULL;

    return 0;

}
/******** End: delete_From_List() Function**********/