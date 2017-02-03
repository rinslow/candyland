from collections import defaultdict


class Immutable(object):
    """Immutability class.

    Attributes:
        changed_values (dict): whether or not a property was set.
    """
    def __init__(self):
        self.__dict__["changed_values"] = defaultdict(bool)

    def __setattr__(self, key, value):
        if self.changed_values[key]:
            raise ImmutabilityException("Cannot change attribute %s." % key)

        self.__dict__[key] = value
        self.changed_values[key] = True

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash(self.__class__.__name__ + "@" + str(self.__dict__))


class ImmutabilityException(Exception):
    """Occurs when trying to change an immutable object."""
    pass
