#include "lists.h"

/**
 * check_cycle - check if a singly linked list has a cycle in it
 * @list: the singly linked list to check
 *
 * Return: 1 if there is a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *temp1 = list;
	listint_t *temp2 = NULL;
	listint_t *temp3 = NULL;

	if (temp1)
	{
		temp3 = list;
		while (temp3)
		{
			if (temp3 == list)
				return (1);
			temp3 = temp3->next;
		}
		temp2 = temp1->next;
		while (temp2)
		{
			if (temp2 == temp1 || temp2 == temp1->next)
				return (1);
			temp1 = temp1->next;
			temp2 = temp2->next;
		}
	}
	return (0);
}
