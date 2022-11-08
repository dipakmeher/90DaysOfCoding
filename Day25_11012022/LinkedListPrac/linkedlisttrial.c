#include<stdio.h>
#include<stdlib.h>

struct node{
    int data;
    struct node* next;
};
struct node *head = NULL;

void insert(int data){
    //creating new link
    struct node *newNode; // Creating newNode
    newNode = (struct node*)malloc(sizeof(struct node));//Allocating memory
    newNode->data = data; // Allocating Data
    newNode->next = head; // Storing address to next and inserting the node in the beginning of LL
    head = newNode; // Making the head pointing to first node
}

void printList(){
    struct node *tempPtr = head;
    printf("Head = %p\n",head);
    while(tempPtr != NULL){
        printf("Node Addr = %p,\t Data: %d, \t next= %p \n",tempPtr, tempPtr->data,tempPtr->next);
        tempPtr= tempPtr->next;
    }
}

int main(){
    insert(108);
    insert(10);
    insert(1);
    printList();
    return 0;
}
