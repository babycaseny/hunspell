# Makefile for source rpm: hunspell
# $Id$
NAME := hunspell
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
