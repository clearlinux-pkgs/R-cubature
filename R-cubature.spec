#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-cubature
Version  : 2.0.4.1
Release  : 30
URL      : https://cran.r-project.org/src/contrib/cubature_2.0.4.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/cubature_2.0.4.1.tar.gz
Summary  : Adaptive Multivariate Integration over Hypercubes
Group    : Development/Tools
License  : GPL-3.0 LGPL-3.0
Requires: R-cubature-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-benchr
Requires: R-mvtnorm
BuildRequires : R-Rcpp
BuildRequires : R-benchr
BuildRequires : R-mvtnorm
BuildRequires : buildreq-R
BuildRequires : buildreq-qmake

%description
G. Johnson for adaptive multivariate integration over hypercubes
    and the Cuba C library of Thomas Hahn for deterministic and
    Monte Carlo integration. Scalar and vector interfaces for 
    cubature and Cuba routines are provided; the vector interfaces
    are highly recommended as demonstrated in the package
    vignette.

%package lib
Summary: lib components for the R-cubature package.
Group: Libraries

%description lib
lib components for the R-cubature package.


%prep
%setup -q -c -n cubature
cd %{_builddir}/cubature

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1594051099

%install
export SOURCE_DATE_EPOCH=1594051099
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library cubature
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library cubature
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library cubature
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc cubature || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/cubature/DESCRIPTION
/usr/lib64/R/library/cubature/INDEX
/usr/lib64/R/library/cubature/Meta/Rd.rds
/usr/lib64/R/library/cubature/Meta/features.rds
/usr/lib64/R/library/cubature/Meta/hsearch.rds
/usr/lib64/R/library/cubature/Meta/links.rds
/usr/lib64/R/library/cubature/Meta/nsInfo.rds
/usr/lib64/R/library/cubature/Meta/package.rds
/usr/lib64/R/library/cubature/Meta/vignette.rds
/usr/lib64/R/library/cubature/NAMESPACE
/usr/lib64/R/library/cubature/NEWS.md
/usr/lib64/R/library/cubature/R/cubature
/usr/lib64/R/library/cubature/R/cubature.rdb
/usr/lib64/R/library/cubature/R/cubature.rdx
/usr/lib64/R/library/cubature/doc/cubature.R
/usr/lib64/R/library/cubature/doc/cubature.Rmd
/usr/lib64/R/library/cubature/doc/cubature.html
/usr/lib64/R/library/cubature/doc/index.html
/usr/lib64/R/library/cubature/doc/version2.R
/usr/lib64/R/library/cubature/doc/version2.Rmd
/usr/lib64/R/library/cubature/doc/version2.html
/usr/lib64/R/library/cubature/help/AnIndex
/usr/lib64/R/library/cubature/help/aliases.rds
/usr/lib64/R/library/cubature/help/cubature.rdb
/usr/lib64/R/library/cubature/help/cubature.rdx
/usr/lib64/R/library/cubature/help/paths.rds
/usr/lib64/R/library/cubature/html/00Index.html
/usr/lib64/R/library/cubature/html/R.css
/usr/lib64/R/library/cubature/include/cuba.h
/usr/lib64/R/library/cubature/include/cubature.h
/usr/lib64/R/library/cubature/include/exp_cubature.h
/usr/lib64/R/library/cubature/include/exp_cubature_typedefs.h
/usr/lib64/R/library/cubature/include/rcubature.h
/usr/lib64/R/library/cubature/tests/testthat.R
/usr/lib64/R/library/cubature/tests/testthat/test_cuba.R
/usr/lib64/R/library/cubature/tests/testthat/test_cubature.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/cubature/libs/cubature.so
/usr/lib64/R/library/cubature/libs/cubature.so.avx2
/usr/lib64/R/library/cubature/libs/cubature.so.avx512
