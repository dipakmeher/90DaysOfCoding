// There is an error in this program that needs to be resolved....

#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<string.h>
#include "linkedListheader.h"

// void print_List();
// struct address_t *create_list(char paramString[26]);
// struct address_t *search_In_List(char paramAlias[11]);
// struct address_t *add_AddressNode_To_List(char paramString[26]);

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


int main(){
    int operationsToPerform=0;
    int lengthOfInputString = 27;
    char *inputString = malloc(sizeof(char) * lengthOfInputString);
    FILE *filePtr = fopen("CS531_Inet.txt", "r+");
     
    if(filePtr == NULL){
        printf("Error! Path doesn't exist.");
        return -1;
    }

    while (fgets(inputString, lengthOfInputString, filePtr))
    {
        add_AddressNode_To_List(inputString);
    }

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
            Quit_Function();
            fclose(filePtr);
            return 0;

        default:
            printf("Invalid choice - please reenter 1-8");
            break;
        }
    }

    return 0;
}

// /******** Start: print_List() Function**********/
// void print_List(){
//     struct address_t *printPtr = head;

//     while (printPtr != NULL)
//     {
//         printf("%d.%d.%d.%d %s\n", printPtr->octet[0], printPtr->octet[1], printPtr->octet[2], printPtr->octet[3], printPtr->alias);
//         printPtr = printPtr->next;
//     }
//     return; 

// }
// /******** End: print_List() Function**********/

// /******** Start: create_New_list Function**********/
// struct address_t *create_list(char paramString[26])
// {
//     struct address_t *newNode = (struct address_t *)malloc(sizeof(struct address_t));
//     if(NULL == newNode){
//         printf("Error while memory allocation to new node");
//         return NULL;
//     }

//     sscanf(paramString, "%d.%d.%d.%d %s", &newNode->octet[0], &newNode->octet[1], &newNode->octet[2], &newNode->octet[3], &newNode->alias);
//     newNode->next = NULL;

//     // Inserting the node in beginning
//     head = newNode;
//     currNode = newNode;
//     return newNode;
// }
// /******** End: create_New_list Function**********/

// /******** Start: search_In_list Function**********/
// struct address_t *search_In_List(char paramAlias[11]){
//     struct address_t *tempPtr = head;
//     bool flagFound = false;

//     while(tempPtr != NULL){
//         if(!(strcmp(tempPtr->alias,paramAlias))){
//             flagFound = true;
//             return tempPtr;
//         }else{
//             tempPtr = tempPtr->next;
//         }
//     }
//     return NULL;
// }
// /******** End: search_In_list Function**********/

// /******** Start: add_Address Function**********/
// struct address_t *add_AddressNode_To_List(char paramString[26])
// {
//     if(head == NULL){
//         return (create_list(paramString));
//     }
//     struct address_t *addNode = (struct address_t *)malloc(sizeof(struct address_t));

//     if(NULL == addNode){
//         printf("Error while memory allocation to new node");
//         return NULL;
//     }

//     sscanf(paramString, "%d.%d.%d.%d %s", &addNode->octet[0], &addNode->octet[1], &addNode->octet[2], &addNode->octet[3], &addNode->alias);
//     addNode->next = NULL;

//     currNode->next = addNode;
//     currNode = addNode;
//     return addNode;  
// }
// /******** End: add_Address Function**********/