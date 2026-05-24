import os
import sys

class AppException(Exception):
    
    def __init__(self, error_message: Exception, error_detail: sys):
        super().__init__(error_message)
        self.error_message = AppException.get_detailed_error_message(error_message=error_message, error_detail=error_detail)
        
    @staticmethod
    def get_detailed_error_message(error, error_detail: sys):
        _, _, exc_tb = error_detail.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        error_message = f"Error occurred in script: {file_name} at line number: {line_number} with error message: {str(error)}"
        return error_message
    
    def __repr__(self):
        """
        Formating object of AppException
        """
        return AppException.__name__.__str__()

    def __str__(self):
        """
        Formating how a object should be visible if used in print statement.
        """
        return self.error_message