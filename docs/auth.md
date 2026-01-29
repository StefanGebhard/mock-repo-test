# Push: feat: add auth

## Overview

This module introduces utility functions intended for simulating or testing OAuth redirection flows, specifically for testing environments. It provides helper functions to construct the necessary authorization URLs without executing actual secure network requests.

## Usage

The primary use case is generating a mock OAuth authorization URL for debugging or unit testing specific authentication paths.

### Example: Building an OAuth URL

This example demonstrates how to build a URL for the Google OAuth provider.

```python
from src.auth import build_oauth_url

client_id = "my_app_123"
redirect_uri = "https://test.app/callback"

# Build the URL
auth_url = build_oauth_url(
    provider="google", 
    client_id=client_id, 
    redirect_uri=redirect_uri,
    scope="profile email"
)

print(auth_url)
# Output: https://accounts.google.com/o/oauth2/v2/auth?client_id=my_app_123&redirect_uri=https%3A%2F%2Ftest.app%2Fcallback&response_type=code&scope=profile+email
```

### Example: Simulating a Redirect

The `login_oauth` function is designed to return a string representation of a redirect instruction, useful for logging or simple assertion in tests.

```python
from src.auth import login_oauth

redirect_message = login_oauth("github")
print(redirect_message)
# Output: Redirecting to github... https://github.com/login/oauth/authorize?client_id=test-client&redirect_uri=https%3A%2F%2Fexample.com%2Fcb&response_type=code&scope=openid
```

## API Reference

### Constants

| Name | Type | Description |
| :--- | :--- | :--- |
| `ALLOWED_PROVIDERS` | `set[str]` | A predefined set of OAuth providers supported by the helper functions: `{"google", "github", "facebook"}`. |

### Functions

#### `build_oauth_url(provider: str, client_id: str, redirect_uri: str, scope: str = "openid") -> str`

Constructs a full authorization URL string for a specified OAuth provider. This function raises a `ValueError` if the provider is not in `ALLOWED_PROVIDERS`.

**Parameters:**
- `provider` (str): The name of the OAuth provider (e.g., "google").
- `client_id` (str): The client ID registered with the provider.
- `redirect_uri` (str): The URI where the authorization server redirects the user back to.
- `scope` (str, optional): The requested OAuth scopes. Defaults to "openid".

**Returns:**
- `str`: The fully constructed, mock authorization URL.

#### `login_oauth(provider: str, client_id: str = "test-client", redirect_uri: str = "https://example.com/cb") -> str`

Generates a convenient string output containing the provider name and the corresponding test OAuth URL built using `build_oauth_url`. It uses default values for `client_id` and `redirect_uri` if not provided.

**Parameters:**
- `provider` (str): The name of the OAuth provider.
- `client_id` (str, optional): The client ID to use. Defaults to "test-client".
- `redirect_uri` (str, optional): The callback URI to use. Defaults to "https://example.com/cb".

**Returns:**
- `str`: A formatted string indicating the redirect action and the URL.