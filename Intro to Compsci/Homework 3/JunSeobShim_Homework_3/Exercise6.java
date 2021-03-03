import java.util.Scanner;
import java.lang.*;

public class Exercise6 {

	public static boolean isAlphaNumeric(String string){
		return string != null && string.matches("^[a-zA-Z0-9]*$");
	}

	public static boolean isAlpha(String string){
		return string != null && string.matches("^[a-zA-Z]*$");
	}

	public static boolean isNum(String string){
		return string != null && string.matches("^[0-9]*$");
	}

	public static boolean oneDigit(String string){
		int numCount = 0;
		for (int i = 0; i < string.length(); i++){
			char a = string.charAt(i);
			if ((Character.isDigit(a)) == true)
				numCount ++;
		}

		if (numCount == 1)
			return true;
		else
			return false;
	}

	public static boolean isUpperNum(String string){
		return string != null && string.matches("^[A-Z0-9]*$");
	}

	public static boolean isLowerNum(String string){
		return string != null && string.matches("^[a-z0-9]*$");
	}

	public static void main(String[] args){

		Scanner input = new Scanner(System.in);

		System.out.print("Enter password: ");
		String password = input.nextLine();

		input.close();

		if ((isAlphaNumeric(password)) == true){
			if ((password.length()) < 8)
				System.out.println("Weak Password");
			else
				if ((password.length()) < 13){
					if (isAlpha(password) == true || isNum(password) == true)
						System.out.println("Medium Password");
					else
						if ((oneDigit(password)) == true){
							if (isUpperNum(password) == true || isLowerNum(password) == true)
								System.out.println("OK Password");
							else
								System.out.println("Strong Password");
						}
						else
							System.out.println("Invalid Password");
				}
				else
					System.out.println("Awesome Password");
		}
		else
			System.out.println("Invalid Password");

	}
}