Summary:	PAM module - authenticate on htpasswd-type files separate from /etc/passwd
Summary(pl):	Modu³ PAM - pozwala na u¿ycie oddzielnych plików z has³ami do ró¿nych us³ug
Name:		pam-pam_pwdfile
Version:	0.98
Release:	2
Epoch:		0
License:	GPL
Group:		Networking
Source0:	http://cpbotha.net/files/pam_pwdfile/pam_pwdfile-%{version}.tar.gz
# Source0-md5:	a60690e288c1c827f6a6040ea38938f1
URL:		http://cpbotha.net/pam_pwdfile.html
BuildRequires:	pam-static > 0.77.3-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PAM module - authenticate on htpasswd-type files separate from
/etc/passwd.

%description -l pl
Modu³ PAM - pozwala na u¿ycie oddzielnych plików z has³ami do ró¿nych
us³ug.

%prep
%setup -q -n pam_pwdfile-%{version}

%build
%{__make} -f contrib/Makefile.standalone \
	CC="%{__cc}" \
	PAMLIB="-lpam -lpamcrypt" \
	CFLAGS="%{rpmcflags} -fPIC -c -Wall -Wformat-security"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/security

install pam_pwdfile.so $RPM_BUILD_ROOT/lib/security

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README changelog
%attr(755,root,root) /lib/security/pam_pwdfile.so
