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


class WellKnownAndValidationTests(unittest.TestCase):
    """Regression coverage for the wellknown singleton (clean-import blocker) and validation paths."""

    def setUp(self) -> None:
        from ccai.dataprofiles import wellknown
        self._wellknown = wellknown
        # Ensure a clean singleton so each test sees deterministic behavior.
        wellknown.DATAPROFILE_MANAGER_SINGLETON = None

    def tearDown(self) -> None:
        self._wellknown.DATAPROFILE_MANAGER_SINGLETON = None

    def test_wellknown_singleton_requires_args_on_first_call(self) -> None:
        from ccai.errors.exceptions import SemanticError
        with self.assertRaises(SemanticError):
            self._wellknown.DataProfileManagerSingleton()

    def test_wellknown_singleton_builds_with_args(self) -> None:
        manager = self._wellknown.DataProfileManagerSingleton(dataprofile_info=LANDSCAPE_DATA, dataprofile_uris=[])
        self.assertIsInstance(manager, DataProfileManager)
        self.assertIn("snowflake-example", manager.profiles)

    def test_lookup_missing_profile_raises_configuration_error(self) -> None:
        from ccai.errors.exceptions import ConfigurationError
        manager = DataProfileManager()
        manager.load_datasource_profiles(LANDSCAPE_DATA)
        with self.assertRaises(ConfigurationError):
            manager.lookup_profile("does-not-exist")

    def test_unknown_profile_field_raises_configuration_error(self) -> None:
        from ccai.errors.exceptions import ConfigurationError
        bad_data = {
            "dataprofiles": [
                {
                    "identifier": "bad-tcp",
                    "category": "basic-tcp",
                    "dbtype": "postgres",
                    "dbname": "testdb",
                    "host": "somedb.somecompany.com",
                    "port": 8888,
                    "credential": "dbadmin",
                    "bogus": "unexpected",
                }
            ]
        }
        manager = DataProfileManager()
        with self.assertRaises(ConfigurationError):
            manager.load_datasource_profiles(bad_data)

    def test_snowflake_without_schema_is_accepted(self) -> None:
        data = {
            "dataprofiles": [
                {
                    "identifier": "sf-no-schema",
                    "category": "snowflake",
                    "account": "some-account",
                    "warehouse": "some-warehouse",
                    "database": "some-database",
                    "credential": "dbadmin",
                }
            ]
        }
        manager = DataProfileManager()
        manager.load_datasource_profiles(data)
        profile = manager.lookup_profile("sf-no-schema")
        self.assertIsInstance(profile, SnowflakeProfile)
        self.assertIsNone(profile.schema)


if __name__ == "__main__":
    unittest.main()
