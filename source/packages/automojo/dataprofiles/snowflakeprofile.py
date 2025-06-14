"""
    .. module:: snowflakeprofile
        :platform: Darwin, Linux, Unix, Windows
        :synopsis: Module that defines the :class:`SnowflakeProfile` class used
                    to describe Snowflake database connection settings.

    .. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2025, Automation Mojo LLC"
__credits__ = []

from typing import Dict, Union

from automojo.dataprofiles.basedataprofile import BaseDataProfile

class SnowflakeProfile(BaseDataProfile):

    category = "snowflake"

    def __init__(self, identifier: str, *, category: str, account: str, warehouse: str, database: str, schema: str = None, parameters: Dict[str, str] = None, credential: str = None):
        """
            Initializes a :class:`SnowflakeProfile` instance.

            :param identifier: Name used to reference the profile.
            :param category: The profile category.
            :param account: Snowflake account identifier.
            :param warehouse: Warehouse name.
            :param database: Database name.
            :param schema: Optional schema name.
            :param parameters: Optional connection parameters.
            :param credential: Credential identifier used for authentication.
        """
        super().__init__(identifier, category=category, credential=credential)

        self._account = account
        self._warehouse = warehouse
        self._database = database
        self._schema = schema
        self._parameters = parameters

        return
    
    @property
    def account(self) -> str:
        """
            The Snowflake account associated with the profile.

            :returns: Account name.
        """
        return self._account
    
    @property
    def database(self) -> str:
        """
            Database name configured for the profile.

            :returns: Database name.
        """
        return self._database
    
    @property
    def parameters(self) -> Dict[str, str]:
        """
            Optional connection parameters for Snowflake.

            :returns: Dictionary of connection parameters.
        """
        return self._parameters
    
    @property
    def schema(self) -> Union[str, None]:
        """
            Schema name associated with the profile.

            :returns: Schema name or ``None``.
        """
        return self._schema
    
    @property
    def warehouse(self) -> str:
        """
            Warehouse configured for the profile.

            :returns: Warehouse name.
        """
        return self._warehouse

    @classmethod
    def validate(cls, profile_info: Dict[str, str]):
        """
            Validates a Snowflake profile configuration.

            :param profile_info: Profile configuration to validate.

            :returns: Lists of errors and warnings.
        """
        
        errors = []
        warns = []

        if "account" not in profile_info:
            errmsg = f"The 'snowflake' profile must have an 'account' field."
            errors.append(errmsg)
        
        if "warehouse" not in profile_info:
            errmsg = f"The 'snowflake' profile must have an 'warehouse' field."
            errors.append(errmsg)
        
        if "database" not in profile_info:
            errmsg = f"The 'snowflake' profile must have an 'database' field."
            errors.append(errmsg)
        
        if "schema" not in profile_info:
            errmsg = f"The 'snowflake' profile must have an 'schema' field."
            errors.append(errmsg)
        
        if "credential" not in profile_info:
            errmsg = f"The 'snowflake' profile must have an 'credential' field."
            errors.append(errmsg)
        

        return errors, warns
