#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<string.h>
#include "linkedListheader.h"
/******** Start: display_Alias_For_Location() Function**********/
void display_Alias_For_Location(){
    int tempOctet[2], countAddress=0;
    int flag = 0;
    while(countAddress<2){
        while(true){
            printf("Enter location value #%d (0-255): ", (countAddress + 1));
            scanf("%d", &tempOctet[countAddress]);
            if(tempOctet[countAddress] >= 0 && tempOctet[countAddress] <= 255){
                break;
            }
            printf("Error: %d is an illegal entry - please reenter",tempOctet[countAddress]);
        }
        countAddress++;
    }
    struct address_t *tempPtr = head;

    while(tempPtr != NULL){
        if((tempPtr->octet[0] == tempOctet[0]) && (tempPtr->octet[1] == tempOctet[1])){
            printf("The Alias for location %d.%d.%d.%d is %s\n", tempPtr->octet[0], tempPtr->octet[1], tempPtr->octet[2], tempPtr->octet[3], tempPtr->alias);
            flag = 1;
        }
        tempPtr = tempPtr->next;
    }
    if(flag == 0){
        printf("\n>>Entered Adresses doesn't exist - please reenter.\n");
    }
}
/******** End: display_Alias_For_Location() Function**********/