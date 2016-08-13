import java.util.HashSet;

/**
 * Created by Gautam on 8/13/16.
 */
class Node
{
    Node link;
    int data;
    //DEF CONS
    Node()
    {
        link=null;
        data=0;
    }
    //PARAM CONS
    Node(Node n, int d)
    {
        link = n;
        data = d;
    }
    public void setLink(Node n)
    {
        link = n;
    }
    public void setData(int d)
    {
        data = d;
    }
    public int getData()
    {
        return data;
    }
    public Node getLink()
    {
        return link;
    }
}
class LinkedList
{
    Node start;
    Node end;
    int size;
    //DEF CONS
    LinkedList()
    {
        start = null;
        end = null;
        size = 0;
    }
    int getSize()
    {
        return size;
    }
    boolean isEmpty()
    {
        return start==null;
    }
    public void insertAtStart(int value)
    {
        System.out.println("INSIDE INSERT AT START");
        Node newNode = new Node(null, value);
        size++;
        if(start==null)
        {
            start = newNode;
            end = start;
        }
        else
        {
            newNode.setLink(start);
            start=newNode;
        }
    }
    public void insertAtEnd(int value)
    {
        System.out.println("INSIDE INSERT AT END");
        Node newNode = new Node(null, value);
        size++;
        {
            if(start==null)
            {
                start = newNode;
                end = start;
            }
            else
            {
                end.setLink(newNode);
                end = newNode;
            }
        }
    }

    public void insertAtPosi(int posi, int value)
    {
        System.out.println("INSIDE INSERT AT POSI");
        Node newNode =  new Node(null, value);
        Node iteratingPointer = start;
        posi = posi - 1;
        for(int i=1; i<=size; i++)
        {
            if(i==posi)
            {
                Node temp = iteratingPointer.getLink();
                iteratingPointer.setLink(newNode);
                newNode.setLink(temp);
                break;
            }
            iteratingPointer = iteratingPointer.getLink();
        }
        size++;
    }
    public boolean searchList(int val)
    {
        Node iteratingPointer = start;
        while(iteratingPointer!=null)
        {
            if(iteratingPointer.getData()==val)
            {
                return true;
            }
            iteratingPointer=iteratingPointer.getLink();

        }
        return false;
    }
    public void deleteAtPosi(int posi)
    {
        System.out.println("INSIDE DELETE AT POSI");
        if(posi==1)
        {
            start=start.getLink();
            size--;
            return;
        }
        if(posi==size)
        {
            //2ptrs - iterator and previous tracker
            Node iterator = start;
            Node previous = start;
            while(iterator!=end)
            {
                previous=iterator;
                iterator=iterator.getLink();
            }
            end = previous;
            end.setLink(null);
            size--;
            return;
        }
        posi=posi-1;
        Node iteratingPointer = start;
        for(int i=1; i<size;i++)
        {
            if(i==posi)
            {
                    iteratingPointer.setLink(iteratingPointer.getLink().getLink());
            }
            iteratingPointer=iteratingPointer.getLink();
        }
        size--;
    }


    public void deleteByVal(int val)
    {

        if(val == start.getData())
        {
            System.out.println(start.getData() + " Deleted!");
            start=start.getLink();
            size--;
            return;
        }
        if(val==end.getData())
        {
            //System.out.println("XXX");
            Node iterator = start;
            Node previous = null;
            while(iterator!=end)
            {
                previous=iterator;
                iterator=iterator.getLink();
            }
            System.out.println(end.getData() + " Deleted!");
            end=previous;
            end.setLink(null);
            size--;

            return;
        }
        Node iteratingPointer = start;
        while(iteratingPointer!=null)
        {
            if(iteratingPointer.getLink().getData()==val)
            {
                System.out.println(iteratingPointer.getLink().getData() + " Deleted!");
                iteratingPointer.setLink(iteratingPointer.getLink().getLink());
                break;
            }
            iteratingPointer=iteratingPointer.getLink();
        }
        size--;
    }

    //CTCI 2.1
    public void removeDup()
    {
        //O(n) time but additional space
        Node iteratingPointer = start;
        Node previous = null;
        HashSet hashset = new HashSet();
        while(iteratingPointer!=null)
        {
            if(hashset.contains(iteratingPointer.getData()))
            {
                /*if hashset already contains data then de-link it from the linked list*/
                previous.setLink(iteratingPointer.getLink());
            }
            else
            {
                hashset.add(iteratingPointer.getData());
                previous = iteratingPointer;
            }
            iteratingPointer=iteratingPointer.getLink();
        }
        System.out.println("AFTER REMOVING DUPS: " + hashset);

    }
    //CTCI 2.1_B
    public void removeDupAlternate()
    {
        //O(n^2) time but no additional space
        Node current = start;
        while(current!=null)
        {
            Node runner = current;
            while(runner.getLink()!=null)
            {
                if(runner.getLink().getData()==current.getData())
                {
                    runner.setLink(runner.getLink().getLink());
                }
                else
                {
                    runner=runner.getLink();
                }
            }
            current=current.getLink();
        }
    }
    //CTCI 2.2 ITERATIVE APPROACH USING 2 POINTERS
    public int kthToLast(int k)
    {
        Node ptr1 = start;
        Node ptr2 = start;
        for(int i=0; i<k; i++)
        {
            ptr2=ptr2.getLink();
        }
        if(ptr2==null)
            System.out.println("REACHED END OF LIST");
        while(ptr2!=null)
        {
            ptr1=ptr1.getLink();
            ptr2=ptr2.getLink();
        }
        return ptr1.getData();
    }
    //CTCI 2.4
    public void pivotSort(int pivot)
    {
        Node beforeStart = null;
        Node beforeEnd = null;
        Node afterStart = null;
        Node afterEnd = null;

        Node iteratingPointer = start;
        while(iteratingPointer!=null)
        {
            Node next =  iteratingPointer.getLink();
            iteratingPointer.setLink(null);
            System.out.println("NOW COMPARING: " + iteratingPointer.getData());
            if(iteratingPointer.getData()<pivot)
            {
                //BEFORE CASE
                if(beforeStart==null)
                {
                    //EMPTY LIST CASE
                    beforeStart=iteratingPointer;
                    beforeEnd=beforeStart;
                    System.out.println("ADDED " + iteratingPointer.data + " TO BEFORE");
                }
                else
                {
                    //ADD TO EXISTING CASE
                    beforeEnd.setLink(iteratingPointer);
                    beforeEnd=iteratingPointer;
                    System.out.println("ADDED " + iteratingPointer.data + " TO BEFORE");
                }
            }
            else
            {
                //AFTER CASE
                if(afterStart==null)
                {
                    //EMPTY LIST CASE
                    afterStart=iteratingPointer;
                    afterEnd=afterStart;
                    System.out.println("ADDED " + iteratingPointer.data + " TO AFTER");
                }
                else
                {
                    //ADD TO EXISTING CASE
                    afterEnd.setLink(iteratingPointer);
                    afterEnd=iteratingPointer;
                    System.out.println("ADDED " + iteratingPointer.data + " TO AFTER");
                }
            }
            iteratingPointer=next;
        }
        /*MERGE TWO LISTS AND PRINT*/
        if(beforeStart==null)
        {
            System.out.println("HERE@");
            Node ptr = afterStart;
            while (ptr!=null)
            {
                System.out.print(ptr.getData() + "->");
                ptr=ptr.getLink();
            }
        }
        else
        {
            System.out.println("HERE");
            beforeEnd.setLink(afterStart);
            Node ptr = beforeStart;
            while (ptr!=null)
            {
                System.out.print(ptr.getData() + "->");
                ptr=ptr.getLink();
            }
        }
    }
    //CTCI2_4_b
    public void pivotSortAlternate(int pivot)
    {
        Node head = start;
        Node tail = start;

        Node iteratingPointer = start;
        while(iteratingPointer!=null)
        {
            Node next = iteratingPointer.getLink();
            if(iteratingPointer.data<pivot)
            {
                iteratingPointer.setLink(head);
                head=iteratingPointer;
            }
            else
            {
                tail.setLink(iteratingPointer);
                tail=iteratingPointer;
            }
            iteratingPointer = next;
        }
        tail.setLink(null);

        Node ptr = head;
        while (ptr!=null)
        {
            System.out.print(ptr.getData() + "->");
            ptr=ptr.getLink();
        }
    }

    public void displayList()
    {
        Node ptr = start;
        while (ptr!=null)
        {
            System.out.print(ptr.getData() + "->");
            ptr=ptr.getLink();
        }
    }
}

class LetsHitIT
{
    public static void main(String args[]) {
        LinkedList linkedList = new LinkedList();
        linkedList.insertAtStart(25);
        linkedList.insertAtEnd(10);
        linkedList.insertAtEnd(19);
        linkedList.insertAtEnd(8);
        linkedList.insertAtEnd(13);

        linkedList.displayList();
        System.out.println();
        linkedList.insertAtPosi(3,12);
        linkedList.displayList();
        System.out.println();
        System.out.println("CURRENT SIZE: "+ linkedList.getSize());
        linkedList.pivotSortAlternate(13);
//        System.out.println("3rd Last element is: " + linkedList.kthToLast(3));
//        linkedList.deleteAtPosi(6);
//        linkedList.displayList();
//        System.out.println();
//        System.out.println(linkedList.searchList(25));
//        linkedList.deleteByVal(10);
//        linkedList.displayList();
//        System.out.println();
//        linkedList.deleteByVal(25);
//        linkedList.displayList();
//        System.out.println();
//        linkedList.deleteByVal(2);
//        linkedList.displayList();
//        System.out.println();
//        linkedList.insertAtEnd(5);
//        linkedList.insertAtEnd(5);
//        System.out.println();
//        linkedList.displayList();
//        System.out.println();
//        System.out.println("AFTER REMOVING DUPS");
//        linkedList.removeDupAlternate();
//        linkedList.displayList();

    }

}
