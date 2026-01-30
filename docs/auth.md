# Push: feat: add auth

## Overview

This module introduces utility functions for simulating or building mock OAuth2 authorization URLs. This functionality is primarily intended for use in unit tests, demos, or specific integration scenarios where simulating the initial redirect step of an OAuth flow is required without performing actual network authentication.

## Usage

This feature exposes two primary functions: `build_oauth_url` for constructing the raw URL, and `login_oauth` which returns a formatted redirection message.

### Example: Building an OAuth URL

```python
from src.auth import build_oauth_url

client_id = "my-app-123"
client_secret = "my-secret-xyz" # Note: client_secret is generally NOT included in the initial GET request URL, but listed here for completeness if other optional params are needed.
redirect_uri = "https://myapp.com/auth/callback"

# Build URL for Google
google_url = build_oauth_url(
    provider="google",
    client_id=client_id,
    redirect_uri=redirect_uri,
    scope="email profile"
)
print(google_url)
# Output: https://accounts.google.com/o/oauth2/v2/auth?client_id=my-app-123&redirect_uri=https://myapp.com/auth/callback&response_type=code&scope=email profile

# Build URL for a default scope provider (e.g., GitHub)
github_url = build_oauth_url(
    provider="github",
    client_id=client_id,
    redirect_uri=redirect_uri
)
print(github_url)
# Output: https://github.com/login/oauth/authorize?client_id=my-app-123&redirect_uri=https://myapp.com/auth/callback&response_type=code&scope=openid
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

#### `build_oauth_url(provider: str, client_id: str, redirect_uri: str, scope: str = "openid", **kwargs) -> str`

Constructs a simulated OAuth 2.0 authorization URL based on the provided provider and credentials. Note that `client_secret` is typically used for the token exchange step and is **not** included in this initial authorization URL.

**Parameters:**
* `provider` (`str`): The name of the provider (must be in `ALLOWED_PROVIDERS`).
* `client_id` (`str`): Your application's client ID.
* `redirect_uri` (`str`): The URI where the authorization server will redirect the user.
* `scope` (`str`, optional): The requested OAuth scope(s). Defaults to `"openid"`.
* `**kwargs`: Allows passing any additional query parameters that the specific provider URL builder might require (e.g., `code_challenge` for PKCE).

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