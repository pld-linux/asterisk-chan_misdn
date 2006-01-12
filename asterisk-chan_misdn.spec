Summary:	Asterisk mISDN channel driver
Summary(pl):	Sterownik kana³u mISDN dla Asteriska
Name:		asterisk-chan_misdn
Version:	0.2.1
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://www.beronet.com/download/chan_misdn/stable/chan_misdn-%{version}.tar.gz
# Source0-md5:	0495c0617c4331d19a399702b2f96366
Source1:	http://isdn.jolly.de/download/v2.7/mISDNuser_for_PBX4Linux-2.7-fix1.tar.gz
# Source1-md5:	146f5f3800545c224abec4108522ea9b
URL:		http://www.beronet.com/index.php?option=com_remository&Itemid=38&func=selectfolder&cat=1&lang=en
BuildRequires:	asterisk-devel
BuildRequires:	mISDN-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mISDN Channel driver (chan_misdn) for the Asterisk Open Source VOIP
Platform.

%description -l pl
Sterownik kana³u mISDN (chan_misdn) dla platformy VOIP o otwartych
¼ród³ach Asterisk.

%prep
%setup -q -n chan_misdn -a1
#-%{version} -a1

sed -i 's/#CFLAGS+=-DASTERISK_STABLE/CFLAGS+=-DASTERISK_STABLE/' Makefile
sed -i 's/-ggdb//g' Makefile

%build
%{__make} -C mISDNuser \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -DInternet_Port=2074 -I`pwd`/include"

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
