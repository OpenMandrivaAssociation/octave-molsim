%global octpkg molsim

Summary:	A seplib wrapper for GNU Octave
Name:		octave-%{octpkg}
Version:	0.9.1
Release:	1
Url:		https://github.com/jesperschmidthansen/%{octpkg}/
Source0:	%{url}/archive/v%{version}/%{octpkg}-%{version}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics

BuildRequires:	octave-devel >= 3.8.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
A GNU Octave molecular dynamics package.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

# remove backup files
#find . -name \*~ -delete

%build
#export CFLAGS="%{optflags} -std=c99"
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

