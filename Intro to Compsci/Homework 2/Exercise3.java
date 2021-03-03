import java.util.Scanner;

public class Exercise3 {
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);

		System.out.print("Enter 1 to convert from dollars to euros; enter 2 to convert from euros to dollars: ");
		int type = input.nextInt();

		System.out.print("Enter the amount to convert: ");
		double amount = input.nextDouble();

		input.close();

		if (type == 1){
			double answer = amount*0.9;
			System.out.print("You entered in "+amount+" Dollars and they are equal to "+answer+" Euros");
		}
		else{
			double answer = amount/0.9;
			System.out.print("You entered in "+amount+" Euros and they are equal to "+answer+" Dollars");
		}





	

	}
}