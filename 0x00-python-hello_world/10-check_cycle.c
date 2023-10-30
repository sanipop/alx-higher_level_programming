/**
 * check_cycle - checking if circle is contained in a linked list.
 * @list: The start of the list
 * Return: Binary status of the result
 */
int check_cycle(listint_t *list)
{
	listint_t *x, *verify;

	if (list == NULL || list->next == NULL)
		return (0);
	x = list;
	verify = x->next;

	while (x != NULL && verify->next != NULL
		&& verify->next->next != NULL)
	{
		if (x == verify)
			return (1);
		x = x->next;
		verify = verify->next->next;
	}
	return (0);
}
