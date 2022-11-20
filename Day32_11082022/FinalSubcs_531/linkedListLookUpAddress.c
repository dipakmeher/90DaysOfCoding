#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<string.h>
#include "linkedListheader.h"
/******** Start: lookUp_Address_in_List() Function**********/
int lookUp_Address_in_List(){
    char newAlias[11];
    struct address_t *foundNode;
    foundNode = NULL;

    printf("Enter alias: ");
    scanf("%s", newAlias);
    foundNode = search_In_List(newAlias);
    if(foundNode!=NULL){
        printf("Address of alias %s: %d.%d.%d.%d\n", foundNode->alias, foundNode->octet[0], foundNode->octet[1], foundNode->octet[2], foundNode->octet[3]);
        return 0;
    }
    printf("\n>>Error: %s does not exist in list.\n", newAlias);
    return -1;
}
/******** End: lookUp_Address_in_List() Function**********/