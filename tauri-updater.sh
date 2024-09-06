# References
# https://ratulmaharaj.com/posts/tauri-automatic-updates
# https://thatgurjot.com/til/tauri-auto-updater/

export TAURI_SIGNING_PRIVATE_KEY=/home/strider/.tauri/exampleTauri.key
export TAURI_SIGNING_PRIVATE_KEY_PASSWORD=SuperSecret987


PROJECT_NAME=example-tauri
PROJECT_VERSION=0.1.1
LATEST_HOST="strycore.com:/home/strider/sites/comandon/example/"

# Build with NO_STRIP to workaround this bug: https://github.com/tauri-apps/tauri/issues/8929
NO_STRIP=true pnpm tauri build

./gen_latest.py $PROJECT_VERSION
scp latest.json $LATEST_HOST