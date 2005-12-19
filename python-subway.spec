%define		module	subway
%define		snap	20051219

Summary:	A pythonic, object-oriented web development stack
Summary(pl):	Pythonowy, zorientowany obiektowo stos do tworzenia WWW
Name:		python-%{module}
Version:	0.2
%define	_rc	rc1
Release:	0.%{_rc}.1
License:	BSD
Group:		Development/Languages/Python
Source0:	%{module}-%{snap}.tar.bz2
# Source0-md5:	4d439e2825479dda68eff179f07da223
URL:		http://subway.python-hosting.com/
BuildRequires:	python
%pyrequires_eq	python-modules
Requires:	python-cheetah
Requires:	python-cherrypy
Requires:	python-FormEncode
Requires:	python-SQLObject
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Subway project aims to create a Web development stack combining the
ideas and spirit of Ruby on Rails with a comprehensive suite of
prewritten Python web libraries and tools.

%description -l pl
Celem projektu Subway jest stworzenie stosu do tworzenia WWW ³±cz±cego
idee i duch Ruby on Rails z obszernym zestawem gotowych bibliotek i
narzêdzi pythonowych do WWW.

%prep
%setup -q -n %{module}-%{snap}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitescriptdir},%{_bindir}}

python ./setup.py install \
	--single-version-externally-managed \
        --optimize 2 \
        --root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/*egg*
