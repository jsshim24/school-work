import java.util.Scanner;

public class Exercise5 {
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);

		System.out.print("Enter first integer: ");
		int x = input.nextInt();

		System.out.print("Enter second integer: ");
		int y = input.nextInt();

		input.close();

		int sum = x+y;
		int diff = x-y;

		double dy = y;
		double div = x/dy;

		int mult = x*y;
		int rem = x%y;

		System.out.println("Sum of x and y is: "+sum);
		System.out.println("Subtraction of x and y is: "+diff);
		System.out.println("Division of x and y is: "+div);
		System.out.println("Multiplication of x and y is: "+mult);
		System.out.println("Remainder of x divided by y is: "+rem);

	}
}