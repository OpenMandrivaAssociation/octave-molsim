%global octpkg molsim

#NOTE *.mex file should be put inti %{_libdir}?

Summary:	A seplib wrapper for GNU Octave
Name:		octave-molsim
Version:	1.0.0
Release:	1
License:	GPLv3+
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/molsim/
Url:		https://github.com/jesperschmidthansen/molsim/
Source0:	https://github.com/jesperschmidthansen/molsim/archive/refs/tags/v%{version}/molsim-%{version}.tar.gz

BuildRequires:  octave-devel >= 6.0.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
molsim is a wrapper for the seplib molecular dynamics library. It 
allows you to perform molecular simulations of simple atomistic 
systems, confined fluids, molecular mixtures, polymers and more.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
#dir %{octpkglibdir}
#{octpkglibdir}/*
#{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

%build
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

