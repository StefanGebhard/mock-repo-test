# Add Database Connection Pooling

## Overview
This module introduces a new `DB` class designed to handle database connections via a connection pool. This change improves performance by reducing the overhead of repeatedly opening and closing individual connections, allowing for efficient reuse of existing connections across the application. The primary goal is to enhance scalability and manage database resource utilization effectively.

## Usage
The `DB` class provides a straightforward interface for establishing connections. Here is a basic example of how to use it:

```python
from src.db import DB

# Instantiate the database connection manager
db = DB()

# Connect to the database pool
db.connect()
# Output: Connected to pool
```

In a real-world application, the `connect` method would likely be integrated into a connection pool management system, establishing a pool of connections at application startup. The current implementation includes a brief sleep period before establishing the next connection to simulate connection establishment latency or to prevent rapid successive connection attempts.

## API Reference
### DB Class
The `DB` class encapsulates the database connection pooling functionality.

#### Methods
- `connect(self)`: Initiates a connection to the database connection pool. This method is currently implemented as a placeholder that prints a confirmation message after a brief sleep, simulating connection establishment. In a production environment, it would establish a connection to a configured database and manage the connection lifecycle.

## Implementation Notes
The current implementation is a foundational step. Future enhancements should include:
- Configuration of database credentials and connection pool parameters (e.g., pool size, timeout).
- Methods to acquire and release connections from the pool.
- Integration with transaction management and error handling.
- Support for multiple database dialects (e.g., PostgreSQL, MySQL).

For further details on architectural updates, refer to the updated architecture documentation.