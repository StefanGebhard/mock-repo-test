# Push: feat: add auth

## Overview

This module introduces utility functions for simulating or building mock OAuth2 authorization URLs. This functionality is primarily intended for use in unit tests, demos, or specific integration scenarios where simulating the initial redirect step of an OAuth flow is required without performing actual network authentication.

## Usage

This feature exposes two primary functions: `build_oauth_url` for constructing the raw URL, and `login_oauth` which returns a formatted redirection message.

### Example: Building an OAuth URL

```python
from src.auth import build_oauth_url

client_id = "my-app-123"
redirect_uri = "https://myapp.com/auth/callback"
state_param = "unique-csrf-token-123"

# Build URL for Google
google_url = build_oauth_url(
    provider="google",
    client_id=client_id,
    redirect_uri=redirect_uri,
    scope="email profile",
    state=state_param
)
print(google_url)
# Output: https://accounts.google.com/o/oauth2/v2/auth?client_id=my-app-123&redirect_uri=https://myapp.com/auth/callback&response_type=code&scope=email+profile&state=unique-csrf-token-123

# Build URL for a default scope provider (e.g., GitHub)
github_url = build_oauth_url(
    provider="github",
    client_id=client_id,
    redirect_uri=redirect_uri,
    state=state_param
)
print(github_url)
# Output: https://github.com/login/oauth/authorize?client_id=my-app-123&redirect_uri=https://myapp.com/cb&response_type=code&scope=openid&state=unique-csrf-token-123
```

### Example: Simulating a Login Redirect

```python
from src.auth import login_oauth

redirect_message = login_oauth("github")
print(redirect_message)
# Output: Redirecting to github... https://github.com/login/oauth/authorize?client_id=test-client&redirect_uri=https://example.com/cb&response_type=code&scope=openid
```

## API Reference

### Constants

| Name | Type | Description |
| :--- | :--- | :--- |
| `ALLOWED_PROVIDERS` | `Set[str]` | A set containing recognized OAuth providers: `{"google", "github", "facebook"}`. |

### Functions

#### `build_oauth_url(provider: str, client_id: str, redirect_uri: str, scope: str = "openid", state: str = "") -> str`

Constructs a simulated OAuth 2.0 authorization URL based on the provided provider and credentials. A non-empty `state` parameter is highly recommended for testing CSRF protection.

**Parameters:**
* `provider` (`str`): The name of the provider (must be in `ALLOWED_PROVIDERS`).
* `client_id` (`str`): Your application's client ID.
* `redirect_uri` (`str`): The URI where the authorization server will redirect the user.
* `scope` (`str`, optional): The requested OAuth scope(s). Defaults to `"openid"`.
* `state` (`str`, optional): The opaque value used by the client to maintain state between the request and callback. Defaults to an empty string.

**Returns:**
* `str`: The fully constructed authorization URL.

**Raises:**
* `ValueError`: If the provided `provider` is not in `ALLOWED_PROVIDERS`.

#### `login_oauth(provider: str, client_id: str = "test-client", redirect_uri: str = "https://example.com/cb") -> str`

Generates a descriptive string message containing a test OAuth URL, useful for logging or visual confirmation during testing.

**Parameters:**
* `provider` (`str`): The name of the provider.
* `client_id` (`str`, optional): The client ID to use. Defaults to `"test-client"`.
* `redirect_uri` (`str`, optional): The redirect URI to use. Defaults to `"https://example.com/cb"`.

**Returns:**
* `str`: A formatted string indicating the redirection target.