#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: singly linked list
 * Return: 0 if there is no cycle, else 1 if there is a cycle
 *
 */
int check_cycle(listint_t *list)
{
	listint_t *temp_list = list;
	
	if (list == NULL)
		return (0);

	while (temp_list != NULL)
	{
		temp_list = temp_list->next;
		if (list == temp_list)
			return (1);
	}

	return (0);
}
