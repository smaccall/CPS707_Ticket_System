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
				
				if(hold.substring(0,2).equals("01")){
					
				} else if (hold.substring(0,2).equals("01")) {
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
		}
		
	}

}

class Updater {
	public void addC(String in){
		//uaf
	}
	public void requestC(String in){
		//uaf
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
                    String newLine = atfETitle + atfSName + newTotal + atfpriceTicketStr;
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
                    String newLine = utfSName + utfType + newTotal;
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
                    String newLine = atfETitle + atfSName + newTotal + atfpriceTicketStr;
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
	public void delete(String in){
		//uaf atf
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
