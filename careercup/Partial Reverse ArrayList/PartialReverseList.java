import java.util.ArrayList;

/**
 * Given an arraylist, reverse the first n elements and print the entire arraylist.  
 * Created by Gautam on 10/18/16.
 */
public class PartialReverseList
{
    private ArrayList<Integer> list;

    public PartialReverseList()
    {
        list = new ArrayList<>();
    }

    public static ArrayList<Integer> reverse(ArrayList<Integer> toBeReversed, int revPivot)
    {
        ArrayList<Integer> result = new ArrayList<>();
        for(int i=revPivot-1; i>=0; i--)
        {
            result.add(toBeReversed.get(i));
        }
        for(int i=revPivot; i<toBeReversed.size(); i++)
        {
            result.add(toBeReversed.get(i));
        }
        return result;
    }

    public static void main(String args[])
    {
        ArrayList<Integer> toTest = new ArrayList<>();
        for(int i=1;i<9;i++)
        {
            toTest.add(i);
        }
        System.out.println("BEFORE: ");
        System.out.println(toTest);
        System.out.println("AFTER: ");
        System.out.println(reverse(toTest, 7));
    }

}
