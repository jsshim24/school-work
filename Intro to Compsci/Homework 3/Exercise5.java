import java.util.Scanner;

public class Exercise5 {
	public static void main(String[] args){
		String winter = "decemberjanuaryfebruary";
		String spring = "marchaprilmay";
		String summer = "junejulyaugust";
		String fall = "septemberoctobernovember";

		Scanner input = new Scanner(System.in);

		System.out.print("Enter month name: ");
		String inputmonth = input.nextLine();

		input.close();

		String month = "(.*)" + inputmonth.toLowerCase() + "(.*)";

		if ((winter.matches(month)) == true)
			System.out.println("Season is: Winter");
		else if ((spring.matches(month)) == true)
			System.out.println("Season is: Spring");
		else if ((summer.matches(month)) == true)
			System.out.println("Season is: Summer");
		else if ((fall.matches(month)) == true)
			System.out.println("Season is: Fall");
		else
			System.out.println("Error");

	}
}