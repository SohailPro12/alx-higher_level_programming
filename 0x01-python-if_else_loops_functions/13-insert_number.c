#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - sorted list
 * @head: address
 * @number: number
 * Return: inserted node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *h_ref = *head, *new_node = malloc(sizeof(listint_t));

	if (!new_node)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (!h_ref || new_node->n < h_ref->n)
	{
		new_node->next = h_ref;
		return (*head = new_node);
	}

	while (h_ref)
	{
		if (!h_ref->next || new_node->n < h_ref->next->n)
		{
			new_node->next = h_ref->next;
			h_ref->next = new_node;
			return (h_ref);
		}
		h_ref = h_ref->next;
	}
	return (NULL);
}
