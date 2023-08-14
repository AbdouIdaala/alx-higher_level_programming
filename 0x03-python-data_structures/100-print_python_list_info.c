#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
    Py_ssize_t size = PyList_Size(p), i;
    PyObject *o;

    printf("[*] Size of the Python List = %ld\n", size);
    for (i = 0; i < size; i++)
    {
        o = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(o)->tp_name);
    }
}