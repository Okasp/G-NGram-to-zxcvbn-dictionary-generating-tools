import java.util.*;
import java.io.*;

public class formatstrip{
	public static void main(String[] args) throws IOException {
		 FileInputStream in = null;
		 FileOutputStream out = null;
		 FileInputStream in2 = null;
		 FileOutputStream out2 = null;
		 FileInputStream in3 = null;
		 FileOutputStream out3 = null;
		 try{
			 in = new FileInputStream("stripped_uk.txt");
			 out = new FileOutputStream("formatstripped_uk-us.txt");

			 BufferedReader r1 = new BufferedReader(new InputStreamReader(in));
			 BufferedWriter w1 = new BufferedWriter(new OutputStreamWriter(out));

			 char c;
			 while((r1.ready())){
				 String line = r1.readLine();
				 w1.write(line+",");
			 }
			 w1.close();
			 r1.close();
		 }finally{
			 if(in != null){
				 in.close();
			 }
			 if(out != null){
				 out.close();
			 }
		 }
		 try{
			 in2 = new FileInputStream("stripped_us.txt");
			 out2 = new FileOutputStream("formatstripped_us.txt");

			 BufferedReader r2 = new BufferedReader(new InputStreamReader(in2));
			 BufferedWriter w2 = new BufferedWriter(new OutputStreamWriter(out2));

			 while((r2.ready())){
				 String line = r2.readLine();
				 w2.write(line+",");
			 }
			 w2.close();
			 r2.close();
		 }finally{
			 if(in2 != null){
				 in2.close();
			 }
			 if(out2 != null){
				 out2.close();
			 }
		 }


		try{
			in3 = new FileInputStream("stripped_uk.txt");
			out3 = new FileOutputStream("formatstripped_uk.txt");

			BufferedReader r3 = new BufferedReader(new InputStreamReader(in3));
			BufferedWriter w3 = new BufferedWriter(new OutputStreamWriter(out3));

			char c;
			while((r3.ready())){
				String line = r3.readLine();
				String[] separate = line.split(" "); // separate pass and #
				w3.write(line+",");
			}
			w3.close();
			r3.close();
		}finally{
			if(in3 != null){
				in3.close();
			}
			if(out3 != null){
				out3.close();
			}
		}
	}
}
