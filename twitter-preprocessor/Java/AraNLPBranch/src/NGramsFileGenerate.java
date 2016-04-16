import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.Writer;

public class NGramsFileGenerate {
	
	
	public static void main(String[] args){
		
		String[] filetypes = {"out_tweets"};
				
		for(String type:filetypes){
			
			File file = new File("D:\\Curriculum\\Natural-Language-Processing\\Directed-Research\\AllData\\Filtered\\"+type+"filtered.txt");
			 if (file.exists()){
			     file.delete();
			 }  
		
			File filein = new File("D:\\Curriculum\\Natural-Language-Processing\\Directed-Research\\AllData\\Extracted\\"+type+".txt");
			
			AraNormalizer arn=new AraNormalizer();
			DiacriticsRemover dr=new DiacriticsRemover();
			PunctuationsRemover pr=new PunctuationsRemover();
			
			
			try (BufferedReader br = new BufferedReader(
					
					new InputStreamReader(
                    new FileInputStream(filein), "UTF8")
					
					)) {
			    String line;
			    Writer out = new BufferedWriter(new OutputStreamWriter(
	    			    new FileOutputStream("D:\\Curriculum\\Natural-Language-Processing\\Directed-Research\\AllData\\Filtered\\"+type+"filtered.txt"), "UTF8"));;
			    
			    while ((line = br.readLine()) != null){
			    	line = line.replaceAll("[\\x00-\\x1F]", "").replaceAll("[\\x21-\\x7F]", "");
			    	
			    	if(line.replaceAll(" ","").length()>1){
			    		
			    		String normalizedText=arn.normalize(line);
						
						normalizedText = dr.removeDiacritics(normalizedText);
						normalizedText = pr.removePunctuations(normalizedText);
						normalizedText = normalizedText.replaceAll("[\\x00-\\x1F]", "").replaceAll("[\\x21-\\x7F]", "");
				    	
				    	try{
				    		 	try {
				    			    out.write(normalizedText+"\n");
				    			} catch(Exception e){
				    				System.err.println(e);
				    			}
				    		
				    	}catch(Exception e){
				    		System.err.println(e);
				    	}
			    	}else{
			    		try {
		    			    out.write("nopropertweet"+"\n");
		    			} catch(Exception e){
		    				System.err.println(e);
		    			}
			    	}
			    }
			    out.close();
			}catch(Exception e){
				e.printStackTrace();
			}
		}
		
		
	}
}
