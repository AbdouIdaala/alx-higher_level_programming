#include "lists.h"

/**
 * check_cycle - check if a singly linked list has a cycle in it
 * @list: the singly linked list to check
 *
 * Return: 1 if there is a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = NULL;

	if (slow)
	{
		fast = slow->next;
		while (fast)
		{
			if (fast == list || fast == slow)
				return (1);
			slow = slow->next;
			fast = fast->next;
		}
	}
	return (0);
}
