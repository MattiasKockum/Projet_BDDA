.PHONY: all clean

TEX_FILES = main.tex sections/*
REF_FILES = references/*
CONF_FILES = config/*
APDX_FILES = annexes/*
TPLT_FILES = templates/*

all: Rapport.pdf
	@make --no-print-directory clean
	@echo "Création de Rapport.pdf avec succès"

Rapport.pdf: $(TEX_FILES) $(REF_FILES) $(CONF_FILES) $(APDX_FILES) $(TPLT_FILES)
	pdflatex main.tex
	makeglossaries main
	bibtex main
	pdflatex main.tex
	pdflatex main.tex
	mv main.pdf Rapport.pdf

clean:
	rm -rf *.aux *.blg *.bbl *.toc *.log *.nav *.blg *.bbl *.out *.log *.snm *.glo  *.lof *.gls *.glg *.ist
