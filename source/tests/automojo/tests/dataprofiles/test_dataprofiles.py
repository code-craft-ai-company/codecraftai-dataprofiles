"""Unit tests for the data profile manager integration points."""

from __future__ import annotations

import unittest

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


class DataProfileManagerTests(unittest.TestCase):
    """Tests that validate DataProfileManager loads known datasource profiles."""

    def setUp(self) -> None:  # noqa: D401 - standard unittest lifecycle hook.
        self.profile_mgr = DataProfileManager()
        self.profile_mgr.load_datasource_profiles(LANDSCAPE_DATA)

    def test_couchdb_profile_is_registered(self) -> None:
        profile_name = "couchdb-example"
        self.assertIn(profile_name, self.profile_mgr.profiles)
        profile = self.profile_mgr.lookup_profile(profile_name)
        self.assertIsInstance(profile, CouchDbProfile)

    def test_basic_tcp_profile_is_registered(self) -> None:
        profile_name = "basic-tcp-example"
        self.assertIn(profile_name, self.profile_mgr.profiles)
        profile = self.profile_mgr.lookup_profile(profile_name)
        self.assertIsInstance(profile, DatabaseBasicTcpProfile)

    def test_basic_socket_profile_is_registered(self) -> None:
        profile_name = "basic-socket-example"
        self.assertIn(profile_name, self.profile_mgr.profiles)
        profile = self.profile_mgr.lookup_profile(profile_name)
        self.assertIsInstance(profile, DatabaseBasicSocketProfile)

    def test_mongodb_atlas_profile_is_registered(self) -> None:
        profile_name = "mongodb-example"
        self.assertIn(profile_name, self.profile_mgr.profiles)
        profile = self.profile_mgr.lookup_profile(profile_name)
        self.assertIsInstance(profile, MongoDBAtlasProfile)

    def test_snowflake_profile_is_registered(self) -> None:
        profile_name = "snowflake-example"
        self.assertIn(profile_name, self.profile_mgr.profiles)
        profile = self.profile_mgr.lookup_profile(profile_name)
        self.assertIsInstance(profile, SnowflakeProfile)


if __name__ == "__main__":
    unittest.main()
