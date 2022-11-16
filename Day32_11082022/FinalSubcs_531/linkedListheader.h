void print_List();
int add_address_to_list();
int lookUp_Address_in_List();   
int update_In_List();
int delete_From_List();
void display_list();
void display_Alias_For_Location();
int save_To_File();
void Quit_Function();
int add_AddressNode_To_List(char paramString[26]);
int create_list(char paramString[26]);
//struct address_t *search_In_List(char paramAlias[11]);

struct address_t{
    int octet[4];
    char alias[11];
    struct address_t *next;
};
struct address_t *head, *currNode;


