import java.io.*;
import java.util.Scanner;
import java.lang.*;
import java.lang.annotation.ElementType;
public class Main {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		try {
			Scanner scanner = new Scanner(new File("dtf.txt"));
			while (scanner.hasNextLine()){
				String hold = scanner.nextLine();
				Updater up = new Updater();
				
				if (hold.substring(0,2).equals("01")) {
					up.create(hold);
				} else if (hold.substring(0,2).equals("02")) {
					up.delete(hold);
				} else if (hold.substring(0,2).equals("03")) {
					up.sell(hold);
				} else if (hold.substring(0,2).equals("04")) {
					up.buy(hold);
				} else if (hold.substring(0,2).equals("05")) {
					up.refund(hold);
				} else if (hold.substring(0,2).equals("06")) {
					up.addC(hold);
				} else if (hold.substring(0,2).equals("07")) {
					up.requestC(hold);
				} else if (hold.substring(0,2).equals("00")) {
					System.out.println("WAAAA2");
				} else {
					System.out.println("WAAAA");
				}
					
					
			}
			
		} catch (FileNotFoundException ex) {
			System.out.print("File not found");
		} catch (IOException e) {
            e.printStackTrace();
        }

    }

}

class Updater {
    //06 clause
	public void addC(String input) throws  IOException {
		//uaf
        String nameB = input.substring(3,19).strip();
        String roleB = input.substring(19,22).strip();
        String amountB = input.substring(22,31).strip();
        Scanner s = new Scanner((new File("uaf.txt")));
        FileWriter fw = new FileWriter("uaf.txt");
        while (s.hasNextLine()){
            String output = s.nextLine();
            if (output.substring(0,16).equals(nameB)){
                Float total = Float.parseFloat(output.substring(20,29)) + Float.parseFloat(amountB);
                fw.write(String.format("%-15d", nameB) + " " + roleB + " " + String.format("%09d", Float.toString(total)));
            } else {
                fw.write(output);
            }
        }
        fw.close();
        s.close();

	}
	public void requestC(String in){
		//nothing :)

	}
	public void buy(String in){
        //atf
        try 
        {
            Scanner s = new Scanner(new File("atf.txt"));
            String eTitle = in.substring(3,22).trim();
            String sName = in.substring(23,37).trim();
            String numTicketsStr = in.substring(38,41).trim();
            int numTickets = Integer.parseInt(numTicketsStr);
            //String priceTicketStr = in.substring(42,48).trim();
            //int priceTicket = Integer.parseInt(priceTicketStr);  
            String newLine = "";
            while (s.hasNextLine())
            {
                String temp = s.nextLine();
                String atfETitle = temp.substring(0,19).trim();
                String atfSName = temp.substring(20,34).trim();
                if (atfETitle.equals(eTitle) && atfSName.equals(sName))
                {
                    String atfnumTicketsStr = temp.substring(35,38).trim();
                    int atfnumTickets = Integer.parseInt(atfnumTicketsStr);
                    String atfpriceTicketStr = temp.substring(39,45).trim();
                    int newTotal = atfnumTickets - numTickets;
                    newLine = atfETitle + atfSName + newTotal + atfpriceTicketStr;
                    break;
                    //int atfpriceTicket = Integer.parseInt(atfpriceTicketStr);
                    
                }
            }
            Updater.modifyFile("atf.txt", in, newLine);
            s.close();
        }
        catch (FileNotFoundException ex)
        {
            System.out.print("ERROR: <File not found>");
        }

        //utf
        try 
        {
            Scanner s = new Scanner(new File("utf.txt"));
            String eTitle = in.substring(3,22).trim();
            String sName = in.substring(23,37).trim();
            String numTicketsStr = in.substring(38,41).trim();
            int numTickets = Integer.parseInt(numTicketsStr);
            String priceTicketStr = in.substring(42,48).trim();
            int priceTicket = Integer.parseInt(priceTicketStr); 
            int totalCredit = numTickets * priceTicket; 
            String newLine = "";
            while (s.hasNextLine())
            {
                String temp = s.nextLine();
                String utfSName = temp.substring(0,15).trim();
                if (utfSName.equals(sName))
                {
                    String utfType = temp.substring(16,18).trim();
                    String utfCreditsStr = temp.substring(20,28).trim();
                    int utfCredits = Integer.parseInt(utfCreditsStr);
                    int newTotal = utfCredits + totalCredit;
                    newLine = utfSName + utfType + newTotal;
                    break;
                    //int atfpriceTicket = Integer.parseInt(atfpriceTicketStr);
                    
                }
            }
            Updater.modifyFile("utf.txt", in, newLine);
            s.close();
        }
        catch (FileNotFoundException ex)
        {
            System.out.print("ERROR: <File not found>");
        }
	}
	public void sell(String in){
        //atf
        try 
        {
            Scanner s = new Scanner(new File("atf.txt"));
            String eTitle = in.substring(3,22).trim();
            String sName = in.substring(23,37).trim();
            String numTicketsStr = in.substring(38,41).trim();
            int numTickets = Integer.parseInt(numTicketsStr);
            String newLine = "";
            //String priceTicketStr = in.substring(42,48).trim();
            //int priceTicket = Integer.parseInt(priceTicketStr);  
            while (s.hasNextLine())
            {
                String temp = s.nextLine();
                String atfETitle = temp.substring(0,19).trim();
                String atfSName = temp.substring(20,34).trim();
                if (atfETitle.equals(eTitle) && atfSName.equals(sName))
                {
                    String atfnumTicketsStr = temp.substring(35,38).trim();
                    int atfnumTickets = Integer.parseInt(atfnumTicketsStr);
                    String atfpriceTicketStr = temp.substring(39,45).trim();
                    int newTotal = atfnumTickets + numTickets;
                    newLine = atfETitle + atfSName + newTotal + atfpriceTicketStr;
                    break;
                    //int atfpriceTicket = Integer.parseInt(atfpriceTicketStr);
                    
                }
            }
            Updater.modifyFile("atf.txt", in, newLine);
            s.close();
        }
        catch (FileNotFoundException ex)
        {
            System.out.print("ERROR: <File not found>");
        }
	}
	public void create(String in){
		//uaf

	}
	public void delete(String input) throws IOException{
		//uaf atf
        //uaf
        String nameB = input.substring(3,19).strip();
        Scanner s = new Scanner((new File("uaf.txt")));
        FileWriter fw = new FileWriter("uaf.txt");
        Scanner s2 = new Scanner((new File("atf.txt")));
        FileWriter fw2 = new FileWriter("atf.txt");
        while (s.hasNextLine()){
            String output = s.nextLine();
            if (output.substring(0,16).equals(nameB)){
               //do nothing
            } else {
                fw.write(output);
            }
        }
        while (s2.hasNextLine()) {
            String output2 = s2.nextLine();
            if (!output2.substring(21,34).equals(nameB))
                fw2.write(output2);
        }
        fw.close();
        s.close();

        //atf


	}
	public void refund(String in){
		//uaf
		
    }
    static void modifyFile(String filePath, String oldString, String newString)
    {
        File fileToBeModified = new File(filePath); 
        String oldContent = "";
        BufferedReader reader = null;
        FileWriter writer = null;
         
        try
        {
            reader = new BufferedReader(new FileReader(fileToBeModified));
             
            //Reading all the lines of input text file into oldContent
            String line = reader.readLine();
            while (line != null) 
            {
                oldContent = oldContent + line + System.lineSeparator();
                line = reader.readLine();
            }
             
            //Replacing oldString with newString in the oldContent
             
            String newContent = oldContent.replaceAll(oldString, newString);
             
            //Rewriting the input text file with newContent
             
            writer = new FileWriter(fileToBeModified);
             
            writer.write(newContent);
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }
        finally
        {
            try
            {
                //Closing the resources
                 
                reader.close();
                 
                writer.close();
            } 
            catch (IOException e) 
            {
                e.printStackTrace();
            }
        }
    }
}
