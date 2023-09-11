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
        self.new_list = []
        self.new_list.extend(self)
        self.new_list.sort()
        print(self.new_list)
