# Makefile for CV generation and compilation
# ==========================================================

PY   := python
TEX  := xelatex
TARGS := cv.tex

.PHONY: all tex clean tex-fast regenerate help

# Default: generate tex + compile PDF
all: generate tex

# Step 1: generate cv.tex from profile.yml
generate:
	$(PY) generate_cv.py

# Step 2: compile PDF (run twice to resolve refs)
tex: generate
	$(TEX) -interaction=nonstopmode $(TARGS)
	$(TEX) -interaction=nonstopmode $(TARGS)

# Compile without regenerating tex (assumes cv.tex is up to date)
tex-fast:
	$(TEX) -interaction=nonstopmode $(TARGS)
	$(TEX) -interaction=nonstopmode $(TARGS)

# Clean build artifacts
clean:
	rm -f cv.aux cv.log cv.out cv.toc cv.snm cv.nav cv.fls cv.fdb_latexmk cv.run.xml
	rm -f cv.pdf

distclean: clean
	rm -f cv.tex

regenerate: distclean all

help:
	@echo "CV Makefile targets:"
	@echo "  make all        - generate cv.tex from profile.yml, then compile PDF (default)"
	@echo "  make generate   - generate cv.tex only"
	@echo "  make tex        - compile PDF (regenerates tex first)"
	@echo "  make tex-fast   - compile PDF without regenerating tex"
	@echo "  make clean      - remove build artifacts (.aux, .log, .pdf, ...)"
	@echo "  make distclean  - remove clean + cv.tex"
	@echo "  make regenerate - full rebuild (distclean + all)"
	@echo "  make help       - show this message"
