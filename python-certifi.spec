%define	module	certifi

Summary:	Mozilla's SSL Certs
Name:		python-%{module}
Version:	2020.06.20
Release:	1
Source0:	https://github.com/certifi/python-certifi/archive/%{version}.tar.gz
License:	ISC
Group:		Development/Python
Url:		https://certifi.io/
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python2)
BuildRequires:	python2-setuptools

%description
This package may or may not become a dependency of Requests. Mozilla's
CA bundle for SSL is MPL / GPL licensed. This will allow for that.

%package -n python2-certifi
Summary:	Mozilla's SSL Certs for Python 2.x
Group:		Development/Python

%description -n python2-certifi
This package may or may not become a dependency of Requests. Mozilla's
CA bundle for SSL is MPL / GPL licensed. This will allow for that.

%prep
%setup -qc
cp -a %{name}-%{version} py2

%install
cd py2
PYTHONDONTWRITEBYTECODE=1 %__python2 setup.py install --root=%{buildroot}

cd ../%{name}-%{version}
PYTHONDONTWRITEBYTECODE=1 %__python setup.py install --root=%{buildroot}

%files
%doc %{name}-%{version}/LICENSE %{name}-%{version}/README.rst
%{py_puresitedir}/certifi*

%files -n python2-certifi
%doc py2/LICENSE py2/README.rst
%{py2_puresitedir}/certifi*
