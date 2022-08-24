#include "lists.h"

/**
 * insert_node - insert number in sorted singly linked list
 * @head: head of the singly linked list
 * @number: number to insert in singly linked list
 *
 * Return: Linked list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *hold_head = *head;
	listint_t *temp = malloc(sizeof(listint_t));
	temp->n = number;
	temp->next = NULL;

	if (head == NULL)
	{
		*head = temp;
		return (*head);
	}
	else
	{
		while (hold_head->n < number)
			hold_head = hold_head->next;
		temp->next = hold_head->next;
		hold_head->next = temp;
	}
	return (hold_head);
}
