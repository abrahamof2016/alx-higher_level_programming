#include "lists.h"
/**
 * check_cycle - check if a singly linked list has a cycle in it.
 * @list: pointer to the first node.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *temp = list;

	while (temp != NULL)
	{
		temp = temp->next;
		if (temp->next == NULL)
		{
			return (0);
		}
		else if (temp->next == list)
		{
			return (1);
		}
	}
	return (0);
}
