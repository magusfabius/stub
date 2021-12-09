Skip to main content
 Participate in the official Python Developers Survey  Take the 2021 survey!
PyPI
Search PyPI
Search projects
Search
Help Sponsors Log in Register
humanfriendly 10.0
pip install humanfriendlyCopy PIP instructions
Latest version
Released: Sep 17, 2021

Human friendly output for text interfaces using Python

Navigation
 Project description
 Release history
 Download files
Project links
Homepage
Statistics
View statistics for this project via Libraries.io, or by using our public dataset on Google BigQuery

Meta
License: MIT License (MIT)

Author: Peter Odding

Requires: Python >=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*

Maintainers
Avatar for xolox from gravatar.com xolox
Classifiers
Development Status
6 - Mature
Environment
Console
Framework
Sphinx :: Extension
Intended Audience
Developers
System Administrators
License
OSI Approved :: MIT License
Natural Language
English
Programming Language
Python
Python :: 2
Python :: 2.7
Python :: 3
Python :: 3.5
Python :: 3.6
Python :: 3.7
Python :: 3.8
Python :: 3.9
Python :: Implementation :: CPython
Python :: Implementation :: PyPy
Topic
Communications
Scientific/Engineering :: Human Machine Interfaces
Software Development
Software Development :: Libraries :: Python Modules
Software Development :: User Interfaces
System :: Shells
System :: System Shells
System :: Systems Administration
Terminals
Text Processing :: General
Text Processing :: Linguistic
Utilities
Slack
Slack is a maintaining sponsor of the Python Software Foundation.

Project description
https://github.com/xolox/python-humanfriendly/actions/workflows/test.yml/badge.svg?branch=master https://codecov.io/gh/xolox/python-humanfriendly/branch/master/graph/badge.svg?token=jYaj4T74TU
The functions and classes in the humanfriendly package can be used to make text interfaces more user friendly. Some example features:

Parsing and formatting numbers, file sizes, pathnames and timespans in simple, human friendly formats.
Easy to use timers for long running operations, with human friendly formatting of the resulting timespans.
Prompting the user to select a choice from a list of options by typing the option’s number or a unique substring of the option.
Terminal interaction including text styling (ANSI escape sequences), user friendly rendering of usage messages and querying the terminal for its size.
The humanfriendly package is currently tested on Python 2.7, 3.5+ and PyPy (2.7) on Linux and macOS. While the intention is to support Windows as well, you may encounter some rough edges.

Getting started
Command line
A note about size units
Windows support
Contact
License
Getting started
It’s very simple to start using the humanfriendly package:

>>> from humanfriendly import format_size, parse_size
>>> from humanfriendly.prompts import prompt_for_input
>>> user_input = prompt_for_input("Enter a readable file size: ")

  Enter a readable file size: 16G

>>> num_bytes = parse_size(user_input)
>>> print(num_bytes)
16000000000
>>> print("You entered:", format_size(num_bytes))
You entered: 16 GB
>>> print("You entered:", format_size(num_bytes, binary=True))
You entered: 14.9 GiB
To get a demonstration of supported terminal text styles (based on ANSI escape sequences) you can run the following command:

$ humanfriendly --demo
Command line
Usage: humanfriendly [OPTIONS]

Human friendly input/output (text formatting) on the command line based on the Python package with the same name.

Supported options:

Option	Description
-c, --run-command	Execute an external command (given as the positional arguments) and render a spinner and timer while the command is running. The exit status of the command is propagated.
--format-table	Read tabular data from standard input (each line is a row and each whitespace separated field is a column), format the data as a table and print the resulting table to standard output. See also the --delimiter option.
-d, --delimiter=VALUE	Change the delimiter used by --format-table to VALUE (a string). By default all whitespace is treated as a delimiter.
-l, --format-length=LENGTH	Convert a length count (given as the integer or float LENGTH) into a human readable string and print that string to standard output.
-n, --format-number=VALUE	Format a number (given as the integer or floating point number VALUE) with thousands separators and two decimal places (if needed) and print the formatted number to standard output.
-s, --format-size=BYTES	Convert a byte count (given as the integer BYTES) into a human readable string and print that string to standard output.
-b, --binary	Change the output of -s, --format-size to use binary multiples of bytes (base-2) instead of the default decimal multiples of bytes (base-10).
-t, --format-timespan=SECONDS	Convert a number of seconds (given as the floating point number SECONDS) into a human readable timespan and print that string to standard output.
--parse-length=VALUE	Parse a human readable length (given as the string VALUE) and print the number of metres to standard output.
--parse-size=VALUE	Parse a human readable data size (given as the string VALUE) and print the number of bytes to standard output.
--demo	Demonstrate changing the style and color of the terminal font using ANSI escape sequences.
-h, --help	Show this message and exit.
A note about size units
When I originally published the humanfriendly package I went with binary multiples of bytes (powers of two). It was pointed out several times that this was a poor choice (see issue #4 and pull requests #8 and #9) and thus the new default became decimal multiples of bytes (powers of ten):

Unit	Binary value	Decimal value
KB	1024	1000
MB	1048576	1000000
GB	1073741824	1000000000
TB	1099511627776	1000000000000
etc	 	 
The option to use binary multiples of bytes remains by passing the keyword argument binary=True to the format_size() and parse_size() functions.

Windows support
Windows 10 gained native support for ANSI escape sequences which means commands like humanfriendly --demo should work out of the box (if your system is up-to-date enough). If this doesn’t work then you can install the colorama package, it will be used automatically once installed.

Contact
The latest version of humanfriendly is available on PyPI and GitHub. The documentation is hosted on Read the Docs and includes a changelog. For bug reports please create an issue on GitHub. If you have questions, suggestions, etc. feel free to send me an e-mail at peter@peterodding.com.

License
This software is licensed under the MIT license.

© 2021 Peter Odding.


Help
Installing packages
Uploading packages
User guide
FAQs
About PyPI
PyPI on Twitter
Infrastructure dashboard
Package index name retention
Our sponsors
Contributing to PyPI
Bugs and feedback
Contribute on GitHub
Translate PyPI
Development credits
Using PyPI
Code of conduct
Report security issue
Privacy policy
Terms of use
Status: All Systems Operational

Developed and maintained by the Python community, for the Python community.
Donate today!

© 2021 Python Software Foundation
Site map

idiomas = "English español français 日本語 português (Brasil) українська Ελληνικά Deutsch 中文 (简体) 中文 (繁體) русский עברית esperanto

projects = [
AWS
AWS
Cloud computing
 Datadog
Datadog
Monitoring
 Facebook / Instagram
Facebook / Instagram
PSF Sponsor
 Fastly
Fastly
CDN
 Google
Google
Object Storage and Download Analytics
 Microsoft
Microsoft
PSF Sponsor
 Pingdom
Pingdom
Monitoring
 Salesforce
Salesforce
PSF Sponsor
 Sentry
Sentry
]


Error logging
 StatusPage
StatusPage
Status page