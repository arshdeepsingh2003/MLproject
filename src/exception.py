#Provides custom exception handling with meaningful error messages and traceability.

import sys 


def error_message_detail(error, error_detail: sys):
    """
    This function creates a detailed error message.
    It tells us:
    - Which file the error happened in
    - On which line the error happened
    - What the actual error message is
    """

    # Get the exception information (type, value, and traceback)
    _, _, exc_tb = error_detail.exc_info()

    # Get the name of the file where the error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Get the line number where the error occurred
    line_number = exc_tb.tb_lineno

    # Create a clean and readable error message
    error_message = (
        f"Error occurred in file [{file_name}] "
        f"at line [{line_number}] "
        f"with message: {str(error)}"
    )

    # Return the final error message
    return error_message


class CustomException(Exception):
    """
    This is a custom exception class.
    It extends Python's built-in Exception class
    and adds more detailed error information.
    """

    def __init__(self, error_message, error_detail: sys):
        # Call the parent class (Exception) constructor
        super().__init__(error_message)

        # Create a detailed error message using our function
        self.error_message = error_message_detail(
            error_message, error_detail
        )

    def __str__(self):
        """
        This function runs when the error is printed.
        It returns the detailed error message instead of a simple one.
        """
        return self.error_message
