##	Why should I use TypeScript?
JavaScript is a loosely typed language. It can be difficult to understand what types of data are being passed around in JavaScript.

In JavaScript, function parameters and variables don't have any information! So developers need to look at documentation, or guess based on the implementation.

TypeScript allows specifying the types of data being passed around within the code, and has the ability to report errors when the types don't match.

For example, TypeScript will report an error when passing a string into a function that expects a number. JavaScript will not.

##	How do I use TypeScript?
A common way to use TypeScript is to use the official TypeScript compiler, which transpiles TypeScript code into JavaScript.

Some popular code editors, such as Visual Studio Code, have built-in TypeScript support and can show errors as you write code!

###	Installing the Compiler
TypeScript has an official compiler which can be installed through npm. 
Within the npm project, run the following command to install the compiler:
-	**npm install typescript --save-dev**
	*Which should give you an output similar to:*
	added 1 package, and audited 2 packages in 2s
	found 0 vulnerabilities
-	The compiler is installed in the node_modules directory and can be run with: **npx tsc**
	*Which should give you an output similar to:*
	Version 4.5.5
	tsc: The TypeScript Compiler - Version 4.5.5
	Followed by a list of all the Common Commands.


###	Configuring the compiler
By default the TypeScript compiler will print a help message when run in an empty project.

The compiler can be configured using a tsconfig.json file.

You can have TypeScript create tsconfig.json with the recommended settings with: **npx tsc --init**
*Which should give you an output similar to:*

Created a new tsconfig.json with:
TS
  target: es2016
  module: commonjs
  strict: true
  esModuleInterop: true
  skipLibCheck: true
  forceConsistentCasingInFileNames: true

You can learn more at https://aka.ms/tsconfig.json


