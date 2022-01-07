#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-jaraco.functools
Version  : 3.5.0
Release  : 36
URL      : https://files.pythonhosted.org/packages/1e/c8/6733dc1c6afca663c08534e7f4e7b14751019f6dd3476c40dbecb3904449/jaraco.functools-3.5.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/1e/c8/6733dc1c6afca663c08534e7f4e7b14751019f6dd3476c40dbecb3904449/jaraco.functools-3.5.0.tar.gz
Summary  : Functools like those found in stdlib
Group    : Development/Tools
License  : MIT
Requires: pypi-jaraco.functools-license = %{version}-%{release}
Requires: pypi-jaraco.functools-python = %{version}-%{release}
Requires: pypi-jaraco.functools-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
Provides: jaraco.functools
Provides: jaraco.functools-python
Provides: jaraco.functools-python3
BuildRequires : pypi(pluggy)
BuildRequires : py-python
BuildRequires : pypi(more_itertools)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pytest
BuildRequires : setuptools_scm
BuildRequires : tox
BuildRequires : pypi(virtualenv)

%description
.. image:: https://img.shields.io/pypi/v/jaraco.functools.svg
:target: `PyPI link`_

%package license
Summary: license components for the pypi-jaraco.functools package.
Group: Default

%description license
license components for the pypi-jaraco.functools package.


%package python
Summary: python components for the pypi-jaraco.functools package.
Group: Default
Requires: pypi-jaraco.functools-python3 = %{version}-%{release}

%description python
python components for the pypi-jaraco.functools package.


%package python3
Summary: python3 components for the pypi-jaraco.functools package.
Group: Default
Requires: python3-core
Provides: pypi(jaraco.functools)
Requires: pypi(more_itertools)

%description python3
python3 components for the pypi-jaraco.functools package.


%prep
%setup -q -n jaraco.functools-3.5.0
cd %{_builddir}/jaraco.functools-3.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641447495
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-jaraco.functools
cp %{_builddir}/jaraco.functools-3.5.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-jaraco.functools/8e6689d37f82d5617b7f7f7232c94024d41066d1
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-jaraco.functools/8e6689d37f82d5617b7f7f7232c94024d41066d1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
