# Push: feat: add auth

## Overview

This module introduces utility functions for building mock OAuth authorization URLs. This feature is primarily intended for use in testing environments, demonstrations, or unit tests where a full OAuth flow setup is unnecessary, allowing quick generation of the expected authorization endpoint query string.

## Usage

The primary utility is generating a standardized, provider-specific OAuth URL based on required parameters.

### Building an OAuth URL

The `build_oauth_url` function constructs the necessary authorization URL. Note that real token exchange or user redirection is *not* handled by this utility.

```python
from src.auth import build_oauth_url

# Example for Google
goggle_url = build_oauth_url(
    provider="google",
    client_id="12345-abcdef.apps.googleusercontent.com",
    redirect_uri="https://myapp.com/auth/callback",
    scope="email profile"
)

print(goggle_url)
# Expected Output: https://accounts.google.com/o/oauth2/v2/auth?client_id=12345-abcdef.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fmyapp.com%2Fauth%2Fcallback&response_type=code&scope=email profile
```

### Simulating a Redirect

The `login_oauth` function provides a higher-level wrapper that returns a string message simulating a redirection sequence, useful for quick testing output.

```python
from src.auth import login_oauth

# Using default test client ID and redirect URI
facebook_login = login_oauth(provider="facebook")
print(facebook_login)
# Output: Redirecting to facebook... https://www.facebook.com/v10.0/dialog/oauth?client_id=test-client&redirect_uri=https://example.com/cb&response_type=code&scope=openid
```

## API Reference

This module exports the following public functions and constants:

### Constants

*   `ALLOWED_PROVIDERS`: A set containing strings of supported OAuth providers (`{"google", "github", "facebook"}`).

### Functions

#### `build_oauth_url(provider: str, client_id: str, redirect_uri: str, scope: str = "openid") -> str`

Constructs a mock OAuth authorization URL.

*   **Parameters**:
    *   `provider` (str): The identity provider (must be in `ALLOWED_PROVIDERS`).
    *   `client_id` (str): The application's client ID.
    *   `redirect_uri` (str): The URI where the user will be redirected after authorization.
    *   `scope` (str, optional): The requested OAuth scopes. Defaults to `"openid"`.
*   **Returns**:
    *   `str`: The fully constructed authorization URL query string.
*   **Raises**:
    *   `ValueError`: If the provided `provider` is not supported.

#### `login_oauth(provider: str, client_id: str = "test-client", redirect_uri: str = "https://example.com/cb") -> str`

Generates a formatted string message indicating a simulated OAuth redirection using testing defaults.

*   **Parameters**:
    *   `provider` (str): The identity provider name.
    *   `client_id` (str, optional): Client ID to use. Defaults to `"test-client"`.
    *   `redirect_uri` (str, optional): Redirect URI to use. Defaults to `"https://example.com/cb"`.
*   **Returns**:
    *   `str`: A formatted string containing the simulated redirect destination.