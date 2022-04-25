#include "lists.h"
/**
 * check_cycle - Checks if a slinked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list->next;
	listint_t *fast = list->next->next;

	if (list == NULL)
		return (0);
	while (slow != fast)
	{
		if (fast == NULL || fast->next == NULL)
			return (0);
		slow = slow->next;
		fast = fast->next->next;
	}
	if (slow == fast)
	{
	return (1);
	}
	else
	return (0);
}
