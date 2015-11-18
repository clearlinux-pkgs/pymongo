#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pymongo
Version  : 3.1.1
Release  : 18
URL      : https://pypi.python.org/packages/source/p/pymongo/pymongo-3.1.1.tar.gz
Source0  : https://pypi.python.org/packages/source/p/pymongo/pymongo-3.1.1.tar.gz
Summary  : Python driver for MongoDB <http://www.mongodb.org>
Group    : Development/Tools
License  : Apache-2.0
Requires: pymongo-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
=======
PyMongo
=======
:Info: See `the mongo site <http://www.mongodb.org>`_ for more information. See `github <http://github.com/mongodb/mongo-python-driver/tree>`_ for the latest source.
:Author: Mike Dirolf
:Maintainer: Bernie Hackett <bernie@mongodb.com>

%package python
Summary: python components for the pymongo package.
Group: Default

%description python
python components for the pymongo package.


%prep
%setup -q -n pymongo-3.1.1

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
