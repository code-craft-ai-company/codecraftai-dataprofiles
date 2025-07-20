
from automojo.dataprofiles.dataprofilemanager import DataProfileManager

from automojo.dataprofiles.couchdbprofile import CouchDbProfile
from automojo.dataprofiles.mongodbatlasprofile import MongoDBAtlasProfile
from automojo.dataprofiles.snowflakeprofile import SnowflakeProfile


def test_couchdb_profile(profile_mgr: DataProfileManager):

    datasource_profiles = profile_mgr.profiles

    profile_name = 'couchdb-example'
    assert profile_name in datasource_profiles, f"There should have been a '{profile_name}' profile."

    testprofile = profile_mgr.lookup_profile(profile_name)

    assert isinstance(testprofile, CouchDbProfile), "The datasource profile returned should have been an 'CouchDbProfile'"

    return


def test_mongodb_atlas_profile(profile_mgr: DataProfileManager):

    datasource_profiles = profile_mgr.profiles

    profile_name = 'mongodb-example'
    assert profile_name in datasource_profiles, f"There should have been a '{profile_name}' profile."

    testprofile = profile_mgr.lookup_profile(profile_name)

    assert isinstance(testprofile, MongoDBAtlasProfile), "The datasource profile returned should have been an 'MongoDBAtlasProfile'"

    return


def test_snowflake_profile(profile_mgr: DataProfileManager):

    datasource_profiles = profile_mgr.profiles

    profile_name = 'snowflake-example'
    assert profile_name in datasource_profiles, f"There should have been a '{profile_name}' profile."

    testprofile = profile_mgr.lookup_profile(profile_name)

    assert isinstance(testprofile, SnowflakeProfile), "The datasource profile returned should have been an 'SnowflakeProfile'"

    return


if __name__ == '__main__':
    from automojo.testbase.entrypoints import generic_test_entrypoint
    generic_test_entrypoint()
