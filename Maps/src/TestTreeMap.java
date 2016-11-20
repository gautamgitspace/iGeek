import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.LinkedHashMap;
import java.util.TreeMap;

/**
 * Created by Gautam on 11/20/16.
 */
public class TestTreeMap
{
    private TreeMap<Integer, String> phoneMap;
    public TestTreeMap()
    {
        phoneMap = new TreeMap<>();
    }

    public TreeMap<Integer, String> readFromFile(String fileName)
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
        TestTreeMap testTreeMap = new TestTreeMap();
        TreeMap<Integer, String> result = testTreeMap.readFromFile("/Users/Gautam/Desktop/phones.txt");
        System.out.println("Printing TreeMap keeping keys in sorted order");
        System.out.println(result);
    }
}
