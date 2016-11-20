import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InterruptedIOException;
import java.util.LinkedHashMap;

/**
 * Created by Gautam on 11/20/16.
 */
public class TestLinkedHashMap
{
    private LinkedHashMap<Integer, String> phoneMap;
    public TestLinkedHashMap()
    {
        phoneMap = new LinkedHashMap<Integer, String>();
    }

    public LinkedHashMap<Integer, String> readFromFile(String fileName)
    {
        try
        {
            BufferedReader bufferedReader = new BufferedReader(new FileReader(fileName));
            String line;
            while((line = bufferedReader.readLine())!=null)
            {
                String tokens[] = line.split(",");
                phoneMap.put(Integer.parseInt(tokens[2].trim()), tokens[3]);
            }
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }
        return phoneMap;
    }
    public static void main(String args[])
    {
        TestLinkedHashMap testLinkedHashMap = new TestLinkedHashMap();
        LinkedHashMap<Integer, String> result = testLinkedHashMap.readFromFile("/Users/Gautam/Desktop/phones.txt");
        System.out.println("Printing LinkedHashMap preserving the order of insertion");
        System.out.println(result);
    }
}
