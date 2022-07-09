%define	module	certifi

Summary:	Mozilla's SSL Certs
Name:		python-%{module}
Version:	2022.6.15
Release:	1
Source0:	https://files.pythonhosted.org/packages/cc/85/319a8a684e8ac6d87a1193090e06b6bbb302717496380e225ee10487c888/certifi-2022.6.15.tar.gz
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
%autosetup -p1 -n certifi-%{version}

%install
PYTHONDONTWRITEBYTECODE=1 %__python setup.py install --root=%{buildroot}

%files
%doc LICENSE README.rst
%{py_puresitedir}/certifi*
