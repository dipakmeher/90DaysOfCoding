#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
struct address_t // structure for storing address and alias
{
    int octet[4];
    char alias[11];
    struct address_t *next;
};

struct address_t *head = NULL;
struct address_t *curr = NULL;

void print_list() // displaying the linked list
{
    struct address_t *ptr = head;

    // printf("\n -------Printing list Start------- \n");
    while (ptr != NULL)
    {
        printf("%d.%d.%d.%d %s\n", ptr->octet[0], ptr->octet[1], ptr->octet[2], ptr->octet[3], ptr->alias);
        ptr = ptr->next;
    }

    return;
}

struct address_t *create_list(char val[27]) // assigning the given address and alias as head if linked list is empty
{
    struct address_t *ptr = (struct address_t *)malloc(sizeof(struct address_t));
    if (NULL == ptr)
    {
        printf("\n Node creation failed \n");
        return NULL;
    }
    sscanf(val, "%d.%d.%d.%d %s", &ptr->octet[0], &ptr->octet[1], &ptr->octet[2], &ptr->octet[3], ptr->alias);
    ptr->next = NULL;

    head = curr = ptr;
    return ptr;
}

struct address_t *add_to_list(char val[27]) // adding the address and alias and storing the address in linked list
{
    if (head == NULL)
    {
        return (create_list(val));
    }

    struct address_t *ptr = (struct address_t *)malloc(sizeof(struct address_t));
    if (NULL == ptr)
    {
        printf("\n Node creation failed \n");
        return NULL;
    }
    sscanf(val, "%d.%d.%d.%d %s", &ptr->octet[0], &ptr->octet[1], &ptr->octet[2], &ptr->octet[3], ptr->alias);
    ptr->next = NULL;

    curr->next = ptr;
    curr = ptr;

    return ptr;
}

struct address_t *search_in_list(char val[11], struct address_t **prev) // searching for the address based on the alias name
{
    struct address_t *ptr = head;
    struct address_t *tmp = NULL;
    bool found = false;
    // printf("\n Searching the list for value [%s] \n", val);
    while (ptr != NULL)
    {
        if (!(strcmp(ptr->alias, val)))
        {
            found = true;
            break;
        }
        else
        {
            tmp = ptr;
            ptr = ptr->next;
        }
    }
    if (true == found)
    {
        if (prev)
        {
            *prev = tmp;
        }
        return ptr;
    }
    else
    {
        return NULL;
    }
}

struct address_t *update_list() // update the address for the given alias name
{
    char val[10];
    int c = 0, b[4];
    printf("Enter alias: ");
    scanf("%s", val);
    struct address_t *ptr = head;
    struct address_t *tmp = NULL;
    bool found = false;
    // printf("\n Searching the list for value [%s] \n", val);
    while (ptr != NULL)
    {
        if (!(strcmp(ptr->alias, val)))
        {
            found = true;
            break;
        }
        else
        {
            tmp = ptr;
            ptr = ptr->next;
        }
    }
    if (true == found)
    {
        printf("update address for %s : %d.%d.%d.%d\n", ptr->alias, ptr->octet[0], ptr->octet[1], ptr->octet[2], ptr->octet[3]);
        while (c < 4)
        {
            printf("Enter location value # %d (0-255): ", (c + 1));
            scanf("%d", &b[c]);
            if (!(b[c] >= 0 && b[c] <= 255))
            {
                printf("error:%d is an illegal entry - please reenter:\n", b[c]);
                continue;
            }
            c++;
        }
        if (b[0] == ptr->octet[0] && b[1] == ptr->octet[1] && b[2] == ptr->octet[2] && b[3] == ptr->octet[3])
        {
            printf("error: duplicate address found");
            return NULL;
        }
        for (int i = 0; i < 4; i++)
        {
            ptr->octet[i] = b[i];
        }
        return ptr;
    }
    else
    {
        return NULL;
    }
}

int delete_from_list() // deleting the address and alias from the linked list
{
    char val[11];
    char ch;
    struct address_t *prev = NULL;
    struct address_t *del = NULL;
    printf("Enter alias: ");
    scanf("%s", val);
    // printf("\n Deleting value [%s] from list\n", val);
    del = search_in_list(val, &prev);
    if (del == NULL)
    {
        printf("error:%s does not exist\n", val);
        print_list();
        return -1;
    }
    else
    {
        printf("Delete %s %d.%d.%d.%d? (y/n) ", del->alias, del->octet[0], del->octet[1], del->octet[2], del->octet[3]);
        scanf("%s", &ch);
        if (ch == 'y')
        {
            if (prev != NULL)
                prev->next = del->next;

            if (del == curr)
            {
                curr = prev;
            }
            else if (!strcmp(del->alias, head->alias))
            {
                head = del->next;
            }
            printf("%s deleted\n", del->alias);
        }
    }
    free(del);
    del = NULL;

    return 0;
}

int add_address() // reading the input format and passing the value to add_to_list() function in the required format
{
    char alias[10], val[27], addr[15];
    int b[4];
    struct address_t *prev = NULL;
    while (true)
    {
        printf("\nEnter alias: ");
        scanf("%s", alias);
        if (strlen(alias) <= 10)
        {
            if (search_in_list(alias, &prev))
            {
                printf("error:%s already exists", alias);
                return -1;
            }
            while (true)
            {
                printf("Enter address for %s: ", alias);
                scanf("%s", addr);
                sscanf(addr, "%d.%d.%d.%d", &b[0], &b[1], &b[2], &b[3]);
                if ((b[0] >= 0 && b[0] <= 255) && (b[1] >= 0 && b[1] <= 255) && (b[2] >= 0 && b[2] <= 255) && (b[3] >= 0 && b[3] <= 255))
                {
                    snprintf(val, sizeof(val), "%s %s", addr, alias);
                    add_to_list(val);
                    return 0;
                }
                printf("error:%s is an illegal address - please reenter:\n", addr);
            }
        }
        printf("\nerror: alias string length should be less/equal to 10");
    }
}

int look_up_address() // printing the address octet based on the alias name
{
    char alias[11];
    struct address_t *prev = NULL;
    struct address_t *found = NULL;
    printf("Enter alias: ");
    scanf("%s", alias);
    found = search_in_list(alias, &prev);
    if (found)
    {
        printf("Address for %s: %d.%d.%d.%d\n", found->alias, found->octet[0], found->octet[1], found->octet[2], found->octet[3]);
        return 0;
    }
    printf("error: %s does not exist", alias);
    return -1;
}

void display_alias_for_location() // printing all the aliases in the given octet range
{
    int b[2], i = 0;
    while (i < 2)
    {
        while (true)
        {
            printf("Enter location value #%d (0-255): ", (i + 1));
            scanf("%d", &b[i]);
            if (b[i] >= 0 && b[i] <= 255)
            {
                break;
            }
            printf("error: %d is an illegal entry - please reenter", b[i]);
        }
        i++;
    }
    struct address_t *ptr = head;
    while (ptr != NULL)
    {
        if ((ptr->octet[0] == b[0]) && (ptr->octet[1] == b[1]))
        {
            printf("%d.      %s\n", ptr->octet[3], ptr->alias);
        }
        ptr = ptr->next;
    }
}

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

int save_to_file() // saving the linked list to a new file after the changes
{
    char filename[20];
    char path[100] = "D:/";
    struct address_t *ptr = head;
    struct address_t *tmp = NULL;
    printf("Enter filename: ");
    scanf("%s", filename);
    strcat(filename, ".txt");
    strcat(path, filename);
    FILE *fptr = fopen(path, "w");
    if (fptr == NULL)
    {
        printf("\nError opening file");
        return -1;
    }
    ptr = head;
    tmp = NULL;
    while (ptr != NULL)
    {
        fprintf(fptr, "%d.%d.%d.%d %s\n", ptr->octet[0], ptr->octet[1], ptr->octet[2], ptr->octet[3], ptr->alias);
        tmp = ptr;
        ptr = ptr->next;
    }
    printf("File saved");
    return 0;
}

int main()
{
    int ch = 0;
    int len = 27;
    char val[11];
    //struct address_t *ptr_search = (struct address_t *)malloc(sizeof(struct address_t));
    char *str = malloc(sizeof(char) * 27);
    FILE *fptr = fopen("C:/Users/ME/Downloads/HW3_Input.txt", "r+");
    if (fptr == NULL)
    {
        printf("Error opening file");
        return (-1);
    }
    while (fgets(str, len, fptr))
    {
        add_to_list(str);
    }

    while (true)
    {
        printf(" \n\n 1) Add address\n 2) Loop up address\n 3) Update address\n 4) Delete address\n 5) Display list\n 6) Display aliases for location\n 7) Save to file\n 8) Quit\n\n Enter option:");
        scanf("%d", &ch);
        switch (ch)
        {
        case 1:
            // Add Address
            add_address();
            break;

        case 2:
            // Look up address
            look_up_address();
            break;

        case 3:
            // update address
            update_list();
            break;

        case 4:
            // delete address
            delete_from_list();
            break;

        case 5:
            // display list
            display_list();
            break;

        case 6:
            // display alias for location
            display_alias_for_location();
            break;

        case 7:
            // save to file
            save_to_file();
            break;

        case 8:
            printf("Good bye!\n");
            fclose(fptr);
            return 0;

        default:
            printf("Invalid choice - please reenter 1-8");
        }
    }
}