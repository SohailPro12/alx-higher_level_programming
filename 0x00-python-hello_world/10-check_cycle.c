#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if list is cyclical
 * @list: pointer to list to check
 * Return: 1 if cyclical, 0 otherwise
 */

int check_cycle(listint_t *list)
{
	if (list == NULL)
		return (0);

	listint_t *prevone = list;
	listint_t *fastone = list->next;

	while (fastone && fastone->next && prevone)
	{
		if (prevone == fastone)
			return (1);
		fastone = fastone->next->next;
		prevone = prevone->next;
	}
	return (0);
}

