%define	module	certifi

Summary:	Mozilla's SSL Certs


Name:		python-%{module}
Version:	14.05.14
Release:	5
Source0:	http://pypi.python.org/packages/source/c/certifi/certifi-%{version}.tar.gz
License:	ISC
Group:		Development/Python
Url:		http://python-requests.org/
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-setuptools

%description
This package may or may not become a dependency of Requests. Mozilla's
CA bundle for SSL is MPL / GPL licensed. This will allow for that.

%prep
%setup -q -n %{module}-%{version}

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean

%files
%doc LICENSE README.rst
%{py_puresitedir}/certifi*
