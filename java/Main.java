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
		//uaf & atf
	}
	public void sell(String in){
		//atf
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
}
