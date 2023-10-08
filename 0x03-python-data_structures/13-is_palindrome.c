#include <string.h>
#include "lists.h"

/**
 * is_palindrome - functin
 * @head: start of list
 * Return: 1 suc or 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *prev = NULL, *tmp;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;

		tmp = slow->next;
		slow->next = prev;
		prev = slow;
		slow = tmp;
	}

	if (fast != NULL)
		slow = slow->next;

	if (slow != NULL)
	{
		if (slow->n != prev->n)
			return (0);

		slow = slow->next;
		prev = prev->next;
	}
	return (1);
}
