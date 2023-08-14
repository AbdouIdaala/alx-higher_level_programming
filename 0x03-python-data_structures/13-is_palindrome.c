#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *temp, *temp1, *first, *second, *head1;

    if (!(*head)->next)
        return (1);
    first = *head;
    second = *head;
    while (1)
    {
        second = second->next->next;
        if (second == NULL)
        {
            head1 = first->next;
            first->next = NULL;
            break;
        }
        if (second->next == NULL)
        {
            head1 = first->next->next;
            first->next = NULL;
            break;
        }
        first = first->next;
    }
    temp1 = reverse_listint(&head1);
    temp = *head;
    while (temp1 && temp)
    {
        if (temp1->n != temp->n)
            return (0);
        temp1 = temp1->next;
        temp = temp->next;
    }
    return (1);
}
/**
 * reverse_listint - the function that reverses a listint_t
 * @head: double pointer
 * Return: a pointer to the first node of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
    listint_t *temp = NULL, *ptr;

    while (*head)
    {
        ptr = (*head)->next;
        (*head)->next = temp;
        temp = *head;
        *head = ptr;
    }
    *head = temp;

    return (*head);
}