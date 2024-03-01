#!/usr/bin/python3
"""python script
- visits https://alx-intranet.hbtn.io/status.
- the oackage used is ulib
"""


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as alx:
        content = alx.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
