#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Pod
%define		pnam	Parser
Summary:	Pod::Parser - base class for creating POD filters and translators
Summary(pl.UTF-8):	Pod::Parser - klasa bazowa do tworzenia klas filtrujących i tłumaczących POD
Name:		perl-Pod-Parser
# perl-modules 5.30 provides 1.63
Version:	1.61
Release:	1
Epoch:		1
# I'm not sure how to interpret the README...
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Pod/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	77e912caf2a1c5b29d577dff80390ce8
URL:		https://metacpan.org/release/Pod-Parser
BuildRequires:	perl(File::Spec) >= 0.82
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Test-Simple >= 0.60
%endif
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

%description -l pl.UTF-8
  Ta papuga jest martwa. Przestała istnieć.
  Odeszła na spotkanie ze swoim stwórcą! TO JEST EX-PAPUGA!
    -- skecz "Martwa Papuga", Latający Cyrk Monty Pythona

Wykonaj s/papuga/pakiet/g, a poznasz status tego modułu.

Pod::Parser to klasa bazowa do tworzenia klas filtrujących i
tłumaczących POD. Obsługuje większą część zadań związanych z analizą
sekcji POD ze strumienia wejściowego, pozostawiając podklasom jedynie
przeprowadzanie samego tłumaczenia tekstu.

Pod::Parser przetwarza pliki POD i wywołuje metody obsługujące różne
komponenty POD. Podklasy Pod::Parser przykrywają te metody w celu
tłumaczenia POD na żądany format wyjściowy.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%{__mv} $RPM_BUILD_ROOT%{_bindir}/podselect{,.cpan}
%{__mv} $RPM_BUILD_ROOT%{_mandir}/man1/podselect{,.cpan}.1p

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO
%attr(755,root,root) %{_bindir}/podselect.cpan
%{perl_vendorlib}/Pod/Find.pm
%{perl_vendorlib}/Pod/InputObjects.pm
%{perl_vendorlib}/Pod/ParseUtils.pm
%{perl_vendorlib}/Pod/Parser.pm
%{perl_vendorlib}/Pod/PlainText.pm
%{perl_vendorlib}/Pod/Select.pm
%{_mandir}/man1/podselect.cpan.1p*
%{_mandir}/man3/Pod::Find.3pm*
%{_mandir}/man3/Pod::InputObjects.3pm*
%{_mandir}/man3/Pod::ParseUtils.3pm*
%{_mandir}/man3/Pod::Parser.3pm*
%{_mandir}/man3/Pod::PlainText.3pm*
%{_mandir}/man3/Pod::Select.3pm*
