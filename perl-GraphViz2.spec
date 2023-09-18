#
# Conditional build:
%bcond_without	tests		# unit tests
#
%define		pdir	GraphViz2
Summary:	GraphViz2 Perl module - interface to the GraphViz graphing tool
Summary(pl.UTF-8):	Moduł Perla GraphViz - interfejs do narzędzia grafowego GraphViz
Name:		perl-GraphViz2
Version:	2.67
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/GraphViz2/%{pdir}-%{version}.tar.gz
# Source0-md5:	3573cf425d6630e25e6fbea678ac7f77
URL:		https://metacpan.org/dist/GraphViz2
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl(Data::Section::Simple) >= 0.02
BuildRequires:	perl(Test::Snapshot) >= 0.06
BuildRequires:	perl-File-Which >= 1.21
BuildRequires:	perl-Graph >= 0.9716
BuildRequires:	perl-IPC-Run3 >= 0.048
BuildRequires:	perl-Moo >= 2.001001
BuildRequires:	perl-Type-Tiny >= 1.000005
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This modules provides an interface to layout and generate images of
directed graphs in a variety of formats (PostScript, PNG, etc.) using
the "dot" and "neato" programs from the GraphViz project.

%description -l pl.UTF-8
Ten moduł udostępnia interfejs do planowania i generowania obrazów
skierowanych grafów w różnych formatach (PostScript, PNG itd.) przy
użyciu programów "dot" i "neato" z projektu GraphViz.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/GraphViz2.pm
%{perl_vendorlib}/GraphViz2
%{_mandir}/man3/GraphViz2*.3*
