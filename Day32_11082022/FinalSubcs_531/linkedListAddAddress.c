#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<string.h>
#include "linkedListheader.h"
/******** Start: add_address_to_list Function**********/
int add_address_to_list(){
    char newAlias[11], newAddr[15], newAddrAlias[26];
    int tempOctet[4];
    while(true){
        printf("Enter new ALIAS for your address-alias pair: ");
        scanf("%s",newAlias);

        if(strlen(newAlias) <= 10){
            if(search_In_List(newAlias)){
                printf("\n>>Error:%s already exists.", newAlias);
                return -1;
            }
 
            while(true){
                printf("Enter address for %s (Format: A1.A2.A3.A4): ", newAlias);
                scanf("%s", newAddr);
                sscanf(newAddr, "%d.%d.%d.%d", &tempOctet[0], &tempOctet[1], &tempOctet[2], &tempOctet[3]);

                struct address_t *traversePtr;
                traversePtr = head;
                while(traversePtr!=NULL){
                    if((tempOctet[0] == traversePtr->octet[0]) && (tempOctet[1] == traversePtr->octet[1]) && (tempOctet[2] == traversePtr->octet[2]) && (tempOctet[3] == traversePtr->octet[3])){
                        printf("Duplicate Address Found..!");
                        return 0;
                    }
                    traversePtr = traversePtr -> next;
                }

                if((tempOctet[0] >= 0 && tempOctet[0]<=255) && (tempOctet[1] >= 0 && tempOctet[1]<=255) && (tempOctet[2] >= 0 && tempOctet[2]<=255) && (tempOctet[3] >= 0 && tempOctet[3]<=255)){
                    snprintf(newAddrAlias,sizeof(newAddrAlias), "%s %s", newAddr, newAlias);
                    add_AddressNode_To_List(newAddrAlias);
                    return 0;
                }else{
                    printf("\n>>Error:%s is an illegal address - please reenter:\n", newAddr);
                }
            }
        }else{
            printf("\n>>Error: Alias length should be less than equal to 10\n");
        }
    }

}
/******** End: add_address_to_list Function**********/