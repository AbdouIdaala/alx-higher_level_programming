#!/usr/bin/python3
"""My list
"""


class MyList(list):
    """_summary_

    Args:
        list (_type_): _description_
    """

    def print_sorted(self):
        """_summary_
        """
        new_list = []
        new_list.extend(self)
        new_list.sort()
        print(new_list)
