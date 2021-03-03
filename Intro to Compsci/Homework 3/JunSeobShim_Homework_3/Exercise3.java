import java.util.Scanner;
import java.lang.Math;
import java.util.Random;

public class Exercise3 {
	public static void main(String[] args){

		Scanner input = new Scanner(System.in);
		Random rand = new Random();

		boolean invalidinput = true;

		System.out.println("Enter letter \"a\" to generate a random char between (a-z), or enter letter \"A\" to generate a random char between (A-Z). ");

		do {
			String a = input.nextLine();

			if (a.equals("a")){
				invalidinput = false;
				int lower = rand.nextInt(26) + 97;
				System.out.println("Your random char is "+ (char)lower + ".");
			}
			else if (a.equals("A")){
				invalidinput = false;
				int upper = rand.nextInt(26) + 65;
				System.out.println("Your random char is "+ (char)upper + ".");
			}
			else
				System.out.println("Invalid entry, please try again.");
		} while (invalidinput);

		input.close();

	}
}