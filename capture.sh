#!/bin/bash

# --- FIX 1: Set the Locale to UTF-8 ---
# This ensures the shell knows how to handle special characters.
# Use the generic C.UTF-8 locale instead of en_US
export LANG=C.UTF-8
export LC_ALL=C.UTF-8


# 3. Start Xvfb on a specific display
#    -ac: Disables access control (allows xterm to connect without auth cookies)
Xvfb :9922 -screen 0 844x472x24 -ac &
PID_XVFB=$!
export DISPLAY=:9922

# 4. ROBUST WAIT: Loop until the display is actually ready
echo "Waiting for Xvfb..."
for i in {1..10}; do
  if xdpyinfo -display :9922 >/dev/null 2>&1; then
    echo "Display :9922 is ready!"
    break
  fi
  sleep 1
done


echo "Launching TUI"


# 5. Run xterm (Now it is safe)
#    -fa 'Monospace': Relies on fontconfig. If this fails, install fonts-dejavu
st -g 120x36 -e ./run_tui.sh &
PID_APP=$!

echo "Waiting 5 seconds"

# 6. Wait for your app to render (adjust as needed)
sleep 5


echo "Capturing screenshot"

# 7. Capture
scrot screenshot.png



# Cleanup
kill $PID_APP
kill $PID_XVFB


echo "Done"
