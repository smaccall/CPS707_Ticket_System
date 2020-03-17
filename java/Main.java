
import java.io.*;
import java.util.Scanner;
public class Main {

	/**
	 * @param args
	 * @throws IOException 
	 */
	public static void main(String[] args) throws IOException {
		// Reads through daily transaction file to apply changes to uaf and atf
		merger();
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

	/**
	 * @param args
	 * @throws IOException 
	 * merge multiple daily transaction files into one
	 */
	public static void merger() throws IOException {
		File dir = new File("\\output");
		PrintWriter pw = new PrintWriter("dtf.txt"); 
		String[] fileNames = dir.list();
		
		for (String fileName : fileNames) {
			if (fileName.contains("dtf")) {
				File f = new File(dir, fileName); 
				  
	            // create object of BufferedReader 
	            BufferedReader br = new BufferedReader(new FileReader(f)); 
	            pw.println("Contents of file " + fileName); 
	  
	            // Read from current file 
	            String line = br.readLine(); 
	            while (line != null) { 
	                // write to the output file 
	                pw.println(line); 
	                line = br.readLine(); 
	            } 
	            pw.flush(); 
	            br.close();
			}
		}
		pw.close();
	}
	
}

/**
 * Class that has methods to update each file according to the correct action
 */
class Updater {
	/**
	 * @param input
	 */
	public void addC(String input) throws  IOException {
		// update the uaf file with the new ammount of credit for that user
        String nameB = input.substring(3,19).strip();
        String roleB = input.substring(19,22).strip();
        String amountB = input.substring(22).strip();
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
	/**
	 * @param input
	 */
	public void buy(String in){
		// update the atf file with the new amount of available tickets
		// update the uaf with buyers new credit amount
        try 
        {
            Scanner s = new Scanner(new File("atf.txt"));
            String eTitle = in.substring(3,22).strip();
            String sName = in.substring(23,37).strip();
            String numTicketsStr = in.substring(38,41).strip();
            int numTickets = Integer.parseInt(numTicketsStr);
            //String priceTicketStr = in.substring(42,48).strip();
            //int priceTicket = Integer.parseInt(priceTicketStr);  
            String newLine = "";
            while (s.hasNextLine())
            {
                String temp = s.nextLine();
                String atfETitle = temp.substring(0,19).strip();
                String atfSName = temp.substring(20,34).strip();
                if (atfETitle.equals(eTitle) && atfSName.equals(sName))
                {
                    String atfnumTicketsStr = temp.substring(35,38).strip();
                    int atfnumTickets = Integer.parseInt(atfnumTicketsStr);
                    String atfpriceTicketStr = temp.substring(39,45).strip();
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
            String eTitle = in.substring(3,22).strip();
            String sName = in.substring(23,37).strip();
            String numTicketsStr = in.substring(38,41).strip();
            int numTickets = Integer.parseInt(numTicketsStr);
            String priceTicketStr = in.substring(42,48).strip();
            int priceTicket = Integer.parseInt(priceTicketStr); 
            int totalCredit = numTickets * priceTicket; 
            String newLine = "";
            while (s.hasNextLine())
            {
                String temp = s.nextLine();
                String utfSName = temp.substring(0,15).strip();
                if (utfSName.equals(sName))
                {
                    String utfType = temp.substring(16,18).strip();
                    String utfCreditsStr = temp.substring(20,28).strip();
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
	
	/**
	 * @param input
	 */
	public void sell(String in){
        // update the atf file with the new ticket available for sale
        try 
        {
            Scanner s = new Scanner(new File("atf.txt"));
            String eTitle = in.substring(3,22).strip();
            String sName = in.substring(23,37).strip();
            String numTicketsStr = in.substring(38,41).strip();
            int numTickets = Integer.parseInt(numTicketsStr);
            String newLine = "";
            //String priceTicketStr = in.substring(42,48).strip();
            //int priceTicket = Integer.parseInt(priceTicketStr);  
            while (s.hasNextLine())
            {
                String temp = s.nextLine();
                String atfETitle = temp.substring(0,19).strip();
                String atfSName = temp.substring(20,34).strip();
                if (atfETitle.equals(eTitle) && atfSName.equals(sName))
                {
                    String atfnumTicketsStr = temp.substring(35,38).strip();
                    int atfnumTickets = Integer.parseInt(atfnumTicketsStr);
                    String atfpriceTicketStr = temp.substring(39,45).strip();
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
	
	/**
	 * @param input
	 */
	public void create(String input) throws IOException{
		// update uaf file with the newly created user
		 String nameB = input.substring(3,19).strip();
		 String role = input.substring(19,22).strip();
		 String credit = input.substring(22).strip();
		 Scanner s = new Scanner((new File("uaf.txt")));
		 FileWriter fw = new FileWriter("uaf.txt");
		 while (s.hasNext()) {
			 //get to bottom of file.
		 }
		 fw.write(String.format("%-15d", nameB) + " " + role + " " + String.format("%09d", credit));		
	}

	/**
	 * @param input
	 */
	public void delete(String input) throws IOException{
		// delete account from uaf and any related tickets deleted from atf
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

	/**
	 * @param input
	 */
	public void refund(String in) throws IOException{
		// update buyer and sellers credit amount in uaf
		String buyer = in.substring(3,19).strip();
		String seller = in.substring(19,35).strip();
		String credit = in.substring(35).strip();
		
		Scanner s = new Scanner((new File("uaf.txt")));
		FileWriter fw = new FileWriter("uaf.txt");
		
		while (s.hasNextLine()) {
			String line = s.nextLine();
			String name = line.substring(0,16).strip();
			if (name.equalsIgnoreCase(buyer)) {
				String role = line.substring(16,19).strip();
				float total = Float.parseFloat(line.substring(20,29)) + Float.parseFloat(credit);
            	fw.write(String.format("%-15d", buyer) + " " + role + " " + String.format("%09d", Float.toString(total)));
			} else if (name.equalsIgnoreCase(seller)) {
				String role = line.substring(16,19).strip();
				float total = Float.parseFloat(line.substring(20,29)) - Float.parseFloat(credit);
            	fw.write(String.format("%-15d", seller) + " " + role + " " + String.format("%09d", Float.toString(total)));
			}
			
		}
		
    }
	
	/**
	 * @param filePath, oldString, newString
	 */
    static void modifyFile(String filePath, String oldString, String newString)
    {
    	// modify the file as specified
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
