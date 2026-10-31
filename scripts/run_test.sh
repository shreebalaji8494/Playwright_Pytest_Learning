#!/usr/bin/env bash
set -e

# Browser comes from the first argument, then the BROWSER env var, then defaults to chrome
BROWSER_NAME="${1:-${browser:-chrome}}"

python -m venv venv
if [ -f venv/Scripts/activate ]; then
  source venv/Scripts/activate
else
  source venv/bin/activate
fi  # Windows venv layout (Git Bash)
pip install -r requirements.txt
case "$BROWSER_NAME" in
  chrome)
    python -m playwright install chrome
    BROWSER_ARGS="--browser chromium --browser-channel chrome"
    ;;
  edge)
    python -m playwright install msedge
    BROWSER_ARGS="--browser chromium --browser-channel msedge"
    ;;
  firefox)
    python -m playwright install firefox
    BROWSER_ARGS="--browser firefox"
    ;;
  webkit)
    python -m playwright install webkit
    BROWSER_ARGS="--browser webkit"
    ;;
  *)
    echo "Unsupported browser: $BROWSER_NAME (use chrome, edge, firefox or webkit)"
    exit 1
    ;;
esac

echo "Running tests on: $BROWSER_NAME"
pytest $BROWSER_ARGS --html=reports/report.html --tracing on -n 5 --screenshot only-on-failure