%define module certifi

Summary:	Mozilla's SSL Certs
Name:		python-certifi
Version:	2026.2.25
Release:	1
License:	MPL-2.0
Group:		Development/Python
URL:		https://certifi.io/
Source0:	https://files.pythonhosted.org/packages/source/c/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
This package may or may not become a dependency of Requests. Mozilla's
CA bundle for SSL is MPL / GPL licensed. This will allow for that.

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info

%files
%doc README.rst
%license LICENSE
%{py_puresitedir}/%{module}
%{py_puresitedir}/%{module}-%{version}.dist-info

