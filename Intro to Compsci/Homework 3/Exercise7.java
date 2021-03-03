import java.util.Scanner;
import java.lang.Math;

public class Exercise7 {
	public static void printMenu(){
		System.out.println("\n1. View your Balance");
		System.out.println("2. Deposit Cash");
		System.out.println("3. Withdraw Cash");
		System.out.println("4. Exit");
		System.out.print("\nEnter your selection: ");
	}

	public static void main(String[] args){
		double balance = 0.00;	

		Scanner input = new Scanner(System.in);

		boolean notExit = true;

		do{
			printMenu();
			
			int mode = input.nextInt();

			if (mode == 1){
				System.out.print("\nYour current balance is: ");
				System.out.printf("%.2f",balance);

			}
			else if (mode == 2){
				System.out.print("\nEnter the amount you want to deposit: ");
				double deposit = input.nextDouble();

				if (deposit > 0)
					balance += deposit;
				else{
					System.out.println(" Sorry not a valid deposit!");
				}
			}
			else if (mode == 3){
				System.out.print("\nEnter the amount you want to withdraw: ");
				double withdrawal = input.nextDouble();

				if (withdrawal <= balance)
					balance -= withdrawal;
				else
					System.out.println(" Sorry you dont have enough balance!");
			}
			else if (mode == 4){
				System.out.println("\nGoodbye");
				notExit = false;
			}
			else
				System.out.println("Invalid selection");

		} while (notExit);

		input.close();


	}
}