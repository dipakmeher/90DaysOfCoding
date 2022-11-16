#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<string.h>
#include "linkedListheader.h"
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