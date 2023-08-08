#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if a singly linked list has a cycle.
 * @list: Singly linked list.
 *
 * Return: 0 if there is no cycle, 1 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *first, *second;

	if (!list)
		return (0);

	first = list->next;
	second = list->next->next;

	while (first && second && second->next)
	{
		if (first == second)
			return (1);

		first = first->next;
		second = second->next->next;
	}
	return (0);
}
