# Custom RustDesk clients for rd.sgohome.us

This fork includes a custom GitHub Actions workflow that builds RustDesk clients with a self-hosted default server.

## Default server

- ID server: `rd.sgohome.us`
- Public key: read from your RustDesk server file:

```bash
cat /mnt/user/appdata/rustdesk-server/data/id_ed25519.pub
```

The workflow patches this file at build time:

```text
libs/hbb_common/src/config.rs
```

It replaces:

```rust
pub const RENDEZVOUS_SERVERS: &[&str] = &[...];
pub const RS_PUB_KEY: &str = "...";
```

with your `rd.sgohome.us` server and your server public key.

## Recommended setup

Create a repository secret:

```text
RUSTDESK_RS_PUB_KEY
```

Value:

```text
content of /mnt/user/appdata/rustdesk-server/data/id_ed25519.pub
```

This avoids typing the key every time you run the workflow.

## Run the workflow

Open GitHub:

```text
Actions -> Build custom self-host RustDesk clients -> Run workflow
```

Inputs:

```text
id_server: rd.sgohome.us
public_key: leave empty if RUSTDESK_RS_PUB_KEY secret exists
build_windows: true
build_linux: true
build_macos: true
build_android: true
build_ios: false by default
```

Artifacts will be available in the workflow run:

```text
rustdesk-windows-x64-rd-sgohome-us
rustdesk-linux-x64-rd-sgohome-us
rustdesk-macos-rd-sgohome-us
rustdesk-android-rd-sgohome-us
rustdesk-ios-rd-sgohome-us
```

## Important notes

1. This does not commit your server public key into the repository.
2. Existing RustDesk installations may keep old local config. Clean install or run `rustdesk.exe --config <config-string>` if needed.
3. Unsigned Windows/macOS builds may show security warnings.
4. iOS requires Apple signing/provisioning for normal installation, so it is disabled by default.
5. RustDesk server should be exposed directly on ports 21115/21116/21117, not through normal Nginx Proxy Manager HTTP proxy.
