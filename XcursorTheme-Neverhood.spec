Summary:	A cursor theme based on cursors from The Neverhood game
Summary(pl.UTF-8):	Motyw kursorów oparty na kursorach z gry The Neverhood
Name:		XcursorTheme-Neverhood
Version:	1.0
Release:	2
License:	GPL
Group:		Themes
Source0:	http://www.kde-look.org/content/files/11359-neverhoodDesktop.tar.gz
# Source0-md5:	f72fbc11c38b3a4858f7c784062ea1ad
URL:		http://www.kde-look.org/content/show.php?content=11359
BuildRequires:	XFree86 >= 4.3
Requires:	XFree86 >= 4.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A plasticine looking cursor theme with a really wobbly feel.

%description -l pl.UTF-8
Motyw kursorów o nietypowym plastelinowym wyglądzie. Sprawia wrażenie
jakoby kursory się chwiały.

%prep
%setup -q -n neverhoodDesktop

%build
cd neverhoodCursor/src
%{__make} \
	COLOR=Pink

%install
rm -rf $RPM_BUILD_ROOT
cd neverhoodCursor/src
%{__make} install \
	COLOR=Pink \
	INSTALLDIR=$RPM_BUILD_ROOT%{_iconsdir}/neverhoodPink/cursors

Z="`/bin/pwd`"
colors="Pink"
for i in $colors;
do
cd $RPM_BUILD_ROOT%{_iconsdir}/neverhood$i/cursors
ln -s hand link
ln -s fleur move
ln -s v_double_arrow sb_v_double_arrow
ln -s h_double_arrow sb_h_double_arrow
done
cd "$Z"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_iconsdir}/neverhood*
