"""
    .. module:: databasebasicprofile
        :platform: Darwin, Linux, Unix, Windows
        :synopsis: Module that defines the :class:`DatabaseBasicProfile` class
                    used for database profile metadata without host details.

    .. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2025, Code Craft AI LLC"
__credits__ = []

from typing import Dict

from ccai.dataprofiles.basedataprofile import BaseDataProfile

class DatabaseBasicSocketProfile(BaseDataProfile):
    """
        The :class:`DatabaseBasicProfile` class describes database connection
        information without host or port details.
    """
    
    category = "basic-socket"

    def __init__(self, identifier: str, *, category: str, dbtype: str, dbname: str = None, socket: str = None, credential: str = None):
        """
            Initializes a :class:`DatabaseBasicProfile` instance.

            :param identifier: Name used to reference the profile.
            :param category: The profile category.
            :param dbtype: The database engine type.
            :param dbname: Optional database name.
            param socket: Optional socket path for the database connection.
            :param credential: Credential identifier used for authentication.
        """
        super().__init__(identifier, category=category, credential=credential)

        self._dbtype = dbtype
        self._dbname = dbname
        self._socket = socket

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
    
    @property
    def socket(self) -> str:
        """
            The socket path for the database connection.

            :returns: Socket path string.
        """
        return self._socket

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
            errmsg = f"The 'basic-socket' profile must have a 'credential' field."
            errors.append(errmsg)

        if "dbtype" not in profile_info:
            errmsg = f"The 'basic-socket' profile must have a 'dbtype' field."
            errors.append(errmsg)

        # 'dbname' and 'socket' are optional (the constructor defaults them to None),
        # so they are not required here -- requiring them rejected configs the data
        # class fully supports.

        return errors, warns