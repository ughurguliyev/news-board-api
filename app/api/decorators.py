from rest_framework.response import Response
from rest_framework import status


def handle_errors(func):
    """Returns standart output if something went wrong.
    For view methods methods.
    """

    def wrap(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            return Response(
                {"success": False, "result": "Something unexpexted happened."},
                status=status.HTTP_400_BAD_REQUEST,
            )

    wrap.__doc__ = func.__doc__
    wrap.__name__ = func.__name__
    return wrap
