%define 	modulename pam_pwdfile
Summary:	PAM module - authenticate on htpasswd-type files separate from /etc/passwd
Summary(pl):	Modu³ PAM pozwalaj±cy na u¿ycie oddzielnych plików z has³ami do ró¿nych us³ug
Name:		pam-%{modulename}
Version:	0.99
Release:	2
Epoch:		0
License:	GPL
Group:		Base/Authentication and Authorization
Source0:	http://cpbotha.net/files/pam_pwdfile/%{modulename}-%{version}.tar.gz
# Source0-md5:	a05b41f0bd1c0de16bec8aad6b1b30a9
URL:		http://cpbotha.net/pam_pwdfile.html
BuildRequires:	pam-static > 0.77.3-2
Obsoletes:	pam_pwdfile
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PAM module - authenticate on htpasswd-type files separate from
/etc/passwd.

%description -l pl
Modu³ PAM pozwalaj±cy na u¿ycie oddzielnych plików z has³ami do
ró¿nych us³ug.

%prep
%setup -q -n %{modulename}-%{version}

%build
%{__make} -f contrib/Makefile.standalone \
	CC="%{__cc}" \
	PAMLIB="-lpam -lpamcrypt" \
	CFLAGS="%{rpmcflags} -fPIC -c -Wall -Wformat-security"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_lib}/security

install pam_pwdfile.so $RPM_BUILD_ROOT/%{_lib}/security

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README changelog contrib/warwick_duncan-cyrus_without_system_accounts.txt
%attr(755,root,root) /%{_lib}/security/pam_pwdfile.so
