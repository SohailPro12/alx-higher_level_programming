#include <Python.h>

/**
 * print_python_list_info - Cpython code print info list
 * @p: list type PyObject.
 */

void print_python_list_info(PyObject *p)
{
	PyObject *item;
	int size, c, i;

	size = Py_SIZE(p);
	c = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", c);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		item = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(item)->tp_name);
	}
}
