CC=gcc
FILES=p46.c
OUT_EXE=p46
LIBS=-lm
CFLAGS=-Wall

build: $(FILES)
	$(CC) -o $(OUT_EXE) $(CFLAGS) $(FILES) $(LIBS)

clean:
	rm -f *.o $(OUT_EXE)

rebuild: clean build
