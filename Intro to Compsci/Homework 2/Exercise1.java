import java.util.Scanner;

public class Exercise1 {
	public static void main(String[] args){


	//Create a scanner
	Scanner input = new Scanner(System.in);

	System.out.print("Enter a value for x: ");
	double x = input.nextDouble();

	System.out.print("Enter a value for y: ");
	double y = input.nextDouble();

	input.close();

	double answer = (3+4*x)/5 - 10*(y-5)/x + 9*(4/x+(9+x)/y);
	System.out.println("The answer is " + answer);


	}
}