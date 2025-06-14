"""
    .. module:: databasebasictcpprofile
        :platform: Darwin, Linux, Unix, Windows
        :synopsis: Module that defines :class:`DatabaseBasicTcpProfile` for
                    databases accessed via host and port over TCP.

    .. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2025, Automation Mojo LLC"
__credits__ = []

from typing import Dict

from automojo.dataprofiles.basedataprofile import BaseDataProfile

class DatabaseBasicTcpProfile(BaseDataProfile):

    category = "basic-tcp"

    def __init__(self, identifier: str, *, category: str, host: str, port: int, dbtype: str, dbname: str = None, credential: str = None):
        """
            Initializes a :class:`DatabaseBasicTcpProfile` instance.

            :param identifier: Name used to reference the profile.
            :param category: The profile category.
            :param host: Host name for the database service.
            :param port: Port for the database service.
            :param dbtype: Database engine type.
            :param dbname: Optional database name.
            :param credential: Credential identifier used for authentication.
        """
        super().__init__(identifier, category=category, credential=credential)

        self._host = host
        self._port = port
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
    
    @property
    def host(self) -> str:
        """
            Host name where the database engine can be reached.

            :returns: Host name value.
        """
        return self._host
    
    @property
    def port(self) -> int:
        """
            TCP port for connecting to the database engine.

            :returns: Port value.
        """
        return self._port

    @classmethod
    def validate(cls, profile_info: Dict[str, str]):
        """
            Validates a basic TCP database profile configuration.

            :param profile_info: Profile configuration to validate.

            :returns: Lists of errors and warnings.
        """
        
        errors = []
        warns = []

        if "credential" not in profile_info:
            errmsg = f"The 'basic-tcp' profile must have an 'credential' field."
            errors.append(errmsg)
        
        if "dbtype" not in profile_info:
            errmsg = f"The 'basic-tcp' profile must have an 'dbtype' field."
            errors.append(errmsg)
        
        if "host" not in profile_info:
            errmsg = f"The 'basic-tcp' profile must have an 'host' field."
            errors.append(errmsg)
        
        if "port" not in profile_info:
            errmsg = f"The 'basic-tcp' profile must have an 'port' field."
            errors.append(errmsg)
        

        return errors, warns