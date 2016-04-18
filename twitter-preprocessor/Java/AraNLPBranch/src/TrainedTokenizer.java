import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;

import opennlp.tools.tokenize.TokenizerME;
import opennlp.tools.tokenize.TokenizerModel;

public class TrainedTokenizer {
public TrainedTokenizer(){}
	

    public String[] tokenize(String line) throws FileNotFoundException, IOException {

        String tokens[] = null;

        InputStream modelIn = new FileInputStream("arabic-token.bin");

        try {
            TokenizerModel model = new TokenizerModel(modelIn);
            TokenizerME tokenizer = new TokenizerME(model);
            tokens = tokenizer.tokenize(line);
            } 
        catch (IOException e) 
           {
            e.printStackTrace();
           } 
        finally 
        {
            if (modelIn != null) {
                try {
                    modelIn.close();
                    } 
                catch (IOException e) {
                   System.out.println(e.getMessage());
                }
            }
        }

        return tokens;
       }
}
