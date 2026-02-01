#include <cs50.h>
#include <stdio.h>


int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int main(void)
{

    int cents;
    do
    {
        cents = get_int("Change owed: ");
    }
    while (cents < 0);


    int quarters = calculate_quarters(cents);
    cents -= quarters * 25;

    int dimes = calculate_dimes(cents);
    cents -= dimes * 10;

    int nickels = calculate_nickels(cents);
    cents -= nickels * 5;

    int pennies = calculate_pennies(cents);


    int coins = quarters + dimes + nickels + pennies;


    printf("%i\n", coins);
}


int calculate_quarters(int cents)
{
    int count = 0;
    while (cents >= 25)
    {
        count++;
        cents -= 25;
    }
    return count;
}

int calculate_dimes(int cents)
{
    int count = 0;
    while (cents >= 10)
    {
        count++;
        cents -= 10;
    }
    return count;
}

int calculate_nickels(int cents)
{
    int count = 0;
    while (cents >= 5)
    {
        count++;
        cents -= 5;
    }
    return count;
}

int calculate_pennies(int cents)
{
    return cents;
}
