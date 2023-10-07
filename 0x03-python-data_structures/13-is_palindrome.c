#include "lists.h"
#include <string.h>
/**
 * is_palindrome - functin
 * @head: start of list
 * Return: 1 suc or 0
 */

int is_palindrome(listint_t **head)
{
	if (*head == NULL)
		return (1);

	char arr[1024];
	int i = 0;
	listint_t *current = *head;

	while (current)
	{
		arr[i] = current->n;
		current = current->next;
		i++;
	}

	int l = strlen(arr) - 1;
	int j = 0;

	while (l > j)
	{
		if (arr[j] != arr[l])
			return (0);
		j++;
		l--;
	}

	return (1);
}
