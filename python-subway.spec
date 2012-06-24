%define		module	subway
%define		snap	20050913

Summary:	A pythonic, object-oriented web development stack
#Summary(pl):	
Name:		python-%{module}
Version:	0
Release:	0.%{snap}.1
License:	BSD
Group:		Development/Languages/Python
Source0:	%{module}-%{snap}.tar.bz2
# Source0-md5:	82655b144bcf72047d3aeeb9357380f7
URL:		http://subway.python-hosting.com/
BuildRequires:	python
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Subway project aims to create  a Web development stack combining the
ideas  and  spirit of  Ruby  on  Rails  with  a comprehensive  suite  of
prewritten Python web libraries and tools.

#description -l pl

#%package examples
#Summary:	Example files for CherryPy
#Summary(pl):	Pliki przyk�ad�w dla CherryPy
#Group:		Development/Languages/Python
#Requires:	%{name} = %{version}-%{release}

#%description examples
#Example files for CherryPy.

#%description examples -l pl
#Pliki przyk�ad�w dla CherryPy.

%prep
%setup -q -n %{module}-%{snap}

%build
%py_comp subway/
%py_ocomp subway/

%install
rm -rf $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install -d $RPM_BUILD_ROOT{%{py_sitescriptdir},%{_bindir}}

cp -r subway $RPM_BUILD_ROOT%{py_sitescriptdir}
install subway_create.py $RPM_BUILD_ROOT%{_bindir}

#cp -r cherrypy/tutorial $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#doc 
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/%{module}

#%files examples
#%defattr(644,root,root,755)
#%{_examplesdir}/%{name}-%{version}
