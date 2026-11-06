/* Bug 4: Off-by-one loop error
 * Intended behavior: Print every element in an array exactly once.
 */
#include <stdio.h>

int main(void)
{
    int numbers[] = {4, 8, 12, 16, 20};
    int length = sizeof(numbers) / sizeof(numbers[0]);

    for (int i = 0; i <= length; i++)
    {
        printf("%d\n", numbers[i]);
    }

    return 0;
}

/* The loop reads one element beyond the end of the array. */
