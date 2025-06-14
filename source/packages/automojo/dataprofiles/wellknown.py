"""
    .. module:: wellknown
        :platform: Darwin, Linux, Unix, Windows
        :synopsis: Module that provides helper functions and singletons for
                    accessing data profile managers.

    .. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2025, Automation Mojo LLC"
__credits__ = []


from threading import RLock

from automojo.foundation.collections.wellknown import ContextSingleton
from automojo.foundation.collections.contextpaths import ContextPaths
from automojo.foundation.collections.mergemap import MergeMap

from automojo.dataprofiles.dataprofilemanager import DataProfileManager

from automojo.foundation.configuration.configurationmaps import CONFIGURATION_MAPS

DATAPROFILE_MANAGER_SINGLETON = None

SINGLETON_LOCK = RLock()


def DataProfileManagerSingleton() -> DataProfileManager:
    """
        Instantiates and gets a global instance of the :class:`DataProfileManager` class.  The
        :class:`DataProfileManager` provides for management of data source connectivity information profiles.
    """
    global DATAPROFILE_MANAGER_SINGLETON

    if DATAPROFILE_MANAGER_SINGLETON is None:
        SINGLETON_LOCK.acquire()
        try:

            if DATAPROFILE_MANAGER_SINGLETON is None:
                ctx = ContextSingleton()

                dataprofiles_config = None
                config_uris = None

                if CONFIGURATION_MAPS.DATAPROFILE_CONFIGURATION_MAP is not None and \
                   len(CONFIGURATION_MAPS.DATAPROFILE_CONFIGURATION_MAP) > 0:
                    configmap: MergeMap = CONFIGURATION_MAPS.DATAPROFILE_CONFIGURATION_MAP
                    if "dataprofiles" in configmap:
                        dataprofiles_config = configmap

                    config_uris = ctx.lookup(ContextPaths.CONFIG_DATAPROFILE_URIS, [])

                elif CONFIGURATION_MAPS.LANDSCAPE_CONFIGURATION_MAP is not None and \
                    len(CONFIGURATION_MAPS.LANDSCAPE_CONFIGURATION_MAP) > 0:
                    configmap: MergeMap = CONFIGURATION_MAPS.LANDSCAPE_CONFIGURATION_MAP
                    if "dataprofiles" in configmap:
                        dataprofiles_config = configmap

                    config_uris = ctx.lookup(ContextPaths.CONFIG_LANDSCAPE_URIS, [])

                profilemgr = DataProfileManager()
                profilemgr.load_datasource_profiles(dataprofiles_config, source_uris=config_uris)
                DATAPROFILE_MANAGER_SINGLETON = profilemgr
                
        finally:
            SINGLETON_LOCK.release()
    
    return DATAPROFILE_MANAGER_SINGLETON