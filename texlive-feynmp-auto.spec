Name:		texlive-feynmp-auto
Version:	30223
Release:	2
Summary:	Automatic processing of feynmp graphics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/feynmp-auto
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/feynmp-auto.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/feynmp-auto.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/feynmp-auto.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package takes care of running Metapost on the output files
produced by the feynmp package, so that the compiled pictures
will be available in the next run of LaTeX. The package honours
options that apply to feynmp.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/feynmp-auto/feynmp-auto.sty
%doc %{_texmfdistdir}/doc/latex/feynmp-auto/README
%doc %{_texmfdistdir}/doc/latex/feynmp-auto/feynmp-auto.pdf
#- source
%doc %{_texmfdistdir}/source/latex/feynmp-auto/feynmp-auto.dtx
%doc %{_texmfdistdir}/source/latex/feynmp-auto/feynmp-auto.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
