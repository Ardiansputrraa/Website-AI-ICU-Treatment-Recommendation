set -eu

export PYTHONUNBUFFERED=true

VIRTUALENV=.data/venv

if [ ! -d $VIRTUALENV ]; then
  python3 -m venv $VIRTUALENV
fi

if [ ! -f $VIRTUALENV/bin/pip ]; then
  curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py | $VIRTUALENV/bin/python
fi

$VIRTUALENV/bin/pip install -r requirements.txt

if [ -f tailwind.config.js ]; then
  echo "Building Tailwind CSS..."
  npx tailwindcss -i ./src/input.css -o ./static/output.css --watch &
fi

$VIRTUALENV/bin/python3 app.py
