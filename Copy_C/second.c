#include <stdio.h>

int main(int argc, char *argv[]) {
    if (argc < 3){
        printf("Plz input 2 arguments, src and destination files");
    	return -1;
	}

    FILE*  in_file = fopen(argv[1], "r");
    FILE* out_file = fopen(argv[2], "w");
    int ch;

    if (in_file == NULL){
        printf("Input file is emptry! error!");
        return -1;
    }

    if (out_file == NULL){
        printf("Error with creation of out file! errror");
        return -1;
    }

    while ((ch = fgetc(in_file) )!= EOF) {
        fputc(ch, out_file);
    }

    fclose(in_file);
    fclose(out_file);

    return 0;
}
