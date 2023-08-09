#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: head of the list
 * @number: number to insert
 *
 * Return: adress of the new node or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *temp = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return(NULL);

	new->n = number;
	new->next = NULL;
	if(*head == NULL) /*the list was empty, the new one only contains number*/
	{
		*head = new;
		return(new)
	}
	else if((*head)->n >= number) /*number is smaller than the first n in list*/
	{
		new->next = *head;
		*head = new;
		return(new);
	}
	else
	{
		while(temp->next != NULL) /*we go thro list to find where to put number*/
		{
			if(temp->next->n >= number) /*found the n that is bigger than number*/
			{
				new->next = temp->next;
				temp->next = new; /*list that starts with number*/
				new = temp;
				return(new);
			}
			temp = temp->next;
		}
		temp->next = new; /*if we went thro the loop but number was the biggest*/
		new = temp;
		return(new)
	}
	return(NULL);
}
