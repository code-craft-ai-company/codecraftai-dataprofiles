"""
    .. module:: mongodbatlasprofile
        :platform: Darwin, Linux, Unix, Windows
        :synopsis: Module that defines the :class:`MongoDBAtlasProfile` class
                    used for MongoDB Atlas connection information.

    .. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2025, Code Craft AI LLC"
__credits__ = []

from typing import Dict

from ccai.dataprofiles.basedataprofile import BaseDataProfile
from ccai.interfaces.ibasiccredential import IBasicCredential

class MongoDBAtlasProfile(BaseDataProfile):
    """
        The :class:`MongoDBAtlasProfile` class stores connection information for
        MongoDB Atlas deployments.
    """

    category = "mongodb-atlas"

    def __init__(self, identifier: str, *, category: str, connection: str, credential: str = None):
        """
            Initializes a :class:`MongoDBAtlasProfile` instance.

            :param identifier: Name used to reference the profile.
            :param category: The profile category.
            :param connection: MongoDB Atlas connection template.
            :param credential: Credential identifier used for authentication.
        """
        super().__init__(identifier, category=category, credential=credential)

        self._connection = connection
        return
    
    @property
    def connection(self) -> str:
        """
            Connection template string for MongoDB Atlas.

            :returns: Connection template.
        """
        return self._connection

    def connection_string(self, credobj: IBasicCredential) -> str:
        """
            Builds a connection string using credential information.

            :param credobj: Credential object containing the username and password.

            :returns: Expanded connection string.
        """
        connstr = self._connection.replace("<username>", credobj.username).replace("<password>", credobj.password)
        return connstr

    @classmethod
    def validate(cls, profile_info: Dict[str, str]):
        """
            Validates a MongoDB Atlas profile configuration.

            :param profile_info: Profile configuration to validate.

            :returns: Lists of errors and warnings.
        """
        
        errors = []
        warns = []

        if "credential" not in profile_info:
            errmsg = f"The 'mongodb-atlas' profile must have a 'credential' field."
            errors.append(errmsg)

        if "connection" not in profile_info:
            errmsg = f"The 'mongodb-atlas' profile must have a 'connection' field."
            errors.append(errmsg)

        return errors, warns
