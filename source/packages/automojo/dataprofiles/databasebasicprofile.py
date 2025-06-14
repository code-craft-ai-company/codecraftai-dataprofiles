"""
    .. module:: databasebasicprofile
        :platform: Darwin, Linux, Unix, Windows
        :synopsis: Module that defines the :class:`DatabaseBasicProfile` class
                    used for database profile metadata without host details.

    .. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2025, Automation Mojo LLC"
__credits__ = []

from typing import Dict

from automojo.dataprofiles.basedataprofile import BaseDataProfile

class DatabaseBasicProfile(BaseDataProfile):

    def __init__(self, identifier: str, *, category: str, dbtype: str, dbname: str = None, credential: str = None):
        """
            Initializes a :class:`DatabaseBasicProfile` instance.

            :param identifier: Name used to reference the profile.
            :param category: The profile category.
            :param dbtype: The database engine type.
            :param dbname: Optional database name.
            :param credential: Credential identifier used for authentication.
        """
        super().__init__(identifier, category=category, credential=credential)

        self._dbtype = dbtype
        self._dbname = dbname

        return
    
    @property
    def dbname(self) -> str:
        """
            The database name associated with the profile.

            :returns: Database name value.
        """
        return self._dbname
    
    @property
    def dbtype(self) -> str:
        """
            The database engine type.

            :returns: Database type string.
        """
        return self._dbtype

    @classmethod
    def validate(cls, profile_info: Dict[str, str]):
        """
            Validates a basic database profile configuration.

            :param profile_info: Profile configuration to validate.

            :returns: Lists of errors and warnings.
        """

        errors = []
        warns = []

        if "credential" not in profile_info:
            errmsg = f"The 'basic-profile' profile must have an 'credential' field."
            errors.append(errmsg)
        
        if "dbname" not in profile_info:
            errmsg = f"The 'basic-profile' profile must have an 'dbname' field."
            errors.append(errmsg)
        
        if "dbtype" not in profile_info:
            errmsg = f"The 'basic-profile' profile must have an 'dbtype' field."
            errors.append(errmsg)

        return errors, warns