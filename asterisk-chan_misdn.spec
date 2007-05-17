# TODO: optflags
Summary:	Asterisk mISDN channel driver
Summary(pl.UTF-8):	Sterownik kanału mISDN dla Asteriska
Name:		asterisk-chan_misdn
%define		_rc rc30
Version:	0.3.1
Release:	0.%{_rc}.1
License:	GPL
Group:		Applications
Source0:	http://www.beronet.com/download/chan_misdn/stable/candidates/chan_misdn-%{version}-%{_rc}.tar.gz
# Source0-md5:	871fd786a62857fc8aaae5b5ffc4ae2b
BuildRequires:	asterisk-devel
BuildRequires:	mISDN-devel >= 1.1.1
BuildRequires:	mISDNuser-devel >= 1.1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mISDN Channel driver (chan_misdn) for the Asterisk Open Source VOIP
Platform.

%description -l pl.UTF-8
Sterownik kanału mISDN (chan_misdn) dla platformy VOIP o otwartych
źródłach Asterisk.

%prep
%setup -q -n chan_misdn

sed -i 's/#CFLAGS+=-DASTERISK_STABLE/CFLAGS+=-DASTERISK_STABLE/' Makefile
sed -i 's/-ggdb//g' Makefile

%build
%{__make} \
	CC="%{__cc}" \
	MISDNUSERLIB=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT

install -D chan_misdn.so $RPM_BUILD_ROOT%{_libdir}/asterisk/modules/chan_misdn.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.misdn misdn.conf
%attr(755,root,root) %{_libdir}/asterisk/modules/*
