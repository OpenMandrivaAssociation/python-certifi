%define	module	certifi

Summary:	Mozilla's SSL Certs
Name:		python-%{module}
Version:	2026.1.4
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/c/certifi/certifi-%{version}.tar.gz#/%{name}-%{version}.tar.gz
License:	ISC
Group:		Development/Python
URL:		https://certifi.io/
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(setuptools)

%description
This package may or may not become a dependency of Requests. Mozilla's
CA bundle for SSL is MPL / GPL licensed. This will allow for that.

%files
%doc LICENSE README.rst
%{py_puresitedir}/certifi*
