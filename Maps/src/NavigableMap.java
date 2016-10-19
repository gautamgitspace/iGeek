import com.sun.source.tree.Tree;

import java.io.BufferedReader;
import java.io.FileReader;
import java.security.PublicKey;
import java.util.*;

/**
 * Created by Gautam on 10/12/16.
 * NAVIGABLE MAP TO RETURN KEYS IS DESCENDING ORDER
 */
public class NavigableMap
{
    public static java.util.NavigableMap<Integer, String> sorted_map_phones = new TreeMap<>();
    public static java.util.NavigableMap<Integer, String> readFromFile(String fileName)
    {

        try {
            BufferedReader br = new BufferedReader(new FileReader(fileName));
            String line;
            while ((line = br.readLine()) != null)
            {
                String tokens[] = line.split(",");
                sorted_map_phones.put(Integer.parseInt(tokens[2].trim()), tokens[3]);
            }
        }
        catch(Exception e)
        {
            e.printStackTrace();
        }
        return  sorted_map_phones.descendingMap();
    }

    public static void main(String args[])
    {
        String fileName = "/Users/Gautam/Desktop/phones.txt";
        java.util.NavigableMap<Integer, String> result = readFromFile(fileName);
        System.out.println(result);
    }

}
