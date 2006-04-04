#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Pod
%define		pnam	Parser
Summary:	Pod::Parser - base class for creating POD filters and translators
Summary(pl):	Pod::Parser - klasa bazowa do tworzenia klas filtruj�cych i t�umacz�cych POD
Name:		perl-Pod-Parser
Version:	1.34
Release:	1
# I'm not sure how to interpret the README...
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4f3a9ebb17bc092bffbcf11dc5d1a5ff
#Patch0:		%{name}-broken.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
  This parrot is dead. It has ceased to be.
  It's gone to meet it's Maker! THIS IS AN EX-PARROT!
    -- The Dead Parrot Sketch, Monty Python's Flying Circus

Do s/parrot/package/g and you know the status of this distribution.

Pod::Parser is a base class for creating POD filters and translators.
It handles most of the effort involved with parsing the POD sections
from an input stream, leaving subclasses free to be concerned only
with performing the actual translation of text.

Pod::Parser parses PODs, and makes method calls to handle the various
components of the POD. Subclasses of Pod::Parser override these
methods to translate the POD into whatever output format they desire.

%description -l pl
  Ta papuga jest martwa. Przesta�a istnie�.
  Odesz�a na spotkanie ze swoim stw�rc�! TO JEST EX-PAPUGA!
    -- skecz "Martwa Papuga", Lataj�cy Cyrk Monty Pythona

Wykonaj s/papuga/pakiet/g, a poznasz status tego modu�u.

Pod::Parser to klasa bazowa do tworzenia klas filtruj�cych i
t�umacz�cych POD. Obs�uguje wi�ksz� cz�� zada� zwi�zanych z analiz�
sekcji POD ze strumienia wej�ciowego, pozostawiaj�c podklasom jedynie
przeprowadzanie samego t�umaczenia tekstu.

Pod::Parser przetwarza pliki POD i wywo�uje metody obs�uguj�ce r�ne
komponenty POD. Podklasy Pod::Parser przykrywaj� te metody w celu
t�umaczenia POD na ��dany format wyj�ciowy.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
#%patch0 -p1 -b .orig

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# resolve conflict with perl-tools
%{__mv} $RPM_BUILD_ROOT%{_bindir}/pod2usage{,.cpan}
%{__mv} $RPM_BUILD_ROOT%{_bindir}/podchecker{,.cpan}
%{__mv} $RPM_BUILD_ROOT%{_bindir}/podselect{,.cpan}
%{__mv} $RPM_BUILD_ROOT%{_mandir}/man1/pod2usage{,.cpan}.1p
%{__mv} $RPM_BUILD_ROOT%{_mandir}/man1/podchecker{,.cpan}.1p
%{__mv} $RPM_BUILD_ROOT%{_mandir}/man1/podselect{,.cpan}.1p

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO
%{perl_vendorlib}/Pod/*.pm
%{_mandir}/man?/*
%{_bindir}/*
