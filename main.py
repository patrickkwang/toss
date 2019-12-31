#!/usr/bin/env python
"""Run TOS server."""
import argparse
from toss.server import app

parser = argparse.ArgumentParser(description='Start TOS server.')
parser.add_argument('--host', default='0.0.0.0', type=str)
parser.add_argument('--port', default=7055, type=int)

args = parser.parse_args()

app.run(
    host=args.host,
    port=args.port,
    debug=False,
)
