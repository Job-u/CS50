#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    string key = argv[1];


    if (strlen(key) != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }


    for (int i = 0; i < 26; i++)
    {
        if (!isalpha(key[i]))
        {
            printf("Key must only contain letters.\n");
            return 1;
        }


        for (int j = i + 1; j < 26; j++)
        {
            if (toupper(key[i]) == toupper(key[j]))
            {
                printf("Key must not contain repeated letters.\n");
                return 1;
            }
        }
    }


    string plaintext = get_string("plaintext: ");


    printf("ciphertext: ");


    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        char c = plaintext[i];

        if (isupper(c))
        {
            int index = c - 'A';
            printf("%c", toupper(key[index]));
        }
        else if (islower(c))
        {
            int index = c - 'a';
            printf("%c", tolower(key[index]));
        }
        else
        {

            printf("%c", c);
        }
    }

    printf("\n");
    return 0;
}
