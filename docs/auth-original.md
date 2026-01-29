# Push: feat: auth.py original

## Overview

This documentation covers the initial implementation of the `auth.py` module, providing basic functionality for handling OAuth redirects, as introduced in the initial feature push.

## Usage

The primary function exposed allows simulating the initiation of an OAuth login flow by specifying the provider.

```python
from src.auth import login_oauth

# Example usage for Google
print(login_oauth('Google'))
# Expected output: Redirecting to Google...

# Example usage for GitHub
print(login_oauth('GitHub'))
# Expected output: Redirecting to GitHub...
```

## API Reference

### Functions

| Name | Description | Returns |
| :--- | :--- | :--- |
| `login_oauth(provider)` | Initiates the external redirection process for the specified OAuth provider. | A string indicating the redirection URL or status. |
