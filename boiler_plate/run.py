"""
Top level script for boilerplate.
"""


from boiler_plate import app


def main():
    app.run(debug=True, host="0.0.0.0")


if __name__ == "__main__":
    main()
