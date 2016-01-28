"""
Top level script for boiler_plate.
"""

import os
from optparse import OptionParser

import boiler_plate


def main():
    """
    Run the boiler_plate server.
    """
    parser = OptionParser(usage="usage: %prog [options]",
                          version="%prog {0}".format(boiler_plate.__version__))
    _port = os.environ.get('PORT')
    if _port is None:
        _port = 5000
    parser.add_option("-d", "--debug",
                      action="store_true",
                      dest="debug",
                      default=False,
                      help="Run Flask in debug")
    parser.add_option("-p", "--port",
                      dest="port",
                      default=_port,
                      help="Set the port")
    parser.add_option("--host",
                      dest="host",
                      default="0.0.0.0",
                      help="The host IP.")
    (options, args) = parser.parse_args()
    boiler_plate.app.run(debug=options.debug, host=options.host, port=int(options.port))


if __name__ == "__main__":
    main()
