#include "lists.h"

/**
 * Check cycle: this function checks if list has a cycle
 * @list: the linked list
 * #Return: returns 1 if list haa a cycle, returns 0 if it doesnt.
 *
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;
	if(!list || !list->next)
		return(0);
	fast = list;
	slow = list;

	while(slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if(slow == fast)
			return(1);

	}
	return(0);
}
