# Push: feat original auth.py

## Overview

This document describes the initial implementation of the core authentication module (`src/auth.py`). This feature introduces preliminary support for OAuth login redirects.

## Usage

The primary function provided allows simulating the initiation of an OAuth login flow by generating the appropriate redirection string.

### Example

To initiate a login via Google, call `login_oauth` with the provider name:

```python
from src.auth import login_oauth

# Initiate Google OAuth login
redirect_url = login_oauth('Google')
print(redirect_url)
# Expected Output: Redirecting to Google...
```

## API Reference

### Functions

| Name | Signature | Description |
| :--- | :--- | :--- |
| `login_oauth` | `login_oauth(provider: str) -> str` | Generates the redirection trigger string for the specified OAuth provider. |
