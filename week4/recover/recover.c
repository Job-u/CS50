#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define BLOCK_SIZE 512

int main(int argc, char *argv[])
{
    //Check correct usage
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    //Open forensic image
    FILE *card = fopen(argv[1], "r");
    if (card == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    //Buffer for reading blocks
    uint8_t buffer[BLOCK_SIZE];

    //JPEG counter
    int jpeg_count = 0;

    //File pointer for recovered JPEG
    FILE *img = NULL;

    //Filename buffer (###.jpg + '\0')
    char filename[8];

    //Read blocks until end of file
    while (fread(buffer, 1, BLOCK_SIZE, card) == BLOCK_SIZE)
    {
        // Check if block starts a new JPEG
        if (buffer[0] == 0xff &&
            buffer[1] == 0xd8 &&
            buffer[2] == 0xff &&
            (buffer[3] & 0xf0) == 0xe0)
        {
            // If already writing a JPEG, close it
            if (img != NULL)
            {
                fclose(img);
            }

            // Create new filename
            sprintf(filename, "%03i.jpg", jpeg_count);

            // Open new JPEG file
            img = fopen(filename, "w");

            // Increase JPEG counter
            jpeg_count++;
        }

        // If we are currently writing a JPEG, write the block
        if (img != NULL)
        {
            fwrite(buffer, 1, BLOCK_SIZE, img);
        }
    }

    //Close remaining files
    if (img != NULL)
    {
        fclose(img);
    }
    fclose(card);

    return 0;
}
