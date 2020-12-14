#include <stdio.h>
#include <string.h>
#include <stdbool.h> 
#include <ctype.h>
//Owen Kasprick
//Removes tags and chifts to lowercase all words

int main(int argc, char *argv[]) {

   FILE *fp;
   //int count = 0;
   char buff[10000];
   
   FILE *fpout;
   char outbuff[10000];
	
   
   char word[10000];
   char word2[10000] = {0};
   char *wordptr = &word[0] ;

   int ncount;

   int i = 0;
   int len = 0;
   
   char line[10000];
   char *fixedword;
   
   char filename[100];
   char outfilename[110];
   strcpy(filename, argv[1]);
   snprintf(outfilename, sizeof(outfilename), "aFIX%s", filename);
   fp = fopen(filename, "r");
   fpout = fopen(outfilename, "w+");
   if (fp == NULL) {
	   perror("Can't open file");
   }

    while (fgets(buff, 10000, fp) != NULL) {
	sscanf(buff, "%s%d", word, &ncount);
 
		
			fixedword = strtok(word, "_");
			//printf("%s\n",fixedword);
			i = 0;
			len = strlen(fixedword);
			while(i<len) {
				fixedword[i] = tolower(fixedword[i]);
				i++;
			}
			if (fprintf(fpout, "%s %d\n", fixedword, ncount) < 0) {
				perror("could not write to file!");
			}
	}

   fclose(fp);
   fclose(fpout);

}