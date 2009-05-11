
%define		tcl_version		%(rpm -q --qf %{V} tcl-devel | cut -d. -f1,2)
%define		tcl_sitelib		%{_datadir}/tcl%{tcl_version}

%define		package	bwidget
Summary:	Extended widget set for Tk
Name:		tcl-%{package}
Version:	1.8.0
Release:	0.3
License:	TCL
Group:		Development/Libraries
URL:		http://tcllib.sourceforge.net/
Source0:	http://dl.sourceforge.net/tcllib/BWidget-%{version}.tar.bz2
# Source0-md5:	5d2433c5fd93ab7f906f4c7ab225b0d8
BuildRequires:	tcl >= 8.4
Requires:	tcl >= %{tcl_version}
Requires:	tk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An extended widget set for Tcl/Tk.

%prep
%setup -q -n BWidget-%{version}
%{__sed} -i 's/\r//' LICENSE.txt

%install
rm -rf $RPM_BUILD_ROOT
# Don't bother with the included configure script and Makefile.  They
# are missing a lot of pieces and won't work at all.  Installation is
# pretty simple, so we can just do it here manually.
install -d $RPM_BUILD_ROOT%{tcl_sitelib}/%{package}%{version}
mkdir $RPM_BUILD_ROOT%{tcl_sitelib}/%{package}%{version}/lang
mkdir $RPM_BUILD_ROOT%{tcl_sitelib}/%{package}%{version}/images

cp -a *.tcl $RPM_BUILD_ROOT%{tcl_sitelib}/%{package}%{version}
cp -a lang/*.rc $RPM_BUILD_ROOT%{tcl_sitelib}/%{package}%{version}/lang
cp -a images/*.gif images/*.xbm $RPM_BUILD_ROOT%{tcl_sitelib}/%{package}%{version}/images

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt LICENSE.txt
%doc BWman/*.html
%dir %{tcl_sitelib}/%{package}%{version}
%{tcl_sitelib}/%{package}%{version}/*.tcl
%{tcl_sitelib}/%{package}%{version}/images
%dir %{tcl_sitelib}/%{package}%{version}/lang
%{tcl_sitelib}/%{package}%{version}/lang/en.rc
%lang(da) %{tcl_sitelib}/%{package}%{version}/lang/da.rc
%lang(de) %{tcl_sitelib}/%{package}%{version}/lang/de.rc
%lang(es) %{tcl_sitelib}/%{package}%{version}/lang/es.rc
%lang(fr) %{tcl_sitelib}/%{package}%{version}/lang/fr.rc
