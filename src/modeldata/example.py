"""Example module provides basic functionality.

A longer description can go here if greater details need to be provided
that span multiple lines.

Available functions:
- greeting: Provides a greeting personalized to the end-user.
"""


def greeting(name="Brad"):
    """
    Personalized greeting

    Provides a personalized greeting based on supplied name.

    Parameters
    ----------
    name
        A string representing the user's name.

    Returns
    -------
    String with personalized greeting.

    Examples
    --------
    >>> greeting(name='John')
    ... 'Hello John!'
    """
    return f"Hello {name}!"
