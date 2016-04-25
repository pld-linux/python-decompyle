%define		module	decompyle
#
Summary:	Python 1.5 Decompiler
Name:		python-%{module}
Version:	2.3.2
Release:	1
License:	BSD-like
Group:		Development/Languages/Python
Source0:	http://downloads.sourceforge.net/decompyle/decompyle_%{version}.tar.gz
# Source0-md5:	6d715feebf748fb0da3b8c1f705584b3
Patch0:		%{name}-hack.patch
URL:		http://sourceforge.net/projects/decompyle/
BuildRequires:	python-devel
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Decompyle is a Python 1.5 disassembler and decompiler which converts
Python 1.5 byte-code (.pyc or .pyo) back into equivalent Python
source. Verification of the produced code (re-compiled) is avaliable
as well.

%prep
%setup -q -n %{module}-%{version}.orig
%patch0 -p1

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANNOUNCE CHANGES README TODO
%attr(755,root,root) %{_bindir}/decompyle
%dir %{py_sitedir}/decompyle
%{py_sitedir}/decompyle/*.py*
%{py_sitedir}/decompyle-*.egg-info
%attr(755,root,root) %{py_sitedir}/decompyle/marshal_*.so
