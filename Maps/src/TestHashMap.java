/**
 * Created by Gautam on 11/20/16.
 */

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;
public class TestHashMap
{
    private static HashMap<Integer, String> phoneMap;
    public TestHashMap()
    {
        phoneMap = new HashMap<Integer, String>();

    }

    public HashMap<Integer, String> readFromFile(String fileName)
    {
        try
        {
            BufferedReader bufferedReader = new BufferedReader(new FileReader(fileName));
            String line;
            while((line = bufferedReader.readLine()) != null)
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
        TestHashMap testHashMap = new TestHashMap();
        HashMap<Integer, String> result = testHashMap.readFromFile("/Users/abhigaut/Library/Mobile Documents/com~apple~CloudDocs/GitHub Cloud/iGeek/Maps/python-dicts/phones.txt");
        System.out.println("Printing Out of order Hash Map:");
        System.out.println(result);
    }
}
