import java.util.Scanner;
import java.lang.Math;

public class Exercise2 {
	public static void main(String[] args){

		Scanner input = new Scanner(System.in);

		System.out.print("\nEnter 1st number: ");
		int num1 = input.nextInt();

		System.out.print("Enter 2nd number: ");
		int num2 = input.nextInt();

		input.close();

		System.out.println("\nThe maximum of the two numbers is: " + Math.max(num1,num2));

	}
}