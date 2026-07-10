%global tl_name feynmp-auto
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Automatic processing of feynmp graphics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/feynmp-auto
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/feynmp-auto.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/feynmp-auto.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/feynmp-auto.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package takes care of running Metapost on the output files produced
by the feynmp package, so that the compiled pictures will be available
in the next run of LaTeX. The package honours options that apply to
feynmp.

