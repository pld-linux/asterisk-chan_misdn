Summary:        Asterisk mISDN channel driver
Summary(pl):    Sterownik kana<B3>u mISDN dla Asteriska
Name:           asterisk-chan_misdn
Version:        0.3.1
Release:        0.rc27.1
License:        GPL
Group:          Applications
Source0:        http://www.beronet.com/download/chan_misdn/stable/chan_misdn.tar.gz
# Source0-md5:	0e2cbccfc6c6c995aeb782d2e40f1003
BuildRequires:  asterisk-devel
BuildRequires:  mISDN-devel
BuildRequires:  mISDNuser-devel
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mISDN Channel driver (chan_misdn) for the Asterisk Open Source VOIP
Platform.

%description -l pl
Sterownik kana�u mISDN (chan_misdn) dla platformy VOIP o otwartych
�r�d�ach Asterisk.

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
