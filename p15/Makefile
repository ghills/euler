CC=gcc
FILES=p15.c
OUT_EXE=p15
LIBS=-lgmp
CFLAGS=-Wall

build: $(FILES)
	$(CC) -o $(OUT_EXE) $(CFLAGS) $(FILES) $(LIBS)

clean:
	rm -f *.o $(OUT_EXE)

rebuild: clean build
