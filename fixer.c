#include <stdio.h>
#include <string.h>
#include <stdbool.h> 
//Owen Kasprick
//Combines totla occurance count data over all years in Google Ngram dataset 2012 file

int main(int argc, char *argv[]) {

   FILE *fp;
   //int count = 0;
   char buff[10000];
   
   FILE *fpout;
   char outbuff[10000];
	
   
   char word[10000];
   int year;
   int ncount;
   int nbooks;
   
   bool fword = true;
   
   char curword[10000];
   memset(curword, '\0', sizeof(curword));
   int curncount = 0;
   
   char line[10000];
   
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
	//count++;
	//printf("%d\n", count);
	sscanf(buff, "%s%d%d%d", word, &year, &ncount, &nbooks);
	//printf("%s\n", word);
	if (fword) {
		fword = false;
		strcpy(curword, word);
		curncount = ncount;
	} else {
		if (strcmp(word, curword) == 0) {
			curncount += ncount;
		} else {
			if (fprintf(fpout, "%s %d\n", curword, curncount) < 0) {
				perror("could not write to file!");
			}
			strcpy(curword, word);
			curncount = ncount;
		}
	}
	
   }
   if (fprintf(fpout, "%s %d\n", curword, curncount) < 0) {
		perror("could not write to file!");
	}
 

   fclose(fp);
   fclose(fpout);

}