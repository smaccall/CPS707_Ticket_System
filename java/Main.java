import org.apache.commons.io.FileUtils;

import java.io.*;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

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
            while (scanner.hasNextLine()) {
                String hold = scanner.nextLine();
                Updater up = new Updater();
                System.out.println(hold);
                if (hold.length() > 0) {
                    if (hold.substring(0, 2).equals("01")) {
                        up.create(hold);
                    } else if (hold.substring(0, 2).equals("02")) {
                        up.delete(hold);
                    } else if (hold.substring(0, 2).equals("03")) {
                        up.sell(hold);
                    } else if (hold.substring(0, 2).equals("04")) {
                        up.buy(hold);
                    } else if (hold.substring(0, 2).equals("05")) {
                        up.refund(hold);
                    } else if (hold.substring(0, 2).equals("06")) {
                        up.addC(hold);
                    } else if (hold.substring(0, 2).equals("00")) {
                        System.out.println("WAAAA2");
                    } else {
                        System.out.println("WAAAA");
                    }
                }
            }
            scanner.close();
        } catch (FileNotFoundException ex) {
            System.out.print("File not found");
        }
    }

    /**
     * @param args
     * @throws IOException merge multiple daily transaction files into one
     */
    public static void merger() throws IOException {
        File dir = new File("src/output");
        PrintWriter pw = new PrintWriter("dtf.txt");
        String[] fileNames = dir.list();

        for (String fileName : fileNames) {
            if (fileName.contains("dtf")) {
                File f = new File(dir, fileName);
                // create object of BufferedReader
                BufferedReader br = new BufferedReader(new FileReader(f));
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
    public void addC(String input) throws IOException {
        // update the uaf file with the new ammount of credit for that user
        String nameB = input.substring(3, 19).strip();
        String roleB = input.substring(19, 22).strip();
        String amountB = input.substring(22).strip();
        Scanner s = new Scanner((new File("src/uaf.txt")));
        while (s.hasNextLine()) {
            String output = s.nextLine();
            if (output.substring(0, 16).strip().equals(nameB)) {
                Float total = Float.parseFloat(output.substring(20)) + Float.parseFloat(amountB);
                String news = String.format("%-15s", nameB) + " " + roleB + " " + (String.format("%09.2f", total));
                modifyFile("src/uaf.txt", output, news);
                break;
            }
        }
        s.close();
    }

    /**
     * @param input
     * @throws IOException
     */
    public void buy(String in) throws IOException {
        // update the atf file with the new amount of available tickets
        // update the uaf with buyers new credit amount
        Scanner s = new Scanner(new File("src/atf.txt"));
        String eTitle = in.substring(3, 22).strip();
        String sName = in.substring(23, 37).strip();
        String numTicketsStr = in.substring(38, 41).strip();
        int numTickets = Integer.parseInt(numTicketsStr);
        String newLine = "";
        int atfnumTickets = 0;
        String temp = "";
        while (s.hasNextLine()) {
            temp = s.nextLine();
            String atfETitle = temp.substring(0, 19).strip();
            String atfSName = temp.substring(20, 34).strip();
            if (atfETitle.equals(eTitle) && atfSName.equals(sName)) {
                String atfnumTicketsStr = temp.substring(35, 38).strip();
                atfnumTickets = Integer.parseInt(atfnumTicketsStr);
                String atfpriceTicketStr = temp.substring(39, 45).strip();
                //int newTotal = atfnumTickets - numTickets;

                newLine = String.format("%-19s", atfETitle) + " " + String.format("%-14s", atfSName) +
                        " " + String.format("%03d", numTickets) + " " + atfpriceTicketStr;

                break;
            }
        }
        Updater.modifyFile("src/atf.txt", temp, newLine);
        s.close();

        s = new Scanner(new File("src/uaf.txt"));
        sName = in.substring(23, 37).strip();
        numTicketsStr = in.substring(38, 41).strip();
        numTickets = Integer.parseInt(numTicketsStr);
        String priceTicketStr = in.substring(42, 48).strip();
        float priceTicket = Float.parseFloat(priceTicketStr);
        float totalCredit = (atfnumTickets - numTickets) * priceTicket;
        newLine = "";
        while (s.hasNextLine()) {
            temp = s.nextLine();
            String uafSName = temp.substring(0, 15).strip();
            if (uafSName.equals(sName)) {
                String uafType = temp.substring(16, 18).strip();
                String uafCreditsStr = temp.substring(20, 28).strip();
                float uafCredits = Float.parseFloat(uafCreditsStr);
                float newTotal = uafCredits + totalCredit;

                newLine = String.format("%-15s", uafSName) + " " + uafType + " " + (String.format("%09.2f", newTotal));
                break;
            }
        }
        Updater.modifyFile("src/uaf.txt", temp, newLine);
        s.close();
    }

    /**
     * @param input
     * @throws IOException
     */
    public void sell(String in) throws IOException {
        // update the atf file with the new ticket available for sale
        Updater.modifyFile("src/atf.txt", "END", in.substring(3) + "\nEND");

    }

    /**
     * @param input
     */
    public void create(String input) throws IOException {
        // update uaf file with the newly created user
        BufferedWriter writer = new BufferedWriter(
                new FileWriter("src/uaf.txt", true)  //Set true for append mode
        );
        writer.write(input.substring(3));
        writer.close();
    }

    /**
     * @param input
     */
    public void delete(String input) throws IOException {
        // delete account from uaf and any related tickets deleted from atf

        List<String> lines = FileUtils.readLines(new File("src/uaf.txt"));
        List<String> updatedLines = lines.stream().filter(s -> !s.contains(input.substring(3))).collect(Collectors.toList());
        FileUtils.writeLines(new File("src/uaf.txt"), updatedLines, false);

        lines = FileUtils.readLines(new File("src/atf.txt"));
        updatedLines = lines.stream().filter(s -> !s.contains(input.substring(3,19).strip())).collect(Collectors.toList());
        FileUtils.writeLines(new File("src/atf.txt"), updatedLines, false);
    }

    /**
     * @param input
     */
    public void refund(String in) throws IOException {
        // update buyer and sellers credit amount in uaf
        String buyer = in.substring(3, 18).strip();
        String seller = in.substring(18, 33).strip();
        String credit = in.substring(33).strip();
        String oldbuy = "";
        String oldsell = "";
        String buys = "";
        String sells = "";

        Scanner s = new Scanner((new File("src/uaf.txt")));
        while (s.hasNextLine()) {
            String line = s.nextLine();
            String name = line.substring(0, 16).strip();
            if (name.equalsIgnoreCase(buyer)) {
                String role = line.substring(16, 19).strip();
                float total = Float.parseFloat(line.substring(20)) + Float.parseFloat(credit);
                oldbuy = line;
                buys = String.format("%-15s", buyer) + " " + role + " " + String.format("%09.2f", (total));
            } else if (name.equalsIgnoreCase(seller)) {
                String role = line.substring(16, 19).strip();
                float total = Float.parseFloat(line.substring(20)) - Float.parseFloat(credit);
                oldsell = line;
                sells = String.format("%-15s", seller) + " " + role + " " + String.format("%09.2f", (total));

            }
        }
        modifyFile("src/uaf.txt", oldbuy,
                buys);
        modifyFile("src/uaf.txt", oldsell,
                sells);
        s.close();
    }

    /**
     * @param filePath, oldString, newString
     */
    static void modifyFile(String filePath, String oldString, String newString) throws IOException {
        // modify the file as specified
        File fileToBeModified = new File(filePath);
        String oldContent = "";
        BufferedReader reader = null;
        FileWriter writer = null;

        reader = new BufferedReader(new FileReader(fileToBeModified));
        //Reading all the lines of input text file into oldContent
        String line = reader.readLine();
        while (line != null) {
            oldContent = oldContent + line + System.lineSeparator();
            line = reader.readLine();
        }

        //Replacing oldString with newString in the oldContent
        String newContent = oldContent.replaceAll(oldString, newString);

        //Rewriting the input text file with newContent
        writer = new FileWriter(fileToBeModified);
        writer.write(newContent);

        reader.close();
        writer.close();

    }
}
