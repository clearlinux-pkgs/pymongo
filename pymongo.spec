#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pymongo
Version  : 3.10.1
Release  : 47
URL      : https://files.pythonhosted.org/packages/dc/9b/6791f7219f3573bfaa2251da4d814f4fbc49f0bbb258df1e08f7d89a7b85/pymongo-3.10.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/dc/9b/6791f7219f3573bfaa2251da4d814f4fbc49f0bbb258df1e08f7d89a7b85/pymongo-3.10.1.tar.gz
Summary  : Python driver for MongoDB <http://www.mongodb.org>
Group    : Development/Tools
License  : Apache-2.0
Requires: pymongo-license = %{version}-%{release}
Requires: pymongo-python = %{version}-%{release}
Requires: pymongo-python3 = %{version}-%{release}
Requires: dnspython
Requires: ipaddress
Requires: kerberos
BuildRequires : buildreq-distutils3
BuildRequires : dnspython
BuildRequires : ipaddress
BuildRequires : kerberos
Patch1: 0001-Switch-to-kerberos-package-name.patch

%description
=======
PyMongo
=======
:Info: See `the mongo site <http://www.mongodb.org>`_ for more information. See `GitHub <http://github.com/mongodb/mongo-python-driver>`_ for the latest source.
:Author: Mike Dirolf
:Maintainer: Bernie Hackett <bernie@mongodb.com>

About
=====

The PyMongo distribution contains tools for interacting with MongoDB
database from Python.  The ``bson`` package is an implementation of
the `BSON format <http://bsonspec.org>`_ for Python. The ``pymongo``
package is a native Python driver for MongoDB. The ``gridfs`` package
is a `gridfs
<http://www.mongodb.org/display/DOCS/GridFS+Specification>`_
implementation on top of ``pymongo``.

PyMongo supports MongoDB 2.6, 3.0, 3.2, 3.4, 3.6, 4.0 and 4.2.

Support / Feedback
==================

For issues with, questions about, or feedback for PyMongo, please look into
our `support channels <http://www.mongodb.org/about/support>`_. Please
do not email any of the PyMongo developers directly with issues or
questions - you're more likely to get an answer on the `mongodb-user
<http://groups.google.com/group/mongodb-user>`_ list on Google Groups.

Bugs / Feature Requests
=======================

Think you’ve found a bug? Want to see a new feature in PyMongo? Please open a
case in our issue management tool, JIRA:

- `Create an account and login <https://jira.mongodb.org>`_.
- Navigate to `the PYTHON project <https://jira.mongodb.org/browse/PYTHON>`_.
- Click **Create Issue** - Please provide as much information as possible about the issue type and how to reproduce it.

Bug reports in JIRA for all driver projects (i.e. PYTHON, CSHARP, JAVA) and the
Core Server (i.e. SERVER) project are **public**.

How To Ask For Help
-------------------

Please include all of the following information when opening an issue:

- Detailed steps to reproduce the problem, including full traceback, if possible.
- The exact python version used, with patch level::

  $ python -c "import sys; print(sys.version)"

- The exact version of PyMongo used, with patch level::

  $ python -c "import pymongo; print(pymongo.version); print(pymongo.has_c())"

- The operating system and version (e.g. Windows 7, OSX 10.8, ...)
- Web framework or asynchronous network library used, if any, with version (e.g.
  Django 1.7, mod_wsgi 4.3.0, gevent 1.0.1, Tornado 4.0.2, ...)

Security Vulnerabilities
------------------------

If you’ve identified a security vulnerability in a driver or any other
MongoDB project, please report it according to the `instructions here
<http://docs.mongodb.org/manual/tutorial/create-a-vulnerability-report>`_.

Installation
============

PyMongo can be installed with `pip <http://pypi.python.org/pypi/pip>`_::

  $ python -m pip install pymongo

Or ``easy_install`` from
`setuptools <http://pypi.python.org/pypi/setuptools>`_::

  $ python -m easy_install pymongo

You can also download the project source and do::

  $ python setup.py install

Do **not** install the "bson" package from pypi. PyMongo comes with its own
bson package; doing "easy_install bson" installs a third-party package that
is incompatible with PyMongo.

Dependencies
============

PyMongo supports CPython 2.7, 3.4+, PyPy, and PyPy3.5+.

Optional dependencies:

GSSAPI authentication requires `pykerberos
<https://pypi.python.org/pypi/pykerberos>`_ on Unix or `WinKerberos
<https://pypi.python.org/pypi/winkerberos>`_ on Windows. The correct
dependency can be installed automatically along with PyMongo::

  $ python -m pip install pymongo[gssapi]

Support for mongodb+srv:// URIs requires `dnspython
<https://pypi.python.org/pypi/dnspython>`_::

  $ python -m pip install pymongo[srv]

TLS / SSL support may require `ipaddress
<https://pypi.python.org/pypi/ipaddress>`_ and `certifi
<https://pypi.python.org/pypi/certifi>`_ or `wincertstore
<https://pypi.python.org/pypi/wincertstore>`_ depending on the Python
version in use. The necessary dependencies can be installed along with
PyMongo::

  $ python -m pip install pymongo[tls]

Wire protocol compression with snappy requires `python-snappy
<https://pypi.org/project/python-snappy>`_::

  $ python -m pip install pymongo[snappy]

Wire protocol compression with zstandard requires `zstandard
<https://pypi.org/project/zstandard>`_::

  $ python -m pip install pymongo[zstd]

You can install all dependencies automatically with the following
command::

  $ python -m pip install pymongo[snappy,gssapi,srv,tls,zstd]

Other optional packages:

- `backports.pbkdf2 <https://pypi.python.org/pypi/backports.pbkdf2/>`_,
  improves authentication performance with SCRAM-SHA-1 and SCRAM-SHA-256.
  It especially improves performance on Python versions older than 2.7.8.
- `monotonic <https://pypi.python.org/pypi/monotonic>`_ adds support for
  a monotonic clock, which improves reliability in environments
  where clock adjustments are frequent. Not needed in Python 3.


Additional dependencies are:

- (to generate documentation) sphinx_

Examples
========
Here's a basic example (for more see the *examples* section of the docs):

.. code-block:: python

  >>> import pymongo
  >>> client = pymongo.MongoClient("localhost", 27017)
  >>> db = client.test
  >>> db.name
  u'test'
  >>> db.my_collection
  Collection(Database(MongoClient('localhost', 27017), u'test'), u'my_collection')
  >>> db.my_collection.insert_one({"x": 10}).inserted_id
  ObjectId('4aba15ebe23f6b53b0000000')
  >>> db.my_collection.insert_one({"x": 8}).inserted_id
  ObjectId('4aba160ee23f6b543e000000')
  >>> db.my_collection.insert_one({"x": 11}).inserted_id
  ObjectId('4aba160ee23f6b543e000002')
  >>> db.my_collection.find_one()
  {u'x': 10, u'_id': ObjectId('4aba15ebe23f6b53b0000000')}
  >>> for item in db.my_collection.find():
  ...     print(item["x"])
  ...
  10
  8
  11
  >>> db.my_collection.create_index("x")
  u'x_1'
  >>> for item in db.my_collection.find().sort("x", pymongo.ASCENDING):
  ...     print(item["x"])
  ...
  8
  10
  11
  >>> [item["x"] for item in db.my_collection.find().limit(2).skip(1)]
  [8, 11]

Documentation
=============

You will need sphinx_ installed to generate the
documentation. Documentation can be generated by running **python
setup.py doc**. Generated documentation can be found in the
*doc/build/html/* directory.

Testing
=======

The easiest way to run the tests is to run **python setup.py test** in
the root of the distribution.

To verify that PyMongo works with Gevent's monkey-patching::

    $ python green_framework_test.py gevent

Or with Eventlet's::

    $ python green_framework_test.py eventlet

.. _sphinx: http://sphinx.pocoo.org/

%package license
Summary: license components for the pymongo package.
Group: Default

%description license
license components for the pymongo package.


%package python
Summary: python components for the pymongo package.
Group: Default
Requires: pymongo-python3 = %{version}-%{release}

%description python
python components for the pymongo package.


%package python3
Summary: python3 components for the pymongo package.
Group: Default
Requires: python3-core
Provides: pypi(pymongo)

%description python3
python3 components for the pymongo package.


%prep
%setup -q -n pymongo-3.10.1
cd %{_builddir}/pymongo-3.10.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583207797
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pymongo
cp %{_builddir}/pymongo-3.10.1/LICENSE %{buildroot}/usr/share/package-licenses/pymongo/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pymongo/7df059597099bb7dcf25d2a9aedfaf4465f72d8d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
