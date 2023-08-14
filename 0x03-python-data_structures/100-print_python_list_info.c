#include <stdio.h>
#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t i;

    printf("[*] Size of the Python List = %ld\n", size);
    for (i = 0; i < size; i++)
    {
        printf("Element %ld: \n", i);
    }
}