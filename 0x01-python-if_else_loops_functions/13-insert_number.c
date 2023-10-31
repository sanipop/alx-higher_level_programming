de "lists.h"

/**
 * insert_node - A function in alinked list.
 * @head: the start of the list.
 * @number: the value to be added to the list.
 *
 * Return: return on fsilure - NULL.
 * Otherwise - else point to the next node.
 */
listint_t *insert_node(listint_t **head, int number)
{
        listint_t *node = *start, *curr;

        curr = malloc(sizeof(listint_t));
        if (curr == NULL)
                return (NULL);
        curr->n = number;

        if (node == NULL || node->n >= number)
        {
                curr->next = node;
                *start = curr;
                return (curr);
        }

        while (node && node->next && node->next->n < number)
                node = node->next;

        curr->next = node->next;
        node->next = curr;

        return (curr);
}
