import java.io.IOException;
import java.io.*;

import java.util.*;

public class ArabicPreProcessor {
	
	static Set<String> stopWords;
	
	static{
		
		stopWords = new HashSet<>();
		
		File file = new File("D:\\Curriculum\\Natural-Language-Processing\\AraNLP\\AraNLP\\src\\main\\arabic.txt");
		try (BufferedReader br = new BufferedReader(new FileReader(file))) {
		    String line;
		    while ((line = br.readLine()) != null) {
		    	stopWords.add(line.replace("\n", "").replace("\r", ""));
		    }
		}catch(Exception e){
			e.printStackTrace();
		}
		
	}

	public static String readStream(InputStream is) {
	    StringBuilder sb = new StringBuilder(512);
	    try {
	        Reader r = new InputStreamReader(is, "UTF-8");
	        int c = 0;
	        while ((c = r.read()) != -1) {
	            sb.append((char) c);
	        }
	    } catch (IOException e) {
	        throw new RuntimeException(e);
	    }
	    return sb.toString();
	}
	
	
	public static void main(String[] args) throws IOException, ClassNotFoundException {
		// Example of using the modules within a simple pipeline
		
		//String[] filetypes = {"INTJ","INFJ","ISTJ","ISFJ","INTP","INFP","ISTP","ISFP","ENTJ","ENFJ","ESTJ","ESFJ","ENTP","ENFP","ESTP","ESFP"};
		String[] filetypes = {"INFJ"};
		
		for(String type:filetypes){
			File filein = new File("D:\\Curriculum\\Natural-Language-Processing\\Directed-Research\\AllData\\Extracted\\"+type+".txt");
			
			FileInputStream fsin = new FileInputStream(filein);
					
			PrintWriter output = new PrintWriter("D:\\Curriculum\\Natural-Language-Processing\\Directed-Research\\AllData\\Tokenized\\" + type + "AraTokens.txt");
			
			String arabicText = readStream(fsin);
			
			TrainedTokenizer tok=new TrainedTokenizer();
			AraNormalizer arn=new AraNormalizer();
			DiacriticsRemover dr=new DiacriticsRemover();
			PunctuationsRemover pr=new PunctuationsRemover();
			
			
			String normalizedText=arn.normalize(arabicText);
			normalizedText = dr.removeDiacritics(normalizedText);
			normalizedText = pr.removePunctuations(normalizedText);
			normalizedText = normalizedText.replaceAll("[\\x00-\\x1F]", "").replaceAll("[\\x21-\\x7F]", "");
			
			File fileout = new File("D:\\Curriculum\\Natural-Language-Processing\\Directed-Research\\AllData\\Filtered\\"+type+"filtered.txt");
			
			byte[] bytes = normalizedText.getBytes();
			
			try{
				FileOutputStream out = new FileOutputStream(fileout);
				out.write(bytes);
			}catch(Exception e){
				System.err.println(e);
			}

			
			String[] tokens=tok.tokenize(normalizedText);
				
			String newText="";
			for (int i=0;i<tokens.length;i++)
			{
				if(!stopWords.contains(tokens[i]))
					output.println(tokens[i]);
				
			}
		
			output.close();
			System.out.println("Text after stemming: "+newText);

		}
		
	}

}
