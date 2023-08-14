#include <stdio.h>
#include <Python.h>
#include <listobject.h>
#include <object.h>

void print_python_list_info(PyObject *p)
{
    Py_ssize_t size = PyList_Size(p);

    printf("[*] Size of the Python List = %ld\n", size);
}