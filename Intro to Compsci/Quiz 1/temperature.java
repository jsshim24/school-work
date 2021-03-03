import java.util.Scanner;
import java.lang.Math;

public class temperature {

	//method to convert celsius to fahrenheit
	public static double tempC2F(double c){
		double f = (9.0/5.0)*c + 32;
		return f;
	}

	//method to convert fahrenheit to celsius
	public static double tempF2C(double f){
		double c = (5.0/9.0)*(f-32);
		return c;
	}

	//method to calculate wind chill from fahrenheit and mph
	public static double windChill(double f, double w){
		double chill = 91.4-((91.4-f)*(0.478+(0.301*Math.sqrt(w))-(0.02*w)));
		return chill;
	}

	//main method
	public static void main(String[] args){
		//Jun Seob Shim
		Scanner input = new Scanner(System.in);

		//print menu
		System.out.println("Enter a letter for one of the following options:");
		System.out.println(" C to convert a Celsius temperature to a Fahrenheit temperature,");
		System.out.println(" F to convert a Fahrenheit temperature to a Celsius temperature,");
		System.out.println(" W to calculate a wind chill factor,");
		System.out.println(" Q to exit the application.");

		//spacing
		System.out.println();

		//take mode input, and convert string to lowercase
		String mode = input.nextLine();
		String selected = mode.toLowerCase();

		//use to determine invalid input
		boolean invalidinput = true;

		//spacing
		System.out.println();

		//can't use if statements, while loop and break after 1 iteration
		while (selected.equals("c")==true){
			//valid input, so don't run last while loop (while invalidinput == true)
			invalidinput = false;

			//get celsius temperature from user
			System.out.print("Enter temperature in Celsius: ");
			double c = input.nextDouble();

			//call function and return fahrenheit conversion
			double f = tempC2F(c);

			//format and print
			System.out.printf("\n%.1f Celsius is %.1f Fahrenheit",c,f);

			//break after 1 iteration
			break;
		}

		//same process as Celsius to Fahrenheit, but flipped
		while (selected.equals("f")==true){
			invalidinput = false;

			System.out.print("Enter temperature in Fahrenheit: ");
			double f = input.nextDouble();

			double c = tempF2C(f);
			System.out.printf("\n%.1f Fahreneit is %.1f Celsius",f,c);

			break;
		}

		//if wind chill mode is selected
		while (selected.equals("w")==true){
			invalidinput = false;

			//get temperature (f) and wind speed (mph) from user
			System.out.print("Enter temperature in Fahrenheit: ");
			double f = input.nextDouble();

			System.out.print("Enter wind speed in mph: ");
			double w = input.nextDouble();

			//call function with 2 arguments (temp and wind speed)
			double wind = windChill(f,w);

			//format and print to screen
			System.out.printf("\nWhen temperature is %.1f Fahrenheit and wind speed is %.1f mph, wind chill factor is %.1f",f,w,wind);

			break;
		}

		//if mode selected is quit
		while (selected.equals("q")==true){
			invalidinput = false;

			System.out.println("Exiting... have a nice day!");

			break;
		}

		//if a valid input wasn't entered (aka if invalidinput wasn't changed to false above)
		while (invalidinput){
			System.out.println("Incorrect entry, program terminated!");

			break;
		}

		input.close();

	}
}