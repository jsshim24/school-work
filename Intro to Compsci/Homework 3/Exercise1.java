import java.util.Scanner;

public class Exercise1 {
	public static void main(String[] args){

		String password = "NYU42day";
		
		Scanner input = new Scanner(System.in);

		System.out.print("\nEnter password: ");

		String guess = input.nextLine();

		input.close();

		if (guess.equals(password))
			System.out.println("Valid Password");
		else
			System.out.println("Invalid Password");

	}
}