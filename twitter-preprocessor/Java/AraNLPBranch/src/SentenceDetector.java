import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;

import opennlp.tools.sentdetect.SentenceDetectorME;
import opennlp.tools.sentdetect.SentenceModel;

public class SentenceDetector {

	public SentenceDetector(){}

	public String[] detectSentences(String text) throws FileNotFoundException
	     {
		String sentences[] = null;

	    InputStream modelIn = new FileInputStream("arabic-sen.bin");

	    try {
	        SentenceModel model = new SentenceModel(modelIn);
	        SentenceDetectorME sentenceDetector = new SentenceDetectorME(model);
	        sentences = sentenceDetector.sentDetect(text);
	        } 
	    catch (IOException e) 
	        {
	        e.printStackTrace();
	         } 
	     finally 
	     {
	        if (modelIn != null)
	        {
	        	try 
	        	{
	                modelIn.close();
	            } catch (IOException e) {
	            	System.out.println(e.getMessage());
	            }
	        }
	    }
	     
	 return sentences;    
	 }

}
