#!/usr/bin/env bash
pygmentize -S default -f html -a .codehilite > static/codehilite.css
python build-db.py
datasette til.db --template-dir templates --static static:static/
