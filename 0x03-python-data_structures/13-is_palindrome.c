#include "lists.h"

/**
 * is_palindrome - find if singly linked list is a palindrome
 * @head: pointer to head of singly linked list
 * Return: 0 if not, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	unsigned int size = 0, k = 0;
	int data[10240];

	if (head == NULL)
		return (0);

	if (*head == NULL)
		return (1);

	while (tmp)
	{
		tmp = tmp->next;
		size += 1;
	}
	if (size == 1)
		return (1);

	tmp = *head;
	while (tmp)
	{
		data[k++] = tmp->n;
		tmp = tmp->next;
	}

	for (k = 0; k <= (size / 2); k++)
	{
		if (data[k] != data[size - k - 1])
			return (0);
	}
	return (1);
}

