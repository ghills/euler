CC=gcc
FILES=p17.c
OUT_EXE=p17
LIBS=
CFLAGS=-Wall

build: $(FILES)
	$(CC) -o $(OUT_EXE) $(CFLAGS) $(FILES) $(LIBS)

clean:
	rm -f *.o $(OUT_EXE)

rebuild: clean build
