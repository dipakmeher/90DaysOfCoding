#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<string.h>
#include "linkedListheader.h"
/******** Start: update_In_List() Function**********/
int update_In_List(){
    char newAlias[11], tempOctet[4];
    int countAddress = 0;

    struct address_t *foundNode = NULL; 

    printf("Enter alias: ");
    scanf("%s", newAlias);
    foundNode = search_In_List(newAlias);
    if(foundNode!=NULL){
        printf("Update address for %s: %d.%d.%d.%d\n", foundNode->alias, foundNode->octet[0], foundNode->octet[1], foundNode->octet[2], foundNode->octet[3]);
        while(countAddress < 4){
            printf("Enter address %d (0-255): ", (countAddress+1));
            scanf("%d", &tempOctet[countAddress]);
            if(!(tempOctet[countAddress]>=0 && tempOctet[countAddress]<=255)){
                printf("error:%d is an illegal entry - please reenter in range 0 to 255:\n", tempOctet[countAddress]);
                continue;
            }
            countAddress++;
        }
        if(tempOctet[0] == foundNode->octet[0] && tempOctet[1] == foundNode->octet[1] && tempOctet[2] == foundNode->octet[2] && tempOctet[3] == foundNode->octet[3]){
            printf("Error: duplicate address found.");
            return -1;
        }
        for (int i = 0; i < 4; i++)
        {
            foundNode->octet[i] = tempOctet[i];
        }
        return 0;
    }else{
        return -1;
    }
}
/******** End: update_In_List() Function**********/