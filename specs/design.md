# AutoMojo DataProfiles Package Design Document

## Overview

The `automojo-dataprofiles` package provides a structured framework for managing data source connectivity profiles used by Automation Mojo utilities. This package enables standardized configuration and access to various database and data storage systems through a unified profile management system.

## Architecture

### Core Components

#### 1. Base Profile System
- **BaseDataProfile**: Abstract base class that defines the common interface for all data source profiles
- Provides fundamental properties: `identifier`, `category`, and optional `credential`
- Implements validation framework for profile configurations

#### 2. Profile Types
The package supports multiple specialized profile types for different data sources:

- **DatabaseBasicSocketProfile**: For databases accessed via Unix sockets
- **DatabaseBasicTcpProfile**: For databases accessed via TCP host/port connections  
- **CouchDbProfile**: Specialized profile for CouchDB instances
- **MongoDBAtlasProfile**: Cloud-specific profile for MongoDB Atlas deployments
- **SnowflakeProfile**: Enterprise data warehouse profile for Snowflake

#### 3. Management Layer
- **DataProfileManager**: Central manager for loading, validating, and accessing profiles
- **Singleton Pattern**: Global access via `DataProfileManagerSingleton()` function
- Configuration integration with the broader AutoMojo framework

## Class Hierarchy

```
BaseDataProfile (Abstract Base)
├── DatabaseBasicSocketProfile
├── DatabaseBasicTcpProfile  
├── CouchDbProfile
├── MongoDBAtlasProfile
└── SnowflakeProfile
```

## Profile Categories

### Basic Database Profiles

#### DatabaseBasicSocketProfile
- **Category**: `basic-socket`
- **Use Case**: Local database connections via Unix sockets
- **Key Properties**: `dbtype`, `dbname`, `socket`, `credential`
- **Validation**: Requires all core fields to be present

#### DatabaseBasicTcpProfile  
- **Category**: `basic-tcp`
- **Use Case**: Network database connections via TCP
- **Key Properties**: `host`, `port`, `dbtype`, `dbname`, `credential`
- **Validation**: Requires host, port, and database type information

### Specialized Database Profiles

#### CouchDbProfile
- **Category**: `couchdb`
- **Use Case**: CouchDB document database connections
- **Key Properties**: `host`, `port`, `scheme`, `dbname`, `credential`
- **Features**: 
  - Connection string generation with credential interpolation
  - Support for HTTP/HTTPS schemes
  - Database-specific validation

#### MongoDBAtlasProfile
- **Category**: `mongodb-atlas`
- **Use Case**: MongoDB Atlas cloud database connections
- **Key Properties**: `connection` (template string), `credential`
- **Features**:
  - Template-based connection strings with placeholder replacement
  - Cloud-optimized configuration
  - Credential interpolation for `<username>` and `<password>` placeholders

#### SnowflakeProfile
- **Category**: `snowflake`
- **Use Case**: Snowflake data warehouse connections
- **Key Properties**: `account`, `warehouse`, `database`, `schema`, `parameters`, `credential`
- **Features**:
  - Enterprise data warehouse specific configuration
  - Optional schema and connection parameters
  - Account-based identification system

## Design Patterns

### 1. Factory Pattern
The `DataProfileManager` uses a factory pattern to instantiate the correct profile type based on the `category` field in configuration data.

### 2. Validation Strategy
Each profile class implements a `validate()` class method that returns lists of errors and warnings, enabling comprehensive configuration validation before instantiation.

### 3. Singleton Pattern
Global access to the profile manager is provided through a thread-safe singleton implementation with lazy initialization.

### 4. Template Method Pattern
Base validation is performed in `BaseDataProfile.validate()`, with specialized validation in each concrete class.

## Configuration Integration

### Profile Loading
- Profiles are loaded from configuration dictionaries via `load_datasource_profiles()`
- Supports multiple configuration sources with URI tracking
- Integrates with the broader AutoMojo configuration system

### Validation Framework
- Two-phase validation: base validation followed by profile-specific validation
- Comprehensive error and warning collection
- Configuration source tracking for debugging

### Error Handling
- Custom `ConfigurationError` exceptions for configuration issues
- Detailed error messages with source URI information
- Graceful handling of missing or invalid profiles

## Dependencies

### External Dependencies
The package references several AutoMojo framework components:
- `automojo.errors.exceptions.ConfigurationError`
- `automojo.interfaces.ibasiccredential.IBasicCredential`
- `automojo.presence.wellknown.ContextSingleton`
- `automojo.presence.contextpaths.ContextPaths`
- `automojo.xmodules.xcollections.mergemap.MergeMap`
- `automojo.configuration.configurationmaps.CONFIGURATION_MAPS`

### Internal Dependencies
- Standard Python libraries: `typing`, `logging`, `os`, `threading`
- No external third-party dependencies

## Usage Patterns

### Profile Definition
Profiles are typically defined in configuration files and loaded at runtime:

```python
profile_config = {
    "identifier": "my-database",
    "category": "basic-tcp",
    "host": "localhost",
    "port": 5432,
    "dbtype": "postgresql",
    "dbname": "testdb",
    "credential": "db-creds"
}
```

### Profile Access
Profiles are accessed through the manager singleton:

```python
manager = DataProfileManagerSingleton()
profile = manager.lookup_profile("my-database")
```

### Connection String Generation
Specialized profiles provide connection string generation:

```python
# For CouchDB
conn_str = couchdb_profile.connection_string(credential_obj)

# For MongoDB Atlas  
conn_str = atlas_profile.connection_string(credential_obj)
```

## Extensibility

### Adding New Profile Types
1. Inherit from `BaseDataProfile`
2. Define a unique `category` class attribute
3. Implement required properties and validation
4. Add factory support in `DataProfileManager`
5. Optionally implement connection string generation

### Validation Extensions
- Custom validation logic can be added to any profile class
- Validation follows the error/warning list pattern
- Base validation is automatically inherited

## Security Considerations

### Credential Management
- Profiles store credential references, not actual credentials
- Credential resolution is handled by external credential management systems
- Connection strings are generated at runtime with credential interpolation

### Configuration Security
- Profile configurations should not contain sensitive data directly
- All sensitive information should be referenced via credential identifiers
- Configuration source URIs are tracked for audit purposes

## Testing Strategy

### Unit Testing
- Each profile class should have comprehensive unit tests
- Validation logic should be thoroughly tested
- Manager functionality requires integration testing

### Integration Testing
- Profile loading from various configuration sources
- Singleton behavior and thread safety
- Error handling and configuration validation

### Test Organization
Following the repository conventions:
- Test files mirror source hierarchy
- Tests located in `source/testroots/automojo/tests/singlehost/dataprofiles/`
- Use `testbase` framework for test execution

## Future Enhancements

### Potential Extensions
1. **Dynamic Profile Discovery**: Auto-discovery of profile types via plugins
2. **Profile Inheritance**: Support for profile templates and inheritance
3. **Connection Pooling**: Integration with connection pool management
4. **Encryption Support**: Built-in support for encrypted connections
5. **Health Checking**: Profile-aware connection health monitoring

### Configuration Enhancements
1. **Schema Validation**: JSON Schema validation for profile configurations
2. **Environment Interpolation**: Support for environment variable substitution
3. **Profile Versioning**: Version management for profile configurations
4. **Hot Reloading**: Dynamic profile reloading without restart

## Conclusion

The AutoMojo DataProfiles package provides a robust, extensible framework for managing data source connectivity information. Its design emphasizes type safety, validation, and integration with the broader AutoMojo ecosystem while maintaining simplicity and ease of use. The modular architecture supports both current requirements and future extensibility needs.