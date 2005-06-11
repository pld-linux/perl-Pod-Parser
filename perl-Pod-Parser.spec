#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Pod
%define		pnam	Parser
Summary:	Pod::Parser - base class for creating POD filters and translators
Summary(pl):	Pod::Parser - klasa bazowa do tworzenia klas filtruj±cych i t³umacz±cych POD
Name:		perl-Pod-Parser
Version:	1.31
Release:	2
# I'm not sure how to interpret the README...
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9239f922617f805bc9da2f71d717061c
Patch0:		perl-Pod-Parser-broken.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pod::Parser is a base class for creating POD filters and translators.
It handles most of the effort involved with parsing the POD sections
from an input stream, leaving subclasses free to be concerned only
with performing the actual translation of text.

Pod::Parser parses PODs, and makes method calls to handle the various
components of the POD. Subclasses of Pod::Parser override these
methods to translate the POD into whatever output format they desire.

%description -l pl
Pod::Parser to klasa bazowa do tworzenia klas filtruj±cych i
t³umacz±cych POD. Obs³uguje wiêksz± czê¶æ zadañ zwi±zanych z analiz±
sekcji POD ze strumienia wej¶ciowego, pozostawiaj±c podklasom jedynie
przeprowadzanie samego t³umaczenia tekstu.

Pod::Parser przetwarza pliki POD i wywo³uje metody obs³uguj±ce ró¿ne
komponenty POD. Podklasy Pod::Parser przykrywaj± te metody w celu
t³umaczenia POD na ¿±dany format wyj¶ciowy.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO
%{perl_vendorlib}/Pod/*.pm
%{_mandir}/man?/*
%{_bindir}/*
