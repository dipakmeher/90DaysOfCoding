#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<string.h>

struct address_t{
    int octet[4];
    char alias[11];
    struct addresss_t *next;
};
struct address_t *head = NULL;
struct address_t *currNode = NULL;

/******** Start: add_Address Function**********/
struct address_t *add_AddressNode_To_List(char paramString[26])
{
    if(head == NULL){
        return (create_list(paramString));
    }

    struct address_t *addNode = (struct address_t *)malloc(sizeof(struct address_t));

    if(NULL == addNode){
        printf("Error while memory allocation to new node");
        return NULL;
    }

    sscanf(paramString, "%d.%d.%d.%d %s", &addNode->octet[0], &addNode->octet[1], &addNode->octet[2], &addNode->octet[3], &addNode->alias);
    addNode->next = NULL;

    currNode->next = addNode;
    currNode = addNode;
    return addNode;
}
/******** End: add_Address Function**********/

/******** Start: create_New_list Function**********/
struct address_t *create_list(char paramString[26])
{
    struct address_t *newNode = (struct address_t *)malloc(sizeof(struct address_t));
    if(NULL == newNode){
        printf("Error while memory allocation to new node");
        return NULL;
    }

    sscanf(paramString, "%d.%d.%d.%d %s", &newNode->octet[0], &newNode->octet[1], &newNode->octet[2], &newNode->octet[3], &newNode->alias);
    newNode->next = NULL;

    // Inserting the node in beginning
    head = currNode = newNode;
    return newNode;
}
/******** End: create_New_list Function**********/

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
}
/******** End: search_In_list Function**********/

/******** Start: add_address_to_list Function**********/
int add_address_to_list(){
    char newAlias[10], newAddr[15], newAddrAlias[26];
    int tempOctet[4];
    while(true){
        printf("Enter new alias for your address-alias pair: ");
        scanf("%s",newAlias);

        if(strlen(newAlias) <= 10){
            if(search_In_List(newAlias)){
                printf("error:%s already exists", newAlias);
                return -1;
            }

            while(true){
                printf("Enter address for %s: ", newAlias);
                scanf("%s", newAddr);
                sscanf(newAddr, "%d.%d.%d.%d", &tempOctet[0], &tempOctet[1], &tempOctet[2], &tempOctet[3]);
                if((tempOctet[0] >= 0 && tempOctet[0]<=255) && (tempOctet[1] >= 0 && tempOctet[1]<=255) && (tempOctet[2] >= 0 && tempOctet[2]<=255) && (tempOctet[3] >= 0 && tempOctet[3]<=255)){
                    snprintf(newAddrAlias,sizeof(newAddrAlias), "%s %s", newAddr, newAlias);
                    add_AddressNode_To_List(newAddrAlias);
                    return 0;
                }
            }
        }
        printf("\nError: Alias string length should be less than equal to 10");
    }

}
/******** End: add_address_to_list Function**********/

/******** Start: lookUp_Address_in_List() Function**********/
int lookUp_Address_in_List(){
    struct address_t *tempPtr = head;
    bool flagFound = false;

    // while(tempPtr != NULL){
    //     if(!(strcmp(tempPtr->alias,paramAlias))){
    //         flagFound = true;
    //         return tempPtr;
    //     }else{
    //         tempPtr = tempPtr->next;
    //     }
    // }
}
/******** End: lookUp_Address_in_List() Function**********/


int main(){
    int operationsToPerform=0;
    int lengthOfInputString = 25;
    char *inputString = malloc(sizeof(char) * lengthOfInputString);
    FILE *filePtr = fopen("C:/Users/ME/Github/90DaysOfCoding/Day25_11012022/AssignmentLinkedListPrac/CS531_Inet.txt", "r+");
    
    if(filePtr == NULL){
        printf("Error! Path doesn't exist.");
        return -1;
    }

    while(fgets(inputString, lengthOfInputString, filePtr) != NULL){
        puts(inputString);
    }

    while(true){
        printf(" \n\n 1) Add address\n 2) Loop up address\n 3) Update address\n 4) Delete address\n 5) Display list\n 6) Display aliases for location\n 7) Save to file\n 8) Quit\n\n Enter option: ");
        scanf("%d", &operationsToPerform);

        switch (operationsToPerform)
        {
        case 1:
            /* code */
            printf("Add Address\n");
            add_address_to_list();
            break;
        case 2:
            printf("Look Up Address\n");
            //lookUp_Address_in_List()
            break;
        case 3:
            printf("Update List\n");
            break;
        case 4:
            printf("Delete From List\n");
            break;
        case 5:
            printf("Display List\n");
            break;
        case 6:
            printf("Display Alias for Location\n");
            break;
        case 7:
            printf("Save To File\n");
            break;
        case 8:
            printf("Good Bye\n");
            return 0;

        default:
            printf("Invalid choice - please reenter 1-8");
            break;
        }
    }

    return 0;
}