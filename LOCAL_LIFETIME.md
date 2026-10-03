# ANYISP Scanner — Local Lifetime Build

This build is configured for local/offline use by the project owner.

- No `/api/v1/activate` request is made.
- No `/api/v1/heartbeat` request is made.
- No `/api/v1/policy` request is made.
- A local encrypted, HMAC-protected lifetime entitlement is created on first run.
- The default engine assignment is V5.
- `days_remaining()` returns 36500 so engines display `UNLIMITED` where supported.
- Existing device/security integrity checks remain enabled.

## GitHub

The package can be uploaded as source code. Do not commit real API keys, private keys, passwords, or user data.
