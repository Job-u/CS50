#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int countLetters(string text);
int countWords(string text);
int countSentences(string text);
int main(void)
{
    // Prompt the user for some text
    string text = get_string("Text: ");

    // Count the number of letters, words, and sentences in the text
    int letters = countLetters(text);
    int words = countWords(text);
    int sentences = countSentences(text);

    // Compute the Coleman-Liau index

    double L = letters * 100.0 / words;
    double S = sentences * 100.0 / words;
    double index = 0.0588 * L - 0.296 * S - 15.8;

    // Print the grade level
    if (round(index) < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (round(index) >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", (int) round(index));
    }

    return 0;
}

int countLetters(string text)
{
    int letters = 0;
    // strlen - calculate the length of a string
    int n = strlen(text);

    for (int i = 0; i < n; i++)
    {
        // isalpha - check whether a character is alphabetical
        if (isalpha(text[i]))
        {
            letters++;
        }
    }
    return letters;
}

int countWords(string text)
{
    int words = 1;
  // strlen - calculate the length of a string
    int n = strlen(text);

    for (int i = 0; i < n; i++)
    {
        if (text[i] == ' ')
        {
            words++;
        }
    }
    return words;
}

int countSentences(string text)
{
    // Return the number of sentences in text

    int sentences = 0;
    // strlen - calculate the length of a string
    int n = strlen(text);
    for (int i = 0; i < n; i++)
    {
        if (text[i] == '!' || text[i] == '.' || text[i] == '?')
        {
            sentences++;
        }
    }
    return sentences;
}
