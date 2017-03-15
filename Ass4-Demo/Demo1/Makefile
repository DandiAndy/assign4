CC=gcc
OBJ=readdata.o getattrib.o maketree.o printtree.o functions.o gain.o ID3.o
FLAGS=-g

ID3:			$(OBJ)
			$(CC) $(FLAGS) $(OBJ) -o $@ -lm

readdata.o:		readdata.c
			$(CC) $(FLAGS) -c readdata.c

getattrib.o:		getattrib.c
			$(CC) $(FLAGS) -c getattrib.c

maketree.o:		maketree.c
			$(CC) $(FLAGS) -c maketree.c

printtree.o:		printtree.c
			$(CC) $(FLAGS) -c printtree.c

functions.o:		functions.c
			$(CC) $(FLAGS) -c functions.c

gain.o:			gain.c
			$(CC) $(FLAGS) -c gain.c

ID3.o:			ID3.c
			$(CC) $(FLAGS) -c ID3.c

