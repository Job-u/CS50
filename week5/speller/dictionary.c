#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#include <string.h>
#include "dictionary.h"


typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;


const unsigned int N = 10000;


node *table[N];


unsigned int word_count = 0;


bool check(const char *word)
{

    unsigned int index = hash(word);


    for (node *cursor = table[index]; cursor != NULL; cursor = cursor->next)
    {

        if (strcasecmp(cursor->word, word) == 0)
        {
            return true;
        }
    }

    return false;
}


unsigned int hash(const char *word)
{
    unsigned int hash_value = 0;

    for (int i = 0; word[i] != '\0'; i++)
    {
        hash_value = (hash_value * 31) + tolower(word[i]);
    }

    return hash_value % N;
}


bool load(const char *dictionary)
{
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        return false;
    }

    char word[LENGTH + 1];

    while (fscanf(file, "%s", word) != EOF)
    {
        // Allocate memory for new node
        node *new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            fclose(file);
            return false;
        }


        strcpy(new_node->word, word);
        new_node->next = NULL;


        unsigned int index = hash(word);


        new_node->next = table[index];
        table[index] = new_node;

        word_count++;
    }

    fclose(file);
    return true;
}


unsigned int size(void)
{
    return word_count;
}


bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        while (cursor != NULL)
        {
            node *temp = cursor;
            cursor = cursor->next;
            free(temp);
        }
    }

    return true;
}
