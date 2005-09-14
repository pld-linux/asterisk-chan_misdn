Summary:	Asterisk mISDN channel driver
Name:		asterisk-chan_misdn
Version:	0.1.1
Release:	0.1
License:	GPL
Group:		Applications
Source0:	chan_misdn-%{version}.tar.gz
# Source0-md5:	77a68e82e8f06d610644033f72bfa217
Source1:	http://isdn.jolly.de/download/v2.7/mISDNuser_for_PBX4Linux-2.7-fix1.tar.gz
# Source0-md5:  146f5f3800545c224abec4108522ea9b
URL:		http://www.beronet.com/index.php?option=com_remository&Itemid=38&func=selectfolder&cat=1&lang=en
BuildRequires:	asterisk-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mISDN Channel driver (chan_misdn) for the Asterisk Open Source VOIP
Platform.

%prep
%setup -q -n chan_misdn-%{version} -a1

sed -i 's/#CFLAGS+=-DASTERISK_STABLE/CFLAGS+=-DASTERISK_STABLE/' Makefile
sed -i 's/-ggdb//g' Makefile

%build

cd mISDNuser
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -DInternet_Port=2074 -I`pwd`/include"
cd -

%{__make} \
	CC="%{__cc}" \
	MISDNUSER="mISDNuser"

%install
rm -rf $RPM_BUILD_ROOT

install -D chan_misdn.so $RPM_BUILD_ROOT%{_prefix}/lib/asterisk/modules/chan_misdn.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.misdn CHANGES mISDN.sample misdn.conf
%attr(755,root,root) %{_prefix}/lib/asterisk/modules/chan_misdn.so
