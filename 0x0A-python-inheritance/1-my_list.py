#!/usr/bin/python3
"""My custom list class
"""


class MyList(list):
    """A custom list class that extends the built-in list class.

    Args:
        list (list): The initial list.
    """

    def print_sorted(self):
        """Prints the elements of the list in ascending order.

        Args:
            None

        Returns:
            None
        """
        new_list = sorted(self)
        print(new_list)
