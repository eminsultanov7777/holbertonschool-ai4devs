/* Fixed Bug 4: Use a valid array boundary. */
#include <stdio.h>

int main(void)
{
    int numbers[] = {4, 8, 12, 16, 20};
    int length = sizeof(numbers) / sizeof(numbers[0]);

    for (int i = 0; i < length; i++)
    {
        printf("%d\n", numbers[i]);
    }

    return 0;
}
