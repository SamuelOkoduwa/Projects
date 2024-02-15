#include <stdio.h>	//A header file library that works with input and output functions such as print f

// int main() {	//It is a function where it's code is executed
// 	printf("Hello world!");	//It is a function used to output/print text to the screen
// 	return 0;	//Ends the main() function
// }

// Creating a variable
int main () {
	int myNum = 12;
	printf("%d \n", myNum);

	char myLetter = 'a';
	printf("My number is %d and my letter is %c \n", myNum, myLetter);

	printf("Kindly look at the next colum for data types \n");
	printf("You can declare multiple variables on multiple lines \n");

	char a = 65, b = 66, c = 'f';
	printf("%c %c %c \n\n", a, b, c);

	printf("The memory size below \n");
	int myInt;
	float myFloat;
	double myDouble;
	char myChar;

	printf("%lu\n", sizeof(myInt));
	printf("%lu\n", sizeof(myFloat));
	printf("%lu\n", sizeof(myDouble));
	printf("%lu\n", sizeof(myChar));

	// int answer = get
	return 0;
}

