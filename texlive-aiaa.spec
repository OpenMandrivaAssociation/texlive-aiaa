# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/aiaa
# catalog-date 2006-09-12 13:40:13 +0200
# catalog-license lppl
# catalog-version 3.6
Name:		texlive-aiaa
Version:	3.6
Release:	11
Summary:	Typeset AIAA conference papers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/aiaa
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aiaa.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aiaa.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aiaa.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A bundle of LaTeX/BibTeX files and sample documents to aid
those producing papers and journal articles according to the
guidelines of the American Institute of Aeronautics and
Astronautics (AIAA).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/aiaa/aiaa.bst
%{_texmfdistdir}/tex/latex/aiaa/aiaa-tc.cls
%doc %{_texmfdistdir}/doc/latex/aiaa/README
%doc %{_texmfdistdir}/doc/latex/aiaa/aiaa.pdf
%doc %{_texmfdistdir}/doc/latex/aiaa/author_guide.pdf
%doc %{_texmfdistdir}/doc/latex/aiaa/author_guide.tex
%doc %{_texmfdistdir}/doc/latex/aiaa/bibtex_database.bib
%doc %{_texmfdistdir}/doc/latex/aiaa/figure_magnet.eps
%doc %{_texmfdistdir}/doc/latex/aiaa/figure_magnet.pdf
%doc %{_texmfdistdir}/doc/latex/aiaa/pre2004/CHANGES
%doc %{_texmfdistdir}/doc/latex/aiaa/pre2004/MANIFEST
%doc %{_texmfdistdir}/doc/latex/aiaa/pre2004/README
%doc %{_texmfdistdir}/doc/latex/aiaa/pre2004/aiaa.dtx
%doc %{_texmfdistdir}/doc/latex/aiaa/pre2004/aiaa.ins
%doc %{_texmfdistdir}/doc/latex/aiaa/pre2004/aiaa.pdf
%doc %{_texmfdistdir}/doc/latex/aiaa/pre2004/aiaalgo.eps
%doc %{_texmfdistdir}/doc/latex/aiaa/pre2004/demos/paper/smpaiaa.ps
%doc %{_texmfdistdir}/doc/latex/aiaa/pre2004/demos/paper/smpaiaa.tex
%doc %{_texmfdistdir}/doc/latex/aiaa/pre2004/demos/paper/smpbtx.bib
%doc %{_texmfdistdir}/doc/latex/aiaa/pre2004/demos/paper/smpfig.eps
%doc %{_texmfdistdir}/doc/latex/aiaa/pre2004/demos/refs/tstbtx.bib
%doc %{_texmfdistdir}/doc/latex/aiaa/pre2004/demos/refs/tstref.tex
%doc %{_texmfdistdir}/doc/latex/aiaa/pre2004/demos/subfigs/smpfig.eps
%doc %{_texmfdistdir}/doc/latex/aiaa/pre2004/demos/subfigs/smpsubf.tex
%doc %{_texmfdistdir}/doc/latex/aiaa/pre2004/demos/talk/smpfig.eps
%doc %{_texmfdistdir}/doc/latex/aiaa/pre2004/demos/talk/smptalk.ps
%doc %{_texmfdistdir}/doc/latex/aiaa/pre2004/demos/talk/smptalk.sty
%doc %{_texmfdistdir}/doc/latex/aiaa/pre2004/demos/talk/smptalk.tex
%doc %{_texmfdistdir}/doc/latex/aiaa/template_advanced.pdf
%doc %{_texmfdistdir}/doc/latex/aiaa/template_advanced.tex
%doc %{_texmfdistdir}/doc/latex/aiaa/template_basic.pdf
%doc %{_texmfdistdir}/doc/latex/aiaa/template_basic.tex
#- source
%doc %{_texmfdistdir}/source/latex/aiaa/aiaa.dtx
%doc %{_texmfdistdir}/source/latex/aiaa/aiaa.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.6-2
+ Revision: 749152
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 3.6-1
+ Revision: 717805
- texlive-aiaa
- texlive-aiaa
- texlive-aiaa
- texlive-aiaa
- texlive-aiaa

