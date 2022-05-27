# -*- coding: utf-8 -*-
import messytables


class DateUtilType(messytables.types.DateUtilType):
    """ DateUtilType extension.
    - CSV format is not DateType
      2022-03-08 00:17:29,2022-03-07 23:52:21
    """
    target_strings = [',']

    def test(self, value):
        for target in self.target_strings:
            if target in value:
                return False
        return super().test(value)
