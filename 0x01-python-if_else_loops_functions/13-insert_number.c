#include "lists.h"

/**
 * insert_node - insert a number into a sorted singly linked list
 * @head: pointer to a pointer of the start of the list
 * @number: integer to be included in node
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new = malloc(sizeof(listint_t));

    if (!new)
        return (NULL);
    new->n = number;
    if (!(*head)->next)
    {
        new->next = *head;
        *head = new;
    }
    /*
    if ((*head)->n > number)
    {
        new->next = *head;
        *head = new;
    }
    */
    return (new);
}