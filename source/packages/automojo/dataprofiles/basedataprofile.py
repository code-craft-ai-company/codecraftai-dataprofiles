"""
    .. module:: basedataprofile
        :platform: Darwin, Linux, Unix, Windows
        :synopsis: Module that defines the :class:`BaseDataProfile` class used as
                    the base for data source profile objects.

    .. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2025, Automation Mojo LLC"
__credits__ = []

from typing import Dict, List, Optional, Tuple, Union

class BaseDataProfile:
    """
        The :class:`BaseDataProfiles` object serves as a base class for data source profile objects.
    """
    def __init__(self, identifier: str, *, category: str, credential: Optional[str] = None):
        """
            Constructs a :class:`BaseDataProfile` instance.

            :param identifier: The name used to reference this profile.
            :param category: The profile category.
            :param credential: Optional credential reference.
        """
        self._identifier = identifier
        self._category = category
        self._credential = credential
        return

    @property
    def credential(self) -> Union[str, None]:
        """
            The credential identifier associated with this profile.

            :returns: Credential identifier or ``None``.
        """
        return self._credential

    @property
    def identifier(self) -> str:
        """
            The identifier for the profile.

            :returns: Profile identifier.
        """
        return self._identifier

    @property
    def category(self) -> str:
        """
            The category for the profile.

            :returns: Profile category.
        """
        return self._category
    
    @classmethod
    def validate(cls, profile_info: Dict[str, str]) -> Tuple[List[str], List[str]]:
        """
            Validates that a data profile has the minimum required fields.

            :param profile_info: Data profile dictionary to validate.

            :returns: Lists of errors and warnings.
        """
        errors = []
        warns = []

        identifier = "Unknown"

        if "identifier" not in profile_info:
            errmsg = "Profile is missing the mandatory 'identifier' field."
            errors.append(errmsg)
        else:
            identifier = profile_info["identifier"]

        if "category" not in profile_info:
            errmsg = f"The '{identifier}' profile is missing the mandatory 'category' field."
            errors.append(errmsg)

        return errors, warns
