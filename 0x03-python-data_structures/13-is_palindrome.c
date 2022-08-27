#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: The head of the linked list
 * Return: 0 if list is not a palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int *arr_n, count = 0, i = 0, j = 0;

	if (*head == NULL)
		return (1);

	while (temp != NULL)
	{
		temp = temp->next;
		count++;
	}

	arr_n = malloc(sizeof(int) * count);
	if (arr_n == NULL)
		return (0);
	while (temp != NULL)
	{
		arr_n[i] = temp->n;
		temp = temp->next;
		i++;
	}
	for (i = count - 1, j = 0; j < i; i--, j++)
	{
		if (arr_n[i] != arr_n[j])
			return (0);
	}
	return (1);
}
