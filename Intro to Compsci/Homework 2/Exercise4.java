import java.util.Scanner;

public class Exercise4 {
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);

		System.out.print("Enter desired grade: ");
		String grade = input.nextLine();

		System.out.print("Enter minimum average required: ");
		double minave = input.nextDouble();

		System.out.print("Enter current average: ");
		double currentave = input.nextDouble();

		System.out.print("Enter how much the final counts (percentage of course grade): ") ;
		double percentage = input.nextDouble();
		double percentdecimal = percentage/100.0;

		input.close();

		double answer = (minave - (currentave*(1-percentdecimal)))/percentdecimal;
		System.out.printf("You need a score of %3.1f",answer,"on the final to get",grade);
	}
}