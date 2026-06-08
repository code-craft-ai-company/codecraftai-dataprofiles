"""
    Testbase tests for the data profile manager integration points.

    These tests validate that :class:`DataProfileManager` loads each known
    datasource profile and resolves it to the expected profile type.
"""

from __future__ import annotations

from ccai.dataprofiles.couchdbprofile import CouchDbProfile
from ccai.dataprofiles.databasebasicsocketprofile import DatabaseBasicSocketProfile
from ccai.dataprofiles.databasebasictcpprofile import DatabaseBasicTcpProfile
from ccai.dataprofiles.dataprofilemanager import DataProfileManager
from ccai.dataprofiles.mongodbatlasprofile import MongoDBAtlasProfile
from ccai.dataprofiles.snowflakeprofile import SnowflakeProfile


LANDSCAPE_DATA = {
    "dataprofiles": [
        {
            "identifier": "basic-tcp-example",
            "category": "basic-tcp",
            "dbtype": "postgres",
            "dbname": "testdb",
            "host": "somedb.somecompany.com",
            "port": 8888,
            "credential": "dbadmin",
        },
        {
            "identifier": "basic-socket-example",
            "category": "basic-socket",
            "dbtype": "postgres",
            "dbname": "testdb",
            "socket": "/var/run/postgresql/.s.PGSQL.5432",
            "credential": "dbadmin",
        },
        {
            "identifier": "mongodb-example",
            "category": "mongodb-atlas",
            "connection": "mongodb+srv://<username>:<password>@automation-mojo-db.q0jpg0g.mongodb.net/",
            "credential": "dbadmin",
        },
        {
            "identifier": "couchdb-example",
            "category": "couchdb",
            "dbname": "testdb",
            "host": "somedb.somecompany.com",
            "port": 8888,
            "credential": "dbadmin",
        },
        {
            "identifier": "snowflake-example",
            "category": "snowflake",
            "account": "some-account",
            "warehouse": "some-warehouse",
            "database": "some-database",
            "schema": "some-schema",
            "credential": "dbadmin",
        },
    ]
}


def _establish_env() -> DataProfileManager:
    """
        Replicate the original ``setUp`` lifecycle hook by creating a fresh
        :class:`DataProfileManager` and loading the landscape datasource
        profiles into it.

        :returns: A ``DataProfileManager`` with the landscape profiles loaded.
    """
    profile_mgr = DataProfileManager()
    profile_mgr.load_datasource_profiles(LANDSCAPE_DATA)
    return profile_mgr


def test_couchdb_profile_is_registered() -> None:
    """
        Verify the ``couchdb-example`` profile is registered and resolves to a
        :class:`CouchDbProfile`.
    """
    profile_mgr = _establish_env()

    profile_name = "couchdb-example"
    assert profile_name in profile_mgr.profiles
    profile = profile_mgr.lookup_profile(profile_name)
    assert isinstance(profile, CouchDbProfile)
    return


def test_basic_tcp_profile_is_registered() -> None:
    """
        Verify the ``basic-tcp-example`` profile is registered and resolves to
        a :class:`DatabaseBasicTcpProfile`.
    """
    profile_mgr = _establish_env()

    profile_name = "basic-tcp-example"
    assert profile_name in profile_mgr.profiles
    profile = profile_mgr.lookup_profile(profile_name)
    assert isinstance(profile, DatabaseBasicTcpProfile)
    return


def test_basic_socket_profile_is_registered() -> None:
    """
        Verify the ``basic-socket-example`` profile is registered and resolves
        to a :class:`DatabaseBasicSocketProfile`.
    """
    profile_mgr = _establish_env()

    profile_name = "basic-socket-example"
    assert profile_name in profile_mgr.profiles
    profile = profile_mgr.lookup_profile(profile_name)
    assert isinstance(profile, DatabaseBasicSocketProfile)
    return


def test_mongodb_atlas_profile_is_registered() -> None:
    """
        Verify the ``mongodb-example`` profile is registered and resolves to a
        :class:`MongoDBAtlasProfile`.
    """
    profile_mgr = _establish_env()

    profile_name = "mongodb-example"
    assert profile_name in profile_mgr.profiles
    profile = profile_mgr.lookup_profile(profile_name)
    assert isinstance(profile, MongoDBAtlasProfile)
    return


def test_snowflake_profile_is_registered() -> None:
    """
        Verify the ``snowflake-example`` profile is registered and resolves to
        a :class:`SnowflakeProfile`.
    """
    profile_mgr = _establish_env()

    profile_name = "snowflake-example"
    assert profile_name in profile_mgr.profiles
    profile = profile_mgr.lookup_profile(profile_name)
    assert isinstance(profile, SnowflakeProfile)
    return
