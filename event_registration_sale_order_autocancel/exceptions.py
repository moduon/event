# Copyright 2024 Moduon Team S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0)

from odoo import _, exceptions


class ModuleNameValidationError(exceptions.ValidationError):
    """Base class for this module's validation errors."""

    def __init__(self, *args, **kwargs):
        self._args, self._kwargs = args, kwargs
        value = self._message()
        super().__init__(value)

    def _message(self):
        """Format the message."""
        return self.__doc__.format(*self._args, **self._kwargs)


class WrongNameError(ModuleNameValidationError):
    """Name {} is wrong."""


class TranslatedWrongNameError(ModuleNameValidationError):
    __doc__ = _("Name {} is wrong.")
