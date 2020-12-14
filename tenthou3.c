#include <stdio.h>
#include <string.h>
#include <stdbool.h> 
#include <unistd.h>
#include <stdbool.h> 
//Owen Kasprick
//Pull 10000 top words not in us dictionary


int main(int argc, char *argv[]) {

   FILE *fpin, *fpout, *fpin2;
   //int count = 0;
   char buff[10000];
   static char outbuff[10000][10000];
   memset(outbuff, '\0', sizeof(outbuff));
   int counts[10000] = {0};
   char word[10000];
   int ncount = 0;
   
   static char usbuff[10000][10000];

   char filename[100];
   char outfilename[110];
   strcpy(filename, argv[1]);
   snprintf(outfilename, sizeof(outfilename), "10000%s-us", filename);
   
   fpin = fopen(filename, "r");
   fpin2 = fopen("10000aFIXeng-us", "r");
   fpout = fopen(outfilename, "w+");
   
   int i = 0;
   
   while (fgets(buff, sizeof(buff), fpin2) != NULL) {
	   sscanf(buff, "%s%d", word, &ncount);
	   strcpy(usbuff[i], word);
	   i++;
   }
   
   int j = 0;
   int prog = 0;
   int tempcount1;
   char tempword1[10000];
   int tempcount2;
   char tempword2[10000];
   
   while (fgets(buff, sizeof(buff), fpin) != NULL) {
	   if((prog%10000)==0) {
		   printf("%d\n", prog);
	   }
	   i = 0;
	   sscanf(buff, "%s%d", word, &ncount);
	   j = 0;
	   while (j < 10000) {
		   if (strcmp(word, usbuff[j]) == 0) {
			   break;
		   }
		   j++;
	   }
	   //printf("%d\n", j);
	   if (j != 10000) {
		   prog++;
		   continue;
	   }
	   while(i<10000) {
			if(strcmp(word, outbuff[i]) ==0){
				//if (counts[i] == -1) {
				//	counts[i] = ncount;
				//	break;
				//}
				//printf("%s=%s, %d ,%d\n", word, outbuff[i], i, ncount );
				ncount += counts[i];
				j = i;
				while (j < 9999) {
					counts[j] = counts[j+1];
					strcpy(outbuff[j], outbuff[j+1]);
					j++;
				}
				//counts[i] = -1;
				i = 0;
				continue;
				
			}
			if(ncount >= counts[i]) {
				j = i;
				tempcount1 = counts[j];
				strcpy(tempword1, outbuff[j]);
				//isrepeat = false;
				//printf("Shifting Array:\n[");
				while(j < 9999) {
					//if (isrepeat) {
					//	break;
					//}
					//if (counts[j+1] == -1) {
					//	isrepeat = true;
					//}
					tempcount2 = counts[j+1];
					counts[j+1] = tempcount1;
					tempcount1 = tempcount2;
					
					strcpy(tempword2, outbuff[j+1]);
					strcpy(outbuff[j+1], tempword1);
					strcpy(tempword1, tempword2);
					j++;
					//printf("%s %d,", outbuff[j], counts[j]);
				}
				//printf("\b]\n");
				counts[i] = ncount;
				strcpy(outbuff[i], word);
				
				break;
			}
		i++;
	   }
	   prog++;
	   //i = 0;
	   //printf("Array: \n [");
	   //while(i<100) {
		//   printf("(%s, %d),", outbuff[i], counts[i]);
		//   i++;
	   //}
	   //printf("\b]\n\n");
	   //if (prog > 100000) break;
   }
   
   i = 0;
   while(i < 10000) {
	   fprintf(fpout, "%s %d\n", outbuff[i], counts[i]);
	   i++;
   }
   
   fclose(fpin);
   fclose(fpout);

}