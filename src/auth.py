"""Simple OAuth redirect helper used in tests."""

ALLOWED_PROVIDERS = {"google", "github", "facebook"}


def build_oauth_url(provider: str, client_id: str, redirect_uri: str, scope: str = "openid") -> str:
    """
    Build a simple OAuth authorization URL for test purposes.
    Does not perform any network requests or real OAuth flows.
    """
    if provider not in ALLOWED_PROVIDERS:
        raise ValueError(f"Unknown provider: {provider!r}")
    # Fake authorization endpoint per provider for tests
    auth_endpoints = {
        "google": "https://accounts.google.com/o/oauth2/v2/auth",
        "github": "https://github.com/login/oauth/authorize",
        "facebook": "https://www.facebook.com/v10.0/dialog/oauth",
    }
    base = auth_endpoints[provider]
    return f"{base}?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope={scope}"


def login_oauth(provider: str, client_id: str = "test-client", redirect_uri: str = "https://example.com/cb") -> str:
    """
    Return a redirect message containing a test OAuth URL.
    Intended for unit tests and commit/demo usage.
    """
    url = build_oauth_url(provider, client_id, redirect_uri)
    return f"Redirecting to {provider}... {url}"