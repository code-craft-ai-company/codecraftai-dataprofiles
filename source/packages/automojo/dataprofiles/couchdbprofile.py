"""
    .. module:: couchdbprofile
        :platform: Darwin, Linux, Unix, Windows
        :synopsis: Module that defines the :class:`CouchDbProfile` class used to
                    describe CouchDB connection information.

    .. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2025, Automation Mojo LLC"
__credits__ = []

from typing import Dict

from automojo.dataprofiles.basedataprofile import BaseDataProfile
from automojo.interfaces.ibasiccredential import IBasicCredential

class CouchDbProfile(BaseDataProfile):

    category = "couchdb"

    def __init__(self, identifier: str, *, category: str, host: str, port: int, scheme: str = "http", dbname: str = None, credential: str = None):
        """
            Initializes a :class:`CouchDbProfile` instance.

            :param identifier: Name used to reference the profile.
            :param category: The profile category.
            :param host: Host name for the CouchDB instance.
            :param port: Port number for the CouchDB service.
            :param scheme: Protocol scheme for the connection.
            :param dbname: Optional database name.
            :param credential: Credential identifier used for authentication.
        """
        super().__init__(identifier, category=category, credential=credential)

        self._host = host
        self._port = port
        self._scheme = scheme
        self._dbname = dbname

        return
    
    @property
    def dbname(self) -> str:
        """
            The name of the CouchDB database.

            :returns: Database name.
        """
        return self._dbname
    
    @property
    def host(self) -> str:
        """
            The host where CouchDB is running.

            :returns: Host name.
        """
        return self._host
    
    @property
    def port(self) -> int:
        """
            The TCP port for CouchDB.

            :returns: Port value.
        """
        return self._port

    def connection_string(self, credobj: IBasicCredential) -> str:
        """
            Builds a connection string for the CouchDB server.

            :param credobj: Credential object containing the username and password.

            :returns: Connection string for the server.
        """
        connstr = f"{self._scheme}://{credobj.username}:{credobj.password}@{self._host}:{self._port}"
        return connstr

    @classmethod
    def validate(cls, profile_info: Dict[str, str]):
        """
            Validates a CouchDB profile configuration.

            :param profile_info: Profile configuration to validate.

            :returns: Lists of errors and warnings.
        """

        errors = []
        warns = []

        if "credential" not in profile_info:
            errmsg = f"The 'couchdb' profile must have an 'credential' field."
            errors.append(errmsg)
        
        if "dbname" not in profile_info:
            errmsg = f"The 'couchdb' profile must have an 'dbname' field."
            errors.append(errmsg)
        
        if "host" not in profile_info:
            errmsg = f"The 'couchdb' profile must have an 'host' field."
            errors.append(errmsg)
        
        if "port" not in profile_info:
            errmsg = f"The 'couchdb' profile must have an 'port' field."
            errors.append(errmsg)

        return errors, warns