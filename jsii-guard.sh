#!/data/data/com.termux/files/usr/bin/bash
export PYTHONUNBUFFERED=1
export NODE_NO_WARNINGS=1
exec node "$@" 2> >(grep -v "ExperimentalWarning" >&2)
