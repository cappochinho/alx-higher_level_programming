#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: singly linked list
 * Return: 0 if there is no cycle, else 1 if there is a cycle
 *
 */
int check_cycle(listint_t *list)
{
	int n_cycles = 0;
	listint_t *temp = list;
	listint_t *temp_list = list;

	while (temp_list != NULL)
	{
		temp_list = temp_list->next;
		if (temp == temp_list)
		{
			n_cycles = 1;
			break;
		}
	}

	return (n_cycles);
}
