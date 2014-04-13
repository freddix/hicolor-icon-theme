Summary:	Directory hierarchy for default icon theme
Name:		hicolor-icon-theme
Version:	0.13
Release:	1
License:	LGPL
Group:		Base
Source0:	http://icon-theme.freedesktop.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	21d0f50aa6b8eef02846cda9e5e9324c
URL:		http://icon-theme.freedesktop.org/wiki/HicolorTheme
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Directory hierarchy for default icon theme.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_iconsdir}/hicolor/{24x24/apps,26x26/apps,16x16/stock/emoticons}
install index.theme $RPM_BUILD_ROOT%{_iconsdir}/hicolor
for dir in `grep Directories= index.theme|sed -e 's/Directories=//;s/,/ /g'` ; do
	install -d $RPM_BUILD_ROOT%{_iconsdir}/hicolor/$dir
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{_iconsdir}/hicolor
