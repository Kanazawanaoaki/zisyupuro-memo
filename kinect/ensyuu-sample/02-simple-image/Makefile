include ../build/common/CommonDefs.mak

BIN_DIR = ../bin

INC_DIRS = /usr/local/include/ni /usr/include/ni

SRC_FILES = ./*.cpp

EXE_NAME = 02-simple-image

ifeq ("$(OSTYPE)","Darwin")
	LDFLAGS += -framework OpenGL -framework GLUT
else
	USED_LIBS += glut GL
endif

USED_LIBS += OpenNI

include ../build/common/CommonCppMakefile
