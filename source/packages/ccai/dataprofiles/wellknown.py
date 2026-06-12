"""
    .. module:: wellknown
        :platform: Darwin, Linux, Unix, Windows
        :synopsis: Module that provides helper functions and singletons for
                    accessing data profile managers.

    .. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2025, Code Craft AI LLC"
__credits__ = []

from typing import List, Optional

from threading import RLock

from ccai.errors.exceptions import SemanticError

from ccai.dataprofiles.dataprofilemanager import DataProfileManager

DATAPROFILE_MANAGER_SINGLETON = None

SINGLETON_LOCK = RLock()


def DataProfileManagerSingleton(dataprofile_info: Optional[dict] = None, dataprofile_uris: Optional[List[str]] = None) -> DataProfileManager:
    """
        Instantiates and gets a global instance of the :class:`DataProfileManager` class.  The
        :class:`DataProfileManager` provides for management of data source connectivity information profiles.
    """
    global DATAPROFILE_MANAGER_SINGLETON

    if DATAPROFILE_MANAGER_SINGLETON is None:

        if dataprofile_info is None or dataprofile_uris is None:
             errmsg = "The first call to create the DataProfileManagerSingleton must include the dataprofile_info and dataprofile_uris parameters."
             raise SemanticError(errmsg)
        
        SINGLETON_LOCK.acquire()
        try:

                profilemgr = DataProfileManager()
                profilemgr.load_datasource_profiles(dataprofile_info, source_uris=dataprofile_uris)
                DATAPROFILE_MANAGER_SINGLETON = profilemgr
                
        finally:
            SINGLETON_LOCK.release()
    
    return DATAPROFILE_MANAGER_SINGLETON