/**
 * Task to to done:
 * Making separate c file for reach program
 * Create MAKE file
*/

#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<string.h>

struct address_t{
    int octet[4];
    char alias[11];
    struct address_t *next;
};
struct address_t *head = NULL;
struct address_t *currNode = NULL;

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

                struct address_t *traversePtr = head;
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

/******** Start: lookUp_Address_in_List() Function**********/
int lookUp_Address_in_List(){
    char newAlias[11];
    struct address_t *foundNode = NULL;

    printf("Enter alias: ");
    scanf("%s", newAlias);
    foundNode = search_In_List(newAlias);
    if(foundNode!=NULL){
        printf("Address of alias %s: %d.%d.%d.%d\n", foundNode->alias, foundNode->octet[0], foundNode->octet[1], foundNode->octet[2], foundNode->octet[3]);
        return 0;
    }
    // while(tempPtr != NULL){
    //     if(!(strcmp(tempPtr->alias,newAlias))){
    //         foundNode = tempPtr;
    //         printf("Address for %s: %d.%d.%d.%d\n", tempPtr->alias, tempPtr->octet[0], tempPtr->octet[1], tempPtr->octet[2], tempPtr->octet[3]);
    //         return 0;
    //     }else{
    //         tempPtr = tempPtr->next;
    //     }
    // }
    printf("\n>>Error: %s does not exist in list.\n", newAlias);
    return -1;
}
/******** End: lookUp_Address_in_List() Function**********/

/******** Start: update_In_List() Function**********/
struct address_t *update_In_List(){
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
            return NULL;
        }
        for (int i = 0; i < 4; i++)
        {
            foundNode->octet[i] = tempOctet[i];
        }
        return foundNode;
    }else{
        return NULL;
    }
}
/******** End: update_In_List() Function**********/

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

/******** Start: display_List() Function**********/
void display_list() // printing the list in the required format
{
    int count = 0;
    struct address_t *ptr = head;
    while (ptr != NULL)
    {
        printf("%d.%d.%d.%d %s\n", ptr->octet[0], ptr->octet[1], ptr->octet[2], ptr->octet[3], ptr->alias);
        ptr = ptr->next;
        count++;
    }
    printf("Total node count: %d\n", count);
    return;
}
/******** End: display_List() Function**********/

/******** Start: display_Alias_For_Location() Function**********/
void display_Alias_For_Location(){
    int tempOctet[2], countAddress=0;
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
        }
        tempPtr = tempPtr->next;
    }
}
/******** End: display_Alias_For_Location() Function**********/

/******** Start: save_To_File Function**********/
int save_To_File(){
    char fileName[20];
    char path[100] = "C:/Users/ME/Github/90DaysOfCoding/Day25_11012022/AssignmentLinkedListPrac/";
    struct address_t *tempPtr = head;

    printf("Enter filename: ");
    scanf("%s",fileName);

    strcat(fileName, ".txt");
    strcat(path,fileName);

    FILE *filePtr = fopen(path, "w");
    if(filePtr == NULL){
        printf("\n>>Error opening File");
        return -1;
    } 
    tempPtr = head;
    while(tempPtr != NULL){
        fprintf(filePtr, "%d.%d.%d.%d %s\n", tempPtr->octet[0], tempPtr->octet[1], tempPtr->octet[2], tempPtr->octet[3], tempPtr->alias);
        tempPtr = tempPtr->next;
    }
    printf("File Saved.");
    fclose(filePtr);
    return 0;

}
/******** End: save_To_File Function**********/


int main(){
    int operationsToPerform=0;
    int lengthOfInputString = 25;
    char *inputString = malloc(sizeof(char) * lengthOfInputString);
    FILE *filePtr = fopen("C:/Users/ME/Github/90DaysOfCoding/Day25_11012022/AssignmentLinkedListPrac/CS531_Inet.txt", "r+");
    
    if(filePtr == NULL){
        printf("Error! Path doesn't exist.");
        return -1;
    }

    // while(fgets(inputString, lengthOfInputString, filePtr) != NULL){
    //     puts(inputString);
    // }

    while(true){
        printf(" \n\n1) Add address\n 2) Loop up address\n 3) Update address\n 4) Delete address\n 5) Display list\n 6) Display aliases for location\n 7) Save to file\n 8) Quit\n\n Enter option: ");
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
            lookUp_Address_in_List();
            break;
        case 3:
            printf("Update List\n");
            update_In_List();
            break;
        case 4:
            printf("Delete From List\n");
            delete_From_List();
            break;
        case 5:
            printf("Display List\n");
            display_list();
            break;
        case 6:
            printf("Display Alias for Location\n");
            display_Alias_For_Location();
            break;
        case 7:
            printf("Save To File\n");
            save_To_File();
            break;
        case 8:
            printf("Good Bye\n");
            fclose(filePtr);
            return 0;

        default:
            printf("Invalid choice - please reenter 1-8");
            break;
        }
    }

    return 0;
}