import java.util.Scanner;

public class Exercise4 {
	public static void main(String[] args){

		Scanner input = new Scanner(System.in);

		System.out.print("Please enter numeric percentage: ");
		int grade = input.nextInt();

		if ((0 <= grade) && (grade <= 59))
			System.out.println("You entered " + grade +"%, your letter grade is F");
		else if ((60 <= grade) && (grade <= 63))
			System.out.println("You entered " + grade +"%, your letter grade is D-");
		else if ((64 <= grade) && (grade <= 67))
			System.out.println("You entered " + grade +"%, your letter grade is D");
		else if ((68 <= grade) && (grade <= 69))
			System.out.println("You entered " + grade +"%, your letter grade is D+");
		else if ((70 <= grade) && (grade <= 73))
			System.out.println("You entered " + grade +"%, your letter grade is C-");
		else if ((74 <= grade) && (grade <= 77))
			System.out.println("You entered " + grade +"%, your letter grade is C");
		else if ((78 <= grade) && (grade <= 79))
			System.out.println("You entered " + grade +"%, your letter grade is C+");
		else if ((80 <= grade) && (grade <= 83))
			System.out.println("You entered " + grade +"%, your letter grade is B-");
		else if ((84 <= grade) && (grade <= 87))
			System.out.println("You entered " + grade +"%, your letter grade is B");
		else if ((88 <= grade) && (grade <= 89))
			System.out.println("You entered " + grade +"%, your letter grade is B+");
		else if ((90 <= grade) && (grade <= 92))
			System.out.println("You entered " + grade +"%, your letter grade is A-");
		else if ((93 <= grade) && (grade <= 100))
			System.out.println("You entered " + grade +"%, your letter grade is A");

		input.close();

	}
}