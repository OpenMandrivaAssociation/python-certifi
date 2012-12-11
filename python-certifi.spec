%define	module	certifi
%define name	python-%{module}
%define version 0.0.8
%define release 1

Summary:	Mozilla's SSL Certs
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/c/%{module}/%{module}-%{version}.tar.gz
License:	ISC
Group:		Development/Python
Url:		http://python-requests.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	python-devel

%description
This package may or may not become a dependency of Requests. Mozilla's
CA bundle for SSL is MPL / GPL licensed. This will allow for that.

%prep
%setup -q -n %{module}-%{version}

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE README.rst
%py_sitedir/certifi*


%changelog
* Wed Apr 25 2012 Lev Givon <lev@mandriva.org> 0.0.8-1
+ Revision: 793430
- imported package python-certifi

