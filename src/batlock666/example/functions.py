# NOQA: D100

def hello(name=None):
    """Return a hello message.
    """
    if name is None:
        # No name was given
        return "Hello, World!"
    else:
        # Name was given
        return "Hello, %s!" % name
