%define	module	certifi

Summary:	Mozilla's SSL Certs


Name:		python-%{module}
Version:	2017.04.17
Release:	1
Source0:	https://github.com/certifi/python-certifi/archive/%{version}.tar.gz
License:	ISC
Group:		Development/Python
Url:		https://certifi.io/
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-setuptools

%description
This package may or may not become a dependency of Requests. Mozilla's
CA bundle for SSL is MPL / GPL licensed. This will allow for that.

%prep
%setup -q

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%files
%doc LICENSE README.rst
%{py_puresitedir}/certifi*
