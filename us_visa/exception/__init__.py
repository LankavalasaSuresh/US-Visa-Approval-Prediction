# Custom Exception code.
# In Python we have one Exception Package. We can create our custom exception by inheriting from Exception class as we did below.
# we are sys because, with the help of system we will trace the issue.



import os
import sys

def error_message_detail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message

class USvisaException(Exception):
    def __init__(self, error_message, error_detail):
        """
        :param error_message: error message in string format
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        return self.error_message
    


#below is Code in demo.py file which we used to test the exception code
#always run code in demo.py file , and not in exception constructor file

'''
from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys

logging.info("Welcome to our custom log")


try:
    a = 10 / "wwr"
except Exception as e:
    raise USvisaException(e, sys) from e
    
    
    
'''
    
