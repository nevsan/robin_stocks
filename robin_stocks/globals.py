"""Holds the session header and other global variables."""
import requests

# Keeps track on if the user is logged in or not.
LOGGED_IN = False
# The session object for making get and post requests.
# Override pool size for better parallelism
POOL_SIZE = 100
_session = requests.Session()
adapter = requests.adapters.HTTPAdapter(
    pool_connections=POOL_SIZE, pool_maxsize=POOL_SIZE
)
_session.mount("https://", adapter)
SESSION = _session
SESSION.headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip,deflate,br",
    "Accept-Language": "en-US,en;q=1",
    "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
    "X-Robinhood-API-Version": "1.315.0",
    "Connection": "keep-alive",
    "User-Agent": "*",
}
