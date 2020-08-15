# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = rwi
SOURCEDIR     = .
BUILDDIR      = _build
APIDOCCMD     = sphinx-apidoc
APIDOCARGS    = --ext-autodoc --ext-intersphinx --ext-coverage --ext-todo --ext-viewcode -d 5 -e -f
APIDOCPROJ    = $(SPHINXPROJ)
APIDOCOUT     = api-reference/$(APIDOCPROJ)
APIDOC_FILES  = $(APIDOCOUT)/$(APIDOCPROJ)*.rst
PKGDIR        = ../$(APIDOCPROJ)

ifneq (,$(wildcard $(APIDOC_FILES)))
    RMCMD = rm -rv $(APIDOC_FILES)
else
    RMCMD = true
endif

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(RMCMD)
	@$(APIDOCCMD) $(APIDOCARGS) -o $(APIDOCOUT) $(PKGDIR)
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
