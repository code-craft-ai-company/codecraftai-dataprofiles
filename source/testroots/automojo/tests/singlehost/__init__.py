

from typing import Generator

import os
import tempfile
import yaml

from automojo.dataprofiles.dataprofilemanager import DataProfileManager
from automojo import testbase

LANDSCAPE_CONTENT = """
dataprofiles:
    -   identifier: basic-database
        category: basic-tcp
        dbtype: postgres
        dbname: testdb
        host: somedb.somecompany.com
        port: 8888
        credential: dbadmin
    -   identifier: mongodb-example
        category: mongodb-atlas
        connection: "mongodb+srv://<username>:<password>@automation-mojo-db.q0jpg0g.mongodb.net/"
        credential: dbadmin
    -   identifier: couchdb-example
        category: couchdb
        dbname: testdb
        host: somedb.somecompany.com
        port: 8888
        credential: dbadmin
    -   identifier: snowflake-example
        category: snowflake
        account: some-account 
        warehouse: some-warehouse
        database: some-database
        schema: some-schema
        credential: dbadmin
"""

@testbase.register.resource_factory()
def create_dataprofilemanager() -> Generator[DataProfileManager, None, None]:

    landscape_file = tempfile.mktemp(suffix=".yaml")

    with open(landscape_file, 'w') as cf:
        cf.write(LANDSCAPE_CONTENT)

    landscape_info = None
    with open(landscape_file, 'r') as cf:
        landscape_info = yaml.safe_load(cf)

    profile_mgr = DataProfileManager()
    profile_mgr.load_datasource_profiles(landscape_info, source_uris=[landscape_file])

    yield profile_mgr

    os.remove(landscape_file)


testbase.originate.parameter(create_dataprofilemanager, identifier="profile_mgr")


