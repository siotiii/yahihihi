while True:
    print(100 * "=")
    print("                               ASSOCIATE IN COMPUTER TECHNOLOGY I.")
    print("                                  \033[95mFUNDAMENTALS OF PROGRAMMING\033[0m        ")
    print("                                         Learn python")
    print(100 * "=")
    print("CHOOSE: ")
    print("\033[93m 1. PRELIM\033[0m")
    print("\033[93m 2. MIDTERMS\033[0m")
    print("\033[93m 3. FINALS\033[0m")
    print("\033[91m 0. EXIT\033[0m")

    print(100 * "_")
    sear = str(input("Search: "))
    print(100 * "_")

    if sear == "0":
        print("\nThank you for using the ACT Learning System. Goodbye! 1,2,3, go kanya kanya na!\n")
        print("Special thanks to our profs: \n")
        print("Sir Regie and sir Jomar!")
        print("4kO to, Si nIcol3 Siot3co na MAhal n4 mahal KayO heart heart oppa peace out...")
        break

    elif sear == "1":
        while True:
            print("\nCHOOSE PRELIM LESSON: ")
            print("\033[94m[a] LESSON 1 : Introduction to Programming & Python\033[0m")
            print("\033[94m[b] LESSON 2 : Python Basic Syntax\033[0m")
            print("\033[94m[c] LESSON 3 : Arithmetic Operators and Expressions\033[0m")
            print("\033[94m[d] LESSON 4 : Basic Input and Output in Python\033[0m")
            print("\033[92m[e] TRY PRELIM ADVENTURE MODE ( Simple Quiz! )\033[0m")
            print("\033[91m[x] Back to Main Menu\033[0m")

            print(100 * "_")
            sea = str(input("Search: ")).lower()
            print(100 * "_")

            if sea == "x":
                break

            elif sea == "a":
                print("Lesson 1 : Introduction to Programming & Python")
                print(100 * "_")
                print(">>What is Programming?")
                print("- Programming is giving instructions to a computer so it can perform tasks.")
                print()
                print(">>What is a Programming Language?")
                print("- A programming language is a special language that computers understand.")
                print()
                print("    Common Languages:")
                print("   > Python → Easy to learn, great for beginners")
                print("   > C / C++ → Fast and powerful")
                print("   > Java → Platform independent")
                print("   > JavaScript → For websites")
                print("   > PHP → For web backends")
                print()
                print(">>What is Python Programming?")
                print("Python is a widely-used programming language that was created by Guido van Rossum in 1991.")
                print("A dutch software engineer best known for creating the Python programming language in 1991")
                print()
                print("Why Learn Python?")
                print("     1. \033[92mSimple and easy to learn\033[0m - Great for beginners")
                print("     2. \033[92mReadable syntax\033[0m – Code looks almost like English")
                print("     3. \033[92mVersatile\033[0m – Used in many fields (AI, web, automation, games, etc.)")
                print("     4. \033[92mHuge community\033[0m – Lots of support, tutorials, and libraries")
                print()
                print("WHAT DO YOU NEED TO START PYTHON PROGRAMMING?")
                print("\n                 Professional IDEs / Code Editors\n")
                print("    PyCharm        ""         VS Code ""                 Jupyter Notebook ")
                print("(by JetBrains)""         (Visual Studio Code)""           / JupyterLab")
                input("\nPress Enter to continue...")

            elif sea == "b":
                while True:
                    print("CHOOSE: ")
                    print("Lesson 2 : Python Basic Syntax")
                    print("1. SYNTAX")
                    print("2. CASE - SENSITIVE")
                    print("3. INDENTATION")
                    print("4. PRINTING OUTPUT")
                    print("5. PYTHON COMMENTS")
                    print("6. VARIABLES, CONSTANTS, AND DATA TYPES IN PYTHON")
                    print("7. BASIC DATA TYPES IN PYTHON")
                    print("x. Back to Prelim Menu")
                    print(100 * "_")
                    sheath = str(input("Search: ")).lower()
                    print(100 * "_")

                    if sheath == "x":
                        break

                    elif sheath == "1":
                        print("SYNTAX")
                        print("Syntax refers to the set of rules that tells us how to correctly write a program in Python.")
                        print()
                        print("Example: Your First Program")
                        print()
                        print("INPUT: ")
                        print('print("Hello, World!")')
                        print('print("Welcome to ACT102 - Fundamentals of Programming")')
                        print()
                        print("OUTPUT: ")
                        print("Hello, World!")
                        print("Welcome to ACT102 - Fundamentals of Programming")
                        input("\nPress Enter to continue...")

                    elif sheath == "2":
                        print("PYTHON IS CASE-SENSITIVE.")
                        print("~ Python treats uppercase and lowercase letters differently.")
                        print("\n\033[92m✓ CORRECT\n\033[0m")
                        print('1  name = "John"'.ljust(28) + "→  Create variable name")
                        print('2  print(name)'.ljust(28) + "→  Print the value of name")
                        print()
                        print(100 * "_")
                        print("\n\033[91m✗ INCORRECT\033[0m\n")
                        print('1  name = "John"'.ljust(28) + "→  Error! Name")
                        print('2  print(Name)'.ljust(28) + "   is not the same as name.")
                        print()
                        print(100 * "_")
                        input("\nPress Enter to continue...")

                    elif sheath == "3":
                        print("INDENTATION")
                        print("Unlike other programming languages, Python uses indentation (spaces) to define blocks of code.")
                        print()
                        print("\033[92m✓ CORRECT\033[0m")
                        print(100 * "_")
                        print('1  age = 18'.ljust(32) + "←  Assign value to variable")
                        print('2')
                        print('3  if age >= 18:'.ljust(32) + "←  Check condition")
                        print('4      print("Adult")'.ljust(32) + "←  Indented (inside the block)")
                        print()
                        print("\033[91m✗ INCORRECT\033[0m")
                        print(100 * "_")
                        print('1  age = 18')
                        print('2')
                        print('3  if age >= 18:')
                        print('4  print("Adult")'.ljust(32) + "←  Not indented (outside the block)")
                        input("\nPress Enter to continue...")

                    elif sheath == "4":
                        print("PRINTING OUTPUT")
                        print()
                        print("    \033[94m1. PRINT STATEMENT\033[0m")
                        print("    The print() function displays information on the screen.")
                        print()
                        print("\033[92mSyntax:\033[0m print(value) ")
                        print("\033[92mPRINT\033[0m – the function that displays output.")
                        print("\033[92m()\033[0m – parentheses that contain the information to be displayed.")
                        print("\033[92mVALUE\033[0m – the text, number, variable, or expression you want to show.")
                        print()
                        print("    \033[94m2. PRINTING TEXT\033[0m")
                        print("    Text (also called a string) must be enclosed in quotation marks.")
                        print(100 * "-")
                        print("\033[92m✓ CORRECT\033[0m")
                        print("~ Text (also called a string) must be enclosed in quotation marks.")
                        print('print("Hello, World!")'.ljust(36) + "→  Correct syntax")
                        print(" " * 36 + "   Uses double quotes inside the parentheses.")
                        print()
                        print(100 * "-")
                        print("\033[91m✗ INCORRECT\033[0m")
                        print('print(Hello, World!)'.ljust(36) + "→  Incorrect syntax")
                        print(" " * 36 + "   Missing quotes around the text.")
                        print(" " * 36 + "   Python treats Hello and World as variable names, not text.")
                        print()
                        print("    \033[94m3. PRINTING NUMBERS\033[0m")
                        print("     You can print numbers directly without quotation marks.")
                        print(100 * "-")
                        print("\033[92m✓ CORRECT\033[0m")
                        print('1  print(100)'.ljust(30) + "OUTPUT: 100")
                        print('2  print(25.5)'.ljust(30) + "        25.5")
                        print(" " * 30 + "Numbers (int, float): used without quotes.")
                        print(" " * 30 + "These are treated as numbers by Python.")
                        print()
                        print("\033[94m= ALSO CORRECT (DIFFERENT DATA TYPE)\033[0m")
                        print(100 * "-")
                        print('1  print("100")'.ljust(30) + "OUTPUT: 100")
                        print('2  print("25.5")'.ljust(30) + "        25.5")
                        print(" " * 30 + "Strings (str): values inside quotes are text.")
                        print(" " * 30 + "Output looks the same, but they are treated as text.")
                        print()
                        print("KEY DIFFERENCE: The output is the same, but the data type is different.")
                        print(100 * "-")
                        print('NUMBER (int / float)'.ljust(30) + "STRING (str)")
                        print('print(type(100))'.ljust(30) + 'print(type("100"))')
                        print("<class 'int'>".ljust(30) + "<class 'str'>")
                        print()
                        print("Remember: Use quotes for text, not for numbers.")
                        input("\nPress Enter to continue...")

                    elif sheath == "5":
                        print("PYTHON COMMENTS")
                        print("- Comments are ignored by Python.")
                        print("- They are used to explain the code.")
                        print()
                        print("\033[92m✓ SINGLE-LINE COMMENT\033[0m")
                        print(100 * "-")
                        print('1  # This is a comment')
                        print('2')
                        print('3  print("Hello")')
                        print()
                        print(" " * 4 + "Uses the hash symbol #")
                        print(" " * 4 + "Comment continues until the end of the line.")
                        print(" " * 4 + "Used for: Short explanations, Disabling a line of code, Quick notes")
                        print()
                        print("\033[94m✓ MULTI-LINE COMMENT\033[0m")
                        print(100 * "-")
                        print('1  """')
                        print('2  This is')
                        print('3  a multi-line')
                        print('4  comment.')
                        print('5  """')
                        print('6')
                        print('7  print("Hello")')
                        print()
                        print(" " * 4 + 'Uses triple quotes """')
                        print(" " * 4 + 'Comment continues until the closing """.')
                        print(" " * 4 + "Used for: Longer explanations, Describing functions, Adding documentation")
                        print(" " * 4 + "Note: The code inside triple quotes is ignored by Python.")
                        input("\nPress Enter to continue...")

                    elif sheath == "6":
                        print("1. WHAT IS A VARIABLE?")
                        print("- A variable is a named storage location used to keep data in a program.")
                        print("- The value of a variable can change while the program is running.")
                        print("Example: a, b, c, age, name")
                        print()
                        print("[ Variable Name ]".ljust(25) + "[ Variable Name ]")
                        print("age".ljust(25) + "name")
                        print("20".ljust(25) + '"John"')
                        print("[ Stored Value ]".ljust(25) + "[ Stored Value ]")
                        print()
                        print(100 * "-")
                        print("VARIABLE NAMING RULES:")
                        print(100 * "-")
                        print("- A variable can have a short name (like x and y)")
                        print("  or a more descriptive name (age, carname, total_volume).")
                        print()
                        print("\033[94mSHORT NAMES\033[0m".ljust(40) + "\033[92mDESCRIPTIVE NAMES\033[0m")
                        print("x = 10".ljust(31) + "age = 25")
                        print("y = 20".ljust(31) + 'carname = "Toyota"')
                        print("total = x + y".ljust(31) + "total_volume = 1250.5")
                        print("print(total)".ljust(31) + "print(total_volume)")
                        print("Examples: x, y, i, j, n, temp".ljust(31) + "Examples: age, carname, total_volume, student_score")
                        print()
                        print("Remember: Both are valid. Choose the one that makes your code clear.")
                        print("- Use short names for quick, simple tasks or temporary variables.")
                        print("- Use descriptive names when your code grows or is read by others.")
                        print()
                        print(100 * "-")
                        print("- A variable name must start with a letter or the underscore character.")
                        print("- A variable name cannot start with a number.")
                        print()
                        print("\033[92m✓ VALID\033[0m".ljust(40) + "\033[91m✗ INVALID\033[0m")
                        print("age = 20  (starts with a letter)".ljust(37) + "1stValue = 10  (starts with a number)")
                        print("_value = 100  (starts with underscore)".ljust(37) + "2total = 30  (starts with a number)")
                        print("total = 50  (starts with a letter)".ljust(37) + '123name = "John"  (starts with a number)')
                        print()
                        print("Tip: After the first character, you can use letters, numbers, and underscores.")
                        print("Why? Python won't know if it's a variable or a number!")
                        print()
                        print(100 * "-")
                        print("- Variable names are case-sensitive (age and AGE are two different variables).")
                        print()
                        print("Variable 1".ljust(25) + "Variable 2")
                        print("age = 18".ljust(25) + "AGE = 25")
                        print("This is a variable named age".ljust(30) + "This is a variable named AGE")
                        print("age  ≠  AGE")
                        print(100 * "-")
                        print("VARIABLE NAMING RULES:")
                        print(100 * "-")
                        print("\033[92m✓ GOOD\033[0m")
                        print("number".ljust(18) + "NUMBER".ljust(18) + "bread".ljust(18) + "spam23".ljust(18) + "_speed")
                        print()
                        print("\033[92m✓ Letter lowercase allowed - a b c\033[0m")
                        print("\033[92m✓ Letter uppercase allowed - A b C\033[0m")
                        print("\033[92m✓ Letters and numbers allowed - a 2 3\033[0m")
                        print("\033[92m✓ Underscore allowed - _abc\033[0m")
                        print()
                        print("\033[92mGood variable names\033[0m: start with a letter or underscore,")
                        print("and can contain letters, numbers, and underscores.")
                        print()
                        print("\033[91m✗ BAD\033[0m")
                        print("1number".ljust(18) + "#bread".ljust(18) + "var.12".ljust(18) + "space name".ljust(18) + "@value")
                        print("✗ Cannot start with a number - 1abc ")
                        print("\033[91m✗ Cannot cannot use special characters like # - #abc\033[0m ")
                        print("\033[91m✗ Cannot cannot use special characters like . - var.12\033[0m ")
                        print("\033[91m✗ Cannot cannot use spaces . - space name\033[0m ")
                        print("\033[91m✗ Cannot cannot use special characters like @ - @value\033[0m ")

                        print("\033[91mBad variable names\033[0m: do not start with a number and cannot")
                        print("contain spaces or special characters (! @ # $ % etc.).")
                        print()
                        print("\033[94m! DIFFERENT (CASE-SENSITIVE)\033[0m")
                        print("number = 10".ljust(18) + "Number = 20".ljust(18) + "NUMBER = 30")
                        print("Variable names are case-sensitive. These are three different variables.")
                        print()
                        print(100 * "-")
                        print("ASSIGNED VALUE TO VARIABLE")
                        print(100 * "-")
                        print("- In programming, we store data in variables.")
                        print("- We assign a value to a variable using the = (assignment operator).")
                        print()
                        print('first_name  =  "John"')
                        print("    ↑          ↑")
                        print("VARIABLE NAME  VALUE")
                        print("The name we choose to represent the data (follows naming rules).")
                        print("The data we store in the variable (can be text, number, etc.).")
                        print()
                        print(100 * "-")
                        print("OUTPUT VARIABLES")
                        print(100 * "-")
                        print("~ The Python print() function is often used to output variables.")
                        print()
                        print("EXAMPLE CODE")
                        print('1  school = "Clark College"'.ljust(
                            35) + "→  We store the text Clark College in a variable named school.")
                        print('2  print(school)'.ljust(35) + "→  We use print() to display the value of the variable school.")
                        print()
                        print("OUTPUT:")
                        print(">>> Clark College")
                        print()
                        print(100 * "-")
                        print("~ In the print() function, you output multiple variables, separated by a comma:")
                        print()
                        print("EXAMPLE CODE")
                        print('1  a = "I"'.ljust(35) + "→  Store I in variable a")
                        print('2  b = "LOVE"'.ljust(35) + "→  Store LOVE in variable b")
                        print('3  c = "CCST"'.ljust(35) + "→  Store CCST in variable c")
                        print('4  # print multiple variables')
                        print('5  print(a, b, c)'.ljust(35) + "→  print() displays the values of a, b, and c separated by spaces")
                        print()
                        print("OUTPUT:")
                        print(">>> I LOVE CCST")
                        print()
                        print(100 * "-")
                        print("~ In the print() function, you output multiple variables, separated by a +:")
                        print()
                        print("EXAMPLE CODE")
                        print('1  x = "I "'.ljust(35) + "→  Store I in variable x")
                        print('2  y = "LOVE "'.ljust(35) + "→  Store LOVE in variable y")
                        print('3  z = "CCST"'.ljust(35) + "→  Store CCST in variable z")
                        print('4  # Add the variables')
                        print('5  print(x + y + z)'.ljust(35) + "→  Add the values of x, y, and z and display the result")
                        print()
                        print("OUTPUT:")
                        print(">>> I LOVE CCST")
                        print()
                        print("HOW IT WORKS:")
                        print('"I "  +  "LOVE "  +  "CCST"  =  "I LOVE CCST"')
                        print("The + operator joins (concatenates) the string values together in order: x first, then y, then z.")
                        input("\nPress Enter to continue...")

                    elif sheath == "7":
                        print("DATA TYPES")
                        print(100 * "_")
                        print("- Data types are categories that tell Python what kind of data a variable stores.")
                        print("- They determine the type of value a variable can hold and what operations")
                        print("  can be performed on that value.")
                        print()
                        print("int".ljust(10) + "Integer numbers".ljust(20) + "Whole numbers (no decimal part).")
                        print(" " * 30 + "Examples: 10, 25, -7, 100")
                        print()
                        print("float".ljust(10) + "Decimal numbers".ljust(20) + "Numbers with a decimal point.")
                        print(" " * 30 + "Examples: 12.5, 3.14, -0.001, 2.0")
                        print()
                        print("str".ljust(10) + "String or text".ljust(20) + "Text or characters inside quotes.")
                        print(" " * 30 + 'Examples: "Hello", "Juan", "CCST"')
                        print()
                        print("bool".ljust(10) + "Boolean values".ljust(20) + "Represents one of two values: True or False.")
                        print(" " * 30 + "Examples: True, False")
                        print()
                        print("Each data type stores a different kind of value.")
                        print("Choosing the right type helps your program work correctly!")
                        print()
                        print(100 * "_")
                        print("DECLARATION OF VARIABLES")
                        print(100 * "_")
                        print("VARIABLE".ljust(15) + "VALUE".ljust(12) + "DATA TYPE".ljust(15) + "DESCRIPTION")
                        print("name".ljust(15) + '"Maria"'.ljust(12) + "str".ljust(15) + "Stores text inside quotes.")
                        print("age".ljust(15) + "20".ljust(12) + "int".ljust(15) + "Stores whole numbers.")
                        print("grade".ljust(15) + "89.5".ljust(12) + "float".ljust(15) + "Stores numbers with decimal points.")
                        print("is_enrolled".ljust(15) + "True".ljust(12) + "bool".ljust(15) + "Stores True or False values.")
                        print()
                        print("Python Code:")
                        print('name = "Maria"')
                        print("age = 20")
                        print("grade = 89.5")
                        print("is_enrolled = True")
                        print()
                        print(100 * "_")
                        print("ASSIGNED VALUE AND OUTPUT THE VALUE")
                        print(100 * "_")
                        print('1  name = "Maria"'.ljust(32) + "# string")
                        print('2  age = 20'.ljust(32) + "# integer")
                        print('3  grade = 89.5'.ljust(32) + "# float")
                        print('4  is_enrolled = True'.ljust(32) + "# boolean")
                        print('5  print(name)'.ljust(32) + "---------> # prints name")
                        print('6  print(age)'.ljust(32) + "---------> # prints age")
                        print('7  print(grade)'.ljust(32) + "---------> # prints grade")
                        print('8  print(is_enrolled)'.ljust(32) + "---> # prints status")
                        print()
                        print("OUTPUT:")
                        name = "Maria"
                        age = 20
                        grade = 89.5
                        is_enrolled = True
                        print(name)
                        print(age)
                        print(grade)
                        print(is_enrolled)
                        input("\nPress Enter to continue...")

                    else:
                        print("\033[91mInvalid choice. Please try again.\033[0m")

            elif sea == "c":
                print("Lesson 3 : Arithmetic Operators and Expressions ")
                print("WHAT ARE ARITHMETIC OPERATORS?")
                print("- Arithmetic operators are symbols used to perform mathematical")
                print("  calculations on numbers. They work the same way as the operators")
                print("  used in everyday mathematics.")
                print()
                print(100 * "_")
                print("PYTHON ARITHMETIC OPERATORS")
                print(100 * "_")
                print("OPERATOR".ljust(12) + "DESCRIPTION".ljust(48) + "EXAMPLE".ljust(12) + "RESULT")
                print("+".ljust(12) + "Addition: Adds two values.".ljust(50) + "5 + 3".ljust(12) + str(5 + 3))
                print("-".ljust(12) + "Subtraction: Subtracts second from first.".ljust(50) + "10 - 4".ljust(12) + str(
                    10 - 4))
                print(
                    "*".ljust(12) + "Multiplication: Multiplies two values.".ljust(50) + "7 * 2".ljust(12) + str(7 * 2))
                print(
                    "/".ljust(12) + "Division: Returns a decimal result.".ljust(50) + "15 / 3".ljust(12) + str(15 / 3))
                print(
                    "//".ljust(12) + "Floor Division: Returns whole number only.".ljust(50) + "17 // 3".ljust(12) + str(
                        17 // 3))
                print("%".ljust(12) + "Modulus: Returns the remainder.".ljust(50) + "10 % 3".ljust(12) + str(10 % 3))
                print("**".ljust(12) + "Exponentiation: Raises to the power.".ljust(50) + "2 ** 3".ljust(12) + str(
                    2 ** 3))
                print()
                print(100 * "_")
                print("EXPRESSIONS IN PYTHON")
                print(100 * "_")
                print("- An expression is a combination of values, variables, and operators")
                print("  that evaluates to a result.")
                print()
                print("PYTHON EXAMPLE: ADD TWO NUMBERS")
                print("1  a = 10".ljust(30) + "# first number")
                print("2  b = 5".ljust(30) + "# second number")
                print("3")
                print("4  result = a + b".ljust(30) + "# add the numbers")
                print('5  print("The result is:", result)'.ljust(30) + "# display the result")
                print()
                print("OUTPUT:")
                a = 10
                b = 5
                result = a + b
                print("10 + 5 = 15")
                print("The result is:", result)
                print()
                print(100 * "_")
                print("ARITHMETIC OPERATORS EXAMPLES  (a = 10, b = 5)")
                print(100 * "_")
                print("Addition:".ljust(30), a + b)
                print("Subtraction:".ljust(30), a - b)
                print("Multiplication:".ljust(30), a * b)
                print("Division:".ljust(30), a / b)
                print("Floor Division:".ljust(30), a // b)
                print("Modulus:".ljust(30), a % b)
                print("Exponentiation:".ljust(30), a ** b)
                print()
                print(100 * "_")
                print("EXPRESSIONS IN PYTHON: QUIZ")
                print(100 * "_")
                print("a = 2")
                print("b = 3")
                print("c = 4")
                print("print(a + b * c)")
                print()
                print("A. 20".ljust(15) + "B. 14".ljust(15) + "C. ERROR")
                print()
                print(100 * "_")
                print("PEMDAS (ORDER OF OPERATIONS)")
                print(100 * "_")
                print("~ Python follows the order of operations (PEMDAS):")
                print("P  Parentheses".ljust(25) + "First")
                print("E  Exponents".ljust(25) + "  |")
                print("M  Multiplication".ljust(25) + "  |")
                print("D  Division".ljust(25) + "  |")
                print("A  Addition".ljust(25) + "  v")
                print("S  Subtraction".ljust(25) + "Last")
                input("\nPress Enter to continue...")

            elif sea == "d":
                print("Lesson 4 : Basic Input and Output in Python")
                print("ACCEPTING USER INPUT")
                print(100 * "_")
                print("- Purpose of input in programming")
                print("- Real-life analogies (e.g., asking for a user's name and responding)")
                print()
                print(100 * "_")
                print("PYTHON INPUT - GETTING USER INPUT")
                print(100 * "_")
                print('1  name = input("Enter your name: ")')
                print('2  age = input("Enter your age: ")')
                print()
                print("- Using input() function")
                print('- Syntax: variable = input("Prompt message: ")')
                print("- All input is string type by default")
                print()
                print(100 * "_")
                print("FORMATTING OUTPUT: Using comma , in print()")
                print(100 * "_")
                print('1  name = input("Enter your name: ")')
                print('2  age = input("Enter your age: ")')
                print('3  print("Name: ", name)')
                print('4  print("Age: ", age)')
                print()
                print("SAMPLE OUTPUT:")
                print("Name:  Maria")
                print("Age:  20")
                print()
                print(100 * "_")
                print("CONVERTING INPUT TO OTHER DATA TYPES")
                print(100 * "_")
                print("B. Float Input (for decimal numbers)")
                print()
                print('1  grade = float(input("Enter your grade: "))')
                print('2  print(f"Your grade is {grade}")')
                print()
                print("C. Boolean Input (True or False using conditions)")
                print()
                print('1  answer = input("Are you a student? (yes/no): ")')
                print('2  is_student = answer.lower() == "yes"')
                print('3  print("Student status:", is_student)')
                print()
                print("Example Program (Combining All)")
                print()
                print('1  name = input("Enter your name: ")')
                print('2  age = int(input("Enter your age: "))')
                print('3  grade = float(input("Enter your final grade: "))')
                print('4  print(f"Student: {name}, Age: {age}, Final Grade: {grade}")')
                print()
                print("SAMPLE OUTPUT:")
                print("Student: Maria, Age: 20, Final Grade: 89.5")
                input("\nPress Enter to continue...")

            elif sea == "e":
                print("" + 100 * "=")
                print("                                PRELIM ADVENTURE MODE!  - ACT 102")
                print(100 * "=")
                print("Answer the following questions. Type the letter of your choice.\n")

                score = 0
                total = 10

                print("1. Who created the Python programming language?")
                print("   a) James Gosling")
                print("   b) Guido van Rossum")
                print("   c) Bjarne Stroustrup")
                print("   d) Dennis Ritchie")
                ans = input("Your answer: ").lower()
                if ans == "b":
                    print("\033[92mCorrect!\033[0m\n")
                    score += 1
                else:
                    print("\033[91mWrong! The correct answer is b) Guido van Rossum\033[0m\n")

                print("2. Which of the following is a valid variable name?")
                print("   a) 1st_name")
                print("   b) student-name")
                print("   c) student_name")
                print("   d) student name")
                ans = input("Your answer: ").lower()
                if ans == "c":
                    print("\033[92mCorrect!\033[0m\n")
                    score += 1
                else:
                    print("\033[91mWrong! The correct answer is c) student_name\033[0m\n")

                print("3. What will be the output of this code?")
                print('   print(10 // 3)')
                print("   a) 3.33")
                print("   b) 3")
                print("   c) 1")
                print("   d) 10")
                ans = input("Your answer: ").lower()
                if ans == "b":
                    print("\033[92mCorrect!\033[0m\n")
                    score += 1
                else:
                    print("\033[91mWrong! The correct answer is b) 3\033[0m\n")

                print("4. Python is a ______ language.")
                print("   a) case-insensitive")
                print("   b) case-sensitive")
                print("   c) both a and b")
                print("   d) none of the above")
                ans = input("Your answer: ").lower()
                if ans == "b":
                    print("\033[92mCorrect!\033[0m\n")
                    score += 1
                else:
                    print("\033[91mWrong! The correct answer is b) case-sensitive\033[0m\n")

                print("5. Which operator is used for exponentiation in Python?")
                print("   a) ^")
                print("   b) **")
                print("   c) *")
                print("   d) //")
                ans = input("Your answer: ").lower()
                if ans == "b":
                    print("\033[92mCorrect!\033[0m\n")
                    score += 1
                else:
                    print("\033[91mWrong! The correct answer is b) **\033[0m\n")

                print("6. What is the data type of the value True?")
                print("   a) int")
                print("   b) str")
                print("   c) bool")
                print("   d) float")
                ans = input("Your answer: ").lower()
                if ans == "c":
                    print("\033[92mCorrect!\033[0m\n")
                    score += 1
                else:
                    print("\033[91mWrong! The correct answer is c) bool\033[0m\n")

                print("7. How do you write a single-line comment in Python?")
                print("   a) // This is a comment")
                print("   b) # This is a comment")
                print("   c) /* This is a comment */")
                print("   d) -- This is a comment")
                ans = input("Your answer: ").lower()
                if ans == "b":
                    print("\033[92mCorrect!\033[0m\n")
                    score += 1
                else:
                    print("\033[91mWrong! The correct answer is b) # This is a comment\033[0m\n")

                print("8. What does the input() function return by default?")
                print("   a) integer")
                print("   b) float")
                print("   c) string")
                print("   d) boolean")
                ans = input("Your answer: ").lower()
                if ans == "c":
                    print("\033[92mCorrect!\033[0m\n")
                    score += 1
                else:
                    print("\033[91mWrong! The correct answer is c) string\033[0m\n")

                print("9. Which of the following is correct indentation?")
                print("   a) if age >= 18:")
                print("      print('Adult')")
                print("   b) if age >= 18:")
                print("   print('Adult')")
                print("   c) Both a and b")
                print("   d) None of the above")
                ans = input("Your answer: ").lower()
                if ans == "a":
                    print("\033[92mCorrect!\033[0m\n")
                    score += 1
                else:
                    print("\033[91mWrong! The correct answer is a)\033[0m\n")

                print("10. What is the result of 17 % 5?")
                print("    a) 3")
                print("    b) 2")
                print("    c) 3.4")
                print("    d) 5")
                ans = input("Your answer: ").lower()
                if ans == "b":
                    print("\033[92mCorrect!\033[0m\n")
                    score += 1
                else:
                    print("\033[91mWrong! The correct answer is b) 2\033[0m\n")

                print(100 * "=")
                print(f"Your Score: {score}/{total}")

                percentage = (score / total) * 100
                print(f"Percentage: {percentage:.0f}%")

                if percentage >= 90:
                    print("\033[92mExcellent! You have a strong understanding of the Prelim topics, Galing!\033[0m")
                elif percentage >= 70:
                    print("\033[93mGood job! Review the topics you missed (huhu).\033[0m")
                else:
                    print("\033[91mKeep practicing! Review mo yung lesson ulit!\033[0m")

                print(100 * "=")
                input("\nPress Enter to go back to Prelim Menu...")

            else:
                print("\033[91mInvalid choice. Please try again.\033[0m")


    elif sear == "2":
        while True:
            print("\nCHOOSE MIDTERM LESSON")
            print("\033[94m[a] LESSON 1 : Conditional Statements in Python \033[0m")
            print("\033[94m[b] LESSON 2 : Logical Operator \033[0m")
            print("\033[92m[e] TRY MIDTERM ADVENTURE MODE ( Simple Quiz! )\033[0m")
            print("\033[91m[x] Back to Main Menu\033[0m")

            print(100 * "_")
            bukol = str(input("Search: ")).lower()
            print(100 * "_")

            if bukol == "x":
                break

            elif bukol == "a":
                while True:
                    print("CHOOSE: ")
                    print("Lesson 1 : Conditional Statements in Python")
                    print("1. Introduction to Conditional Statement")
                    print("2. Relational Operators")
                    print("3. The if Statement")
                    print("4. The if-else Statement")
                    print("5. The if-elif-else Statement")
                    print("6. Nested Condition in Python")
                    print("x. Back to Midterm Menu")
                    print(100 * "_")
                    bucole = str(input("Search: ")).lower()
                    print(100 * "_")

                    if bucole == "x":
                        break

                    elif bucole == "1":
                        print("INTRODUCTION TO CONDITIONAL STATEMENT")
                        print("- A Conditional Statement allows a program to make decisions based on whether")
                        print("a condition is True or False.")
                        print(100 * "_")
                        print("BASIC STRUCTURE")
                        print("if condition: ")
                        print("          Statement")
                        print(100 * "_")
                        print("if             -> The if keyword starts the conditional statement.")
                        print("condition      -> Evaluated. If True, the indented statement is executed.")
                        print("statement      -> The code that runs when the condition is True.")
                        print()
                        print("HOW IT WORKS")
                        print()
                        print("           START")
                        print("             |")
                        print("             ⬇  ")
                        print("          IS THE")
                        print( "        CONDITION _________no (False)")
                        print("           TRUE?                   |")
                        print("             |                     ⬇ ")
                        print("             |  yes(True)")
                        print("             ⬇               SKIP THE")
                        print("        EXECUTE THE          STATEMENT")
                        print("         STATEMENT               |")
                        print("             |                   ⬇ ")
                        print("             | ___________________")
                        print("             ⬇ ")
                        print("            END")
                        print(100 * "_")
                        print("EXAMPLE:")
                        print("age = 18")
                        print("if age >= 18:")
                        print('    print("You are an adult.")')
                        print("OUTPUT WHEN RUN:")
                        age = 18
                        if age >= 18:
                            print("You are an adult.")
                        print(100 * "_")
                        print("IN SIMPLE TERMS:")
                        print("The program checks the condition.")
                        print("If True, it does something.")
                        print("If False, it does nothing (or something else).")
                        print(100 * "_")
                        input("\nPress Enter to continue...")

                    elif bucole == "2":
                        print("RELATIONAL OPERATORS")
                        print("- Relational operators, also called comparison operators, are used to compare two values.")
                        print("The result is always either True or False.")
                        print()
                        print(54 * "_")
                        print("|Operator |    Meaning     |   Example   |   Result  |")
                        print(54 * "_")
                        print("|   ==    |    Equal to    |   10==10    |    TRUE   |")
                        print(54 * "_")
                        print("|   !=    |  Not equal to  |   10!= 5    |    TRUE   |")
                        print(54 * "_")
                        print("|   >     |  Greater than  |   10 > 5    |    TRUE   |")
                        print(54 * "_")
                        print("|   <     |    Less than   |   10 < 5    |    TRUE   |")
                        print(54 * "_")
                        print("|   >=    | Greater than or|   10>= 5    |    TRUE   |")
                        print("          |    equal to    |             |           |")
                        print(54 * "_")
                        print("|   <=    |   Less that or |   5<= 10    |    TRUE   |")
                        print("|         |    equal to    |             |           |")
                        print(54 * "_")
                        print()
                        print("Remember: ")
                        print("Relational operators compare values and always return either True or False.")
                        print(100 * "_")
                        print("EXAMPLE:")
                        print("score = 85")
                        print("print(score >= 75)")
                        print(100 * "_")
                        print("OUTPUT:")
                        score = 85
                        print(score >= 75)
                        print("Explanation: Since 85 is greater than or equal to 75,")
                        print("the expression score >= 75 evaluates to True.")
                        print(100 * "_")
                        input("\nPress Enter to continue...")

                    elif bucole == "3":
                        print("THE IF STATEMENTS")
                        print("- The if statement executes a block of code only when a condition is true.")
                        print(100 * "_")
                        print("SYNTAX")
                        print("if condition : ")
                        print("       statement(s)")
                        print(100 * "_")
                        print("if             -> The if keyword starts the conditional statement.")
                        print("condition      -> The condition is evaluated. If it is True, the indented block is executed.")
                        print("statement(s)   -> One or more statements that run when the condition is True.")
                        print("Note: If the condition is False, the indented block is skipped\n")
                        print()
                        print("HOW IT WORKS")
                        print()
                        print("           START")
                        print("             |")
                        print("             ⬇  ")
                        print("          IS THE")
                        print("        CONDITION _________no (False)")
                        print("           TRUE?                   |")
                        print("             |                     ⬇ ")
                        print("             |  yes(True)")
                        print("             ⬇               SKIP THE")
                        print("        EXECUTE THE           BLOCK")
                        print("       INTENDED BLOCK            |")
                        print("             |                   ⬇ ")
                        print("             | ___________________")
                        print("             ⬇ ")
                        print("            END")
                        print(100 * "_")
                        print("EXAMPLE:")
                        print("age = 20")
                        print("if age >= 18:")
                        print('    print("You are an adult.")')
                        print("OUTPUT WHEN RUN:")
                        age = 18
                        if age >= 18:
                            print("You are an adult.")
                        print(100 * "_")
                        print("What happens?")
                        print("If age is 18 or more (True), the message is printed.")
                        print("If age is less than 18 (False), nothing happens.\n")
                        print("Key points: ")
                        print("The block of code must be indented.")
                        print("The block runs only when the condition is True.")
                        input("\nPress Enter to continue...")

                    elif bucole == "4":
                        print("THE IF-ELSE STATEMENT")
                        print("- The else statement provides an alternative when the if condition is false.")
                        print(100 * "_")
                        print("SYNTAX")
                        print("if condition : ")
                        print("         statement")
                        print("else :")
                        print("         statement")
                        print(100 * "_")
                        print("Keypoints: ")
                        print("Use else when you want an alternative action if the if condition is False.")
                        print("Only one of the if or else block will be executed.\n")
                        print("EXAMPLE:")
                        print("score = 65")
                        print("if score >= 18:")
                        print('    print("PASSED")')
                        print("else: ")
                        print('    print("FAILED")\n')
                        print("OUTPUT:")
                        print("FAILED")
                        print(100 * "_")
                        print("EXPLANATION:")
                        print("In this example, score is 65, which is less than 75,")
                        print("so the else block runs and the program prints Failed.")
                        print(100 * "_")
                        print("Examples of if-else with All Comparison Operators")
                        print(54 * "_")
                        print("Examples of if-else with All Comparison Operators (score = 10)")
                        line = 108 * "_"
                        print(line)
                        print("| " + "Operator".ljust(9) + "| " + "Meaning".ljust(24) + "| " + "Condition".ljust(15)
                              + "| " + "When True".ljust(18) + "| " + "When False".ljust(18) + "|")
                        print(line)

                        rows = [
                            ("==", "Equal to", "score == 10", "Equal", "Not Equal"),
                            ("!=", "Not equal to", "score != 10", "Not Equal", "Equal"),
                            (">", "Greater than", "score > 10", "Greater", "Not Greater"),
                            ("<", "Less than", "score < 10", "Less", "Not Less"),
                            (">=", "Greater than or equal to", "score >= 10", "Greater or Equal", "Less"),
                            ("<=", "Less than or equal to", "score <= 10", "Less or Equal", "Greater"),
                        ]

                        for op, meaning, condition, true_out, false_out in rows:
                            print("| " + op.ljust(9) + "| " + meaning.ljust(24) + "| " + condition.ljust(15)
                                  + "| " + true_out.ljust(18) + "| " + false_out.ljust(18) + "|")
                            print(line)

                        print()
                        print("ACTUAL OUTPUT (score = 10):")
                        score = 10
                        print("==", end="  -> ")
                        if score == 10:
                            print("Equal")
                        else:
                            print("Not Equal")
                        print("!=", end="  -> ")
                        if score != 10:
                            print("Not Equal")
                        else:
                            print("Equal")
                        print(">", end="   -> ")
                        if score > 10:
                            print("Greater")
                        else:
                            print("Not Greater")
                        print("<", end="   -> ")
                        if score < 10:
                            print("Less")
                        else:
                            print("Not Less")
                        print(">=", end="  -> ")
                        if score >= 10:
                            print("Greater or Equal")
                        else:
                            print("Less")
                        print("<=", end="  -> ")
                        if score <= 10:
                            print("Less or Equal")
                        else:
                            print("Greater")
                        print()
                        input("\nPress Enter to continue...")

                    elif bucole == "5":
                        print("THE IF-ELIF-ELSE STATEMENT")
                        print(100 * "_")
                        print("~ The elif statement is used when there are multiple conditions to evaluate.")
                        print("  Python checks each condition from top to bottom and executes the")
                        print("  first condition that is True.")
                        print()
                        print("SYNTAX:".ljust(32) + "EXAMPLE:")
                        print("if condition1:".ljust(32) + "1  score = 85")
                        print("    statement".ljust(32) + "2  if score >= 90:")
                        print("elif condition2:".ljust(32) + '3      print("Excellent")')
                        print("    statement".ljust(32) + "4  elif score >= 80:")
                        print("    ...".ljust(32) + '5      print("Very Good")')
                        print("else:".ljust(32) + "6  elif score >= 75:")
                        print("    statement".ljust(32) + '7      print("Passed")')
                        print("".ljust(32) + "8  else:")
                        print("".ljust(32) + '9      print("Failed")')
                        print()
                        print("OUTPUT:")
                        score = 85
                        if score >= 90:
                            print("Excellent")
                        elif score >= 80:
                            print("Very Good")
                        elif score >= 75:
                            print("Passed")
                        else:
                            print("Failed")
                        print()
                        print("EXPLANATION:")
                        print("- score is 85")
                        print("- 85 >= 90 -> False")
                        print("- 85 >= 80 -> True ✓")
                        print('- Therefore, print("Very Good") is executed.')
                        print("- The remaining elif and else blocks are skipped.")
                        print("In an if-elif-else structure, only the first condition that")
                        print("evaluates to True is executed.")
                        print()
                        print("KEY POINTS:")
                        print("- Python checks conditions from top to bottom.")
                        print("- If a condition is True, its block is executed and the rest are skipped.")
                        print("- If none of the conditions are True, the else block is executed.")
                        input("\nPress Enter to continue...")

                    elif bucole == "6":
                        print("NESTED CONDITION IN PYTHON")
                        print(100 * "_")
                        print("- A nested condition is a condition inside another condition.")
                        print()
                        print("SYNTAX:")
                        print("if condition1:                 <- First condition is checked.")
                        print("    if condition2:             <- Checked only if the first condition is True.")
                        print("        # block of code")
                        print("    else:")
                        print("        # block of code")
                        print("else:                          <- This runs if the first condition is False.")
                        print("    # block of code")
                        print()
                        print(100 * "_")
                        print("DEBUTANT AGE RULES BY GENDER")
                        print(100 * "_")
                        print("~ A debutant is someone (male or female) who meets the minimum age")
                        print("  requirement and is being formally presented in a debut.")
                        print()
                        print("Male (M):   Is age >= 21?  Yes -> MALE DEBUTANT")
                        print("                           No  -> male, but not a debutant yet")
                        print("Female (F): Is age >= 18?  Yes -> FEMALE DEBUTANT")
                        print("                           No  -> female, but not a debutant yet")
                        print()
                        print(100 * "_")
                        print("CODE:")
                        print('gender = input("Enter gender (M/F): ")')
                        print('age = int(input("Enter age: "))')
                        print("if gender == 'M':")
                        print("    if age >= 21:")
                        print('        print("You are a MALE DEBUTANT.")')
                        print("    else:")
                        print('        print("You are a male, but not a debutant yet.")')
                        print("else:")
                        print("    if age >= 18:")
                        print('        print("You are a FEMALE DEBUTANT.")')
                        print("    else:")
                        print('        print("You are a female, but not a debutant yet.")')
                        print()
                        print("SAMPLE RUNS:")
                        print("M, 21 -> You are a MALE DEBUTANT.")
                        print("M, 19 -> You are a male, but not a debutant yet.")
                        print("F, 18 -> You are a FEMALE DEBUTANT.")
                        print("F, 16 -> You are a female, but not a debutant yet.")
                        print()
                        print("TIP: Read the flow from the top. The inner condition (age) is checked")
                        print("only if the outer condition (gender) is True.")
                        print()
                        print(100 * "_")
                        print("\033[94mTRY IT YOURSELF:\033[0m")
                        gender = input("Enter gender (M/F): ").strip().upper()
                        age = int(input("Enter age: "))
                        if gender == "M":
                            if age >= 21:
                                print("\033[94mYou are a MALE DEBUTANT.\033[0m")
                            else:
                                print("\033[94mYou are a male, but not a debutant yet.\033[0m")
                        else:
                            if age >= 18:
                                print("\033[95mYou are a FEMALE DEBUTANT.\033[0m")
                            else:
                                print("\033[95mYou are a female, but not a debutant yet.\033[0m")
                        input("\nPress Enter to continue...")

                    else:
                        print("\033[91mInvalid choice. Please try again.\033[0m")

            elif bukol == "b":
                while True:
                    print("\nLesson 2 : Logical Operators")
                    print("CHOOSE: ")
                    print("1. What are Logical Operators?")
                    print("2. The and Operator")
                    print("3. The or Operator")
                    print("4. The not Operator")
                    print("[x]. Back to Midterm Menu")
                    print(100 * "_")
                    bwaha = str(input("Search: ")).lower()
                    print(100 * "_")

                    if bwaha == "x":
                        break

                    elif bwaha == "1":
                        print("WHAT ARE LOGICAL OPERATORS?")
                        print("-Logical Operators are used to combine or reverse conditions in a Python Program.")
                        print("-They are commonly used with if, elif, and else.")
                        print()
                        print("Python has three logical operators:")
                        print(54 * "_")
                        print("|   OPERATOR    |            MEANING                 |")
                        print(54 * "_")
                        print("|     and       | Both conditions must be TRUE       |")
                        print(54 * "_")
                        print("|      or       | Atleast one condition must be TRUE |")
                        print(54 * "_")
                        print("|     not       | Reverse the result                 |")
                        print(54 * "_")
                        print("EXAMPLE:")
                        print("age = 20")
                        print("if age >= 18 and age <= 60:")
                        print('    print("Allowed")')
                        print()
                        print("Here, Python checks two conditions:")
                        print("1  age >= 18")
                        print("2  age <= 60")
                        print("Both must be True because we used and.")
                        print()
                        input("\nPress Enter to continue...")

                    elif bwaha == "2":
                        print("THE and OPERATOR")
                        print(100 * "_")
                        print("- The and operator returns True only when ALL conditions are True.")
                        print()
                        print("EXAMPLE:")
                        print("age = 20")
                        print("has_id = True")
                        print("if age >= 18 and has_id:")
                        print('    print("You are allowed to enter.")')
                        print("else:")
                        print('    print("You are not allowed to enter.")')
                        print()
                        print("EXPLANATION - The program checks:")
                        age = 20
                        has_id = True
                        print("1  age >= 18".ljust(20) + "->  " + str(age >= 18))
                        print("2  has_id".ljust(20) + "->  " + str(has_id))
                        print("Since both are True:  True and True = " + str(True and True))
                        print()
                        print("OUTPUT:")
                        if age >= 18 and has_id:
                            print("You are allowed to enter.")
                        else:
                            print("You are not allowed to enter.")
                        print()
                        print(100 * "_")
                        print("TRUTH TABLE - and")
                        print(100 * "_")
                        print("CONDITION A".ljust(16) + "CONDITION B".ljust(16) + "A and B")
                        for a, b in [(True, True), (True, False), (False, True), (False, False)]:
                            print(str(a).ljust(16) + str(b).ljust(16) + str(a and b))
                        print("Easy way to remember: AND = KAILANGAN LAHAT TRUE")
                        print()
                        input("\nPress Enter to continue...")

                    elif bwaha == "3":
                        print("THE or OPERATOR")
                        print(100 * "_")
                        print("- The or operator returns True when at least ONE condition is True.")
                        print()
                        print("EXAMPLE CODE:")
                        print('day = "Saturday"')
                        print('if day == "Saturday" or day == "Sunday":')
                        print('    print("It\'s the weekend!")')
                        print("else:")
                        print('    print("It\'s a regular school day.")')
                        print()
                        print("THE PROGRAM CHECKS:")
                        day = "Saturday"
                        print('1  day == "Saturday"'.ljust(26) + "->  " + str(day == "Saturday"))
                        print('2  day == "Sunday"'.ljust(26) + "->  " + str(day == "Sunday"))
                        print("Therefore:  True or False = " + str(True or False))
                        print()
                        print("OUTPUT:")
                        if day == "Saturday" or day == "Sunday":
                            print("It's the weekend!")
                        else:
                            print("It's a regular school day.")
                        print()
                        print(100 * "_")
                        print("TRUTH TABLE - or")
                        print(100 * "_")
                        print("CONDITION A".ljust(16) + "CONDITION B".ljust(16) + "A or B")
                        for a, b in [(True, True), (True, False), (False, True), (False, False)]:
                            print(str(a).ljust(16) + str(b).ljust(16) + str(a or b))
                        print("Easy way to remember: OR = KAHIT ISA LANG TRUE")
                        print()
                        print(100 * "_")
                        input("\nPress Enter to continue...")

                    elif bwaha == "4":
                        print("THE not OPERATOR")
                        print(100 * "_")
                        print("- The not operator reverses the result of a condition.")
                        print("True  ->  False")
                        print("False ->  True")
                        print()
                        print("EXAMPLE:")
                        print("is_raining = False")
                        print("if not is_raining:")
                        print('    print("You can go outside.")')
                        print("else:")
                        print('    print("Bring an umbrella.")')
                        print()
                        print("EXPLANATION:")
                        is_raining = False
                        print("1  is_raining = False")
                        print("2  not is_raining")
                        print("3  not False = " + str(not is_raining))
                        print("4  Output:", end=" ")
                        if not is_raining:
                            print("You can go outside.")
                        else:
                            print("Bring an umbrella.")
                        print()
                        print(100 * "_")
                        print("TRUTH TABLE - not")
                        print(100 * "_")
                        print("CONDITION".ljust(16) + "not CONDITION")
                        for c in [True, False]:
                            print(str(c).ljust(16) + str(not c))
                        print("Easy way to remember: NOT = BALIKTARIN ANG RESULT")
                        input("\nPress Enter to continue...")

                    else:
                        print("\033[91mInvalid choice. Please try again.\033[0m")

            elif bukol == "e":
                print("" + 100 * "=")
                print("                            MIDTERMS ADVENTURE MODE!  - ACT 102 (MIDTERMS)")
                print(100 * "=")
                print("Answer the following questions. Type the letter of your choice.\n")

                score = 0
                total = 10

                print("1. What allows a program to make decisions based on whether a condition is True or False?")
                print("   a) Loop statement")
                print("   b) Print statement")
                print("   c) Conditional statement")
                print("   d) Input statement")
                ans = input("Your answer: ").lower()
                if ans == "c":
                    print("\033[92mCorrect!\033[0m\n")
                    score += 1
                else:
                    print("\033[91mWrong! The correct answer is c) Conditional statement\033[0m\n")

                print("2. Which relational operator means 'equal to'?")
                print("   a) =")
                print("   b) ==")
                print("   c) !=")
                print("   d) >=")
                ans = input("Your answer: ").lower()
                if ans == "b":
                    print("\033[92mCorrect!\033[0m\n")
                    score += 1
                else:
                    print("\033[91mWrong! The correct answer is b) ==\033[0m\n")

                print("3. What will be the output of this code?")
                print('   print(10 != 5)')
                print("   a) True")
                print("   b) False")
                print("   c) 5")
                print("   d) Error")
                ans = input("Your answer: ").lower()
                if ans == "a":
                    print("\033[92mCorrect!\033[0m\n")
                    score += 1
                else:
                    print("\033[91mWrong! The correct answer is a) True\033[0m\n")

                print("4. What happens when the condition of an if statement is False?")
                print("   a) The program shows an error")
                print("   b) The indented block still runs")
                print("   c) The indented block is skipped")
                print("   d) The program closes")
                ans = input("Your answer: ").lower()
                if ans == "c":
                    print("\033[92mCorrect!\033[0m\n")
                    score += 1
                else:
                    print("\033[91mWrong! The correct answer is c) The indented block is skipped\033[0m\n")

                print("5. What will be the output of this code?")
                print("   score = 65")
                print("   if score >= 75:")
                print('       print("PASSED")')
                print("   else:")
                print('       print("FAILED")')
                print("   a) PASSED")
                print("   b) FAILED")
                print("   c) Error")
                print("   d) Nothing")
                ans = input("Your answer: ").lower()
                if ans == "b":
                    print("\033[92mCorrect!\033[0m\n")
                    score += 1
                else:
                    print("\033[91mWrong! The correct answer is b) FAILED\033[0m\n")

                print("6. Which keyword is used to check another condition after an if statement?")
                print("   a) else if")
                print("   b) elseif")
                print("   c) elif")
                print("   d) otherwise")
                ans = input("Your answer: ").lower()
                if ans == "c":
                    print("\033[92mCorrect!\033[0m\n")
                    score += 1
                else:
                    print("\033[91mWrong! The correct answer is c) elif\033[0m\n")

                print("7. What is a nested condition?")
                print("   a) A condition inside another condition")
                print("   b) A condition that never runs")
                print("   c) A condition that repeats forever")
                print("   d) A condition without an operator")
                ans = input("Your answer: ").lower()
                if ans == "a":
                    print("\033[92mCorrect!\033[0m\n")
                    score += 1
                else:
                    print("\033[91mWrong! The correct answer is a) A condition inside another condition\033[0m\n")

                print("8. The and operator returns True only when ______.")
                print("   a) at least one condition is True")
                print("   b) both conditions are False")
                print("   c) the result is reversed")
                print("   d) all conditions are True")
                ans = input("Your answer: ").lower()
                if ans == "d":
                    print("\033[92mCorrect!\033[0m\n")
                    score += 1
                else:
                    print("\033[91mWrong! The correct answer is d) all conditions are True\033[0m\n")

                print("9. What is the result of this expression?")
                print("   True or False")
                print("   a) True")
                print("   b) False")
                print("   c) Error")
                print("   d) None")
                ans = input("Your answer: ").lower()
                if ans == "a":
                    print("\033[92mCorrect!\033[0m\n")
                    score += 1
                else:
                    print("\033[91mWrong! The correct answer is a) True\033[0m\n")

                print("10. What is the result of not True?")
                print("    a) True")
                print("    b) False")
                print("    c) 1")
                print("    d) Error")
                ans = input("Your answer: ").lower()
                if ans == "b":
                    print("\033[92mCorrect!\033[0m\n")
                    score += 1
                else:
                    print("\033[91mWrong! The correct answer is b) False\033[0m\n")

                print(100 * "=")
                print(f"Your Score: {score}/{total}")

                percentage = (score / total) * 100
                print(f"Percentage: {percentage:.0f}%")

                if percentage >= 90:
                    print("\033[92mExcellent! You have a strong understanding of the Midterm topics, Galing!\033[0m")
                elif percentage >= 70:
                    print("\033[93mGood job! Review the topics you missed (huhu).\033[0m")
                else:
                    print("\033[91mKeep practicing! Review mo yung lesson ulit!\033[0m")

                print(100 * "=")
                input("\nPress Enter to go back to Midterm Menu...")

            else:
                print("\033[91mInvalid choice. Please try again.\033[0m")


    elif sear == "3":
        while True:
            print("\nCHOOSE FINALS TOPIC: ")
            print("\033[94m[a] INTRODUCTION TO ITERATION\033[0m")
            print("\033[94m[b] TYPES OF LOOPS IN PYTHON\033[0m")
            print("\033[94m[c] PYTHON FOR LOOP\033[0m")
            print("\033[94m[d] PYTHON WHILE LOOP\033[0m")
            print("\033[92m[e] TRY FINALS ADVENTURE MODE ( Simple Quiz! )\033[0m")
            print("\033[91m[x] Back to Main Menu\033[0m")
            print(100 * "_")
            zir = str(input("Search: ")).lower()
            print(100 * "_")

            if zir == "a":
                print("INTRODUCTION TO ITERATION")
                print(100 * "_")
                print("- Iteration means repeating a process.")
                print("- In programming, it means repeatedly executing a set of instructions.")
                print("- Each repetition is called an iteration.")
                print()
                print("for number in range(3):")
                print('    print("Welcome to Python!")')
                print()

                print("OUTPUT:")

                for number in range(3):
                    print(number + 1, "Welcome to Python!")
                print("The print() instruction executes once during each iteration.")
                print()
                print(100 * "_")
                print("- Iteration allows a program to perform the same task multiple times.")
                print()
                print("WITHOUT A LOOP:".ljust(34) + "USING A LOOP:")
                print('print("Study Python")'.ljust(34) + "for number in range(4):")
                print('print("Study Python")'.ljust(34) + '    print("Study Python")')
                print('print("Study Python")')
                print('print("Study Python")')
                print("Both produce the same output, but the loop makes the program shorter")
                print("and easier to modify. To repeat 100 times, change 4 to 100.")
                input("\nPress Enter to continue...")

            elif zir == "b":
                print("TYPES OF LOOPS IN PYTHON")
                print(100 * "_")
                print("- Python has two main types of loops: for and while.")
                print()
                print("for loop: repeats instructions for each item in a sequence.")
                print("          Useful when the number of repetitions is known.")
                print("while loop: repeats instructions while a condition is True.")
                print("            Useful when repetition depends on a condition.")
                print()
                print("for number in range(3):".ljust(34) + "count = 1")
                print('    print("Hello!")'.ljust(34) + "while count <= 3:")
                print("".ljust(34) + '    print("Hello!")')
                print("".ljust(34) + "    count += 1")
                print("Both examples print Hello! three times.")
                input("\nPress Enter to continue...")

            elif zir == "c":
                print("PYTHON for LOOP")
                print(100 * "_")
                print("SYNTAX:")
                print("for variable in sequence:")
                print("    statement(s)")
                print("variable: receives each item")
                print("sequence: items to loop through")
                print("Indented statements: the loop body")
                print()
                print("EXAMPLE CODE:")
                print("for number in range(4):")
                print('    print("Study Python")')

                print("OUTPUT:")
                for number in range(4):
                    print("Study Python")

                print("Use a colon 🙂) after the loop header and indent the loop body.")
                print()
                print(100 * "_")
                print("for LOOP: PRINT NUMBERS 1 TO 5")
                print(100 * "_")
                print("for number in range(1, 6):")
                print("    print(number)")

                print("OUTPUT:")

                for number in range(1, 6):
                    print(number)

                print("HOW IT WORKS:")
                print("1. range(1, 6) produces 1, 2, 3, 4, and 5.")
                print("2. The start value 1 is included; the stop value 6 is excluded.")
                print("3. Each iteration assigns the next value to number.")
                print("4. print(number) displays that value. After 5, the loop ends.")
                print("1 -> 2 -> 3 -> 4 -> 5   (5 iterations)")
                print()
                print(100 * "_")
                print("COUNTING DOWNWARD WITH range(): 5 TO 1")
                print(100 * "_")
                print("for number in range(5, 0, -1):")
                print("    print(number)")
                print("OUTPUT:")

                for number in range(5, 0, -1):
                    print(number)

                print("HOW IT WORKS:")
                print("1. Start at 5.")
                print("2. Stop before 0; the stop value is excluded.")
                print("3. The step -1 decreases the value by 1 each iteration.")
                print("4. print(number) displays 5, 4, 3, 2, and 1 on separate lines.")
                print()
                print(100 * "_")
                print("EXERCISE: OUTPUT ODD NUMBERS (for loop)")
                print(100 * "_")
                print("Write a for loop using range() to print the odd numbers from 1 to 9.")
                print("for number in range(1, 10, 2):")
                print("    print(number)")

                print("OUTPUT:")

                for number in range(1, 10, 2):
                    print(number)

                print()
                print("EXERCISE: OUTPUT EVEN NUMBERS (for loop)")
                print("Write a for loop using range() to print the even numbers from 2 to 10.")
                print("for number in range(2, 11, 2):")
                print("    print(number)")

                print("OUTPUT:")

                for number in range(2, 11, 2):
                    print(number)
                input("\nPress Enter to continue...")

            elif zir == "d":
                print("PYTHON while LOOP")
                print(100 * "_")
                print("SYNTAX:")
                print("while condition:")
                print("    statement(s)")
                print("condition: checked before each iteration")
                print("Indented statements: run while the condition is True.")
                print()
                print("EXAMPLE CODE:")
                print("count = 1")
                print("while count <= 5:")
                print("    print(count)")
                print("    count += 1")

                print("OUTPUT:")

                count = 1

                while count <= 5:
                    print(count)

                    count += 1

                print("count += 1 increases count by 1 each iteration.")
                print("When count becomes 6, the condition is False and the loop stops.")
                print()
                print(100 * "_")
                print("COUNTING DOWNWARD WITH A while LOOP: 5 TO 1")
                print(100 * "_")
                print("number = 5")
                print("while number >= 1:")
                print("    print(number)")
                print("    number -= 1")

                print("OUTPUT:")

                number = 5

                while number >= 1:
                    print(number)

                    number -= 1

                print("HOW IT WORKS:")
                print("1. Start with number = 5.")
                print("2. Repeat while number >= 1.")
                print("3. Print number, then decrease it by 1 using number -= 1.")
                print("4. Stop when number becomes 0 and the condition is False.")
                print()
                print(100 * "_")
                print("EXERCISE: OUTPUT ODD NUMBERS (while loop)")
                print(100 * "_")
                print("number = 1")
                print("while number <= 9:")
                print("    print(number)")
                print("    number += 2")

                print("OUTPUT:")

                number = 1

                while number <= 9:
                    print(number)

                    number += 2

                print()
                print("EXERCISE: OUTPUT EVEN NUMBERS (while loop)")
                print("number = 2")
                print("while number <= 10:")
                print("    print(number)")
                print("    number += 2")

                print("OUTPUT:")

                number = 2

                while number <= 10:
                    print(number)

                    number += 2

                print()
                print(100 * "_")
                print("REPEATING A PROGRAM WITH while True")
                print(100 * "_")
                print("while True:")
                print('    name = input("Enter your name (X to exit): ")')
                print('    if name.upper() == "X":')
                print('        print("Program stopped.")')
                print("        break")
                print('    print("Hello,", name)')
                print()
                print("HOW IT WORKS:")
                print("1. while True keeps the program repeating.")
                print("2. Enter a name to display a greeting.")
                print("3. Type X or x, then press Enter. break stops the loop.")
                print("The program repeats until the user chooses to exit.")
                print()
                print("TRY IT YOURSELF:")

                while True:

                    name = input("Enter your name (X to exit): ")

                    if name.upper() == "X":
                        print("Program stopped.")

                        break

                    print("Hello,", name)
                input("\nPress Enter to continue...")

            elif zir == "e":
                print("" + 100 * "=")
                print("                                 FINALS ADVENTURE MODE!  - ACT 102")
                print(100 * "=")
                print("Answer the following questions. Type the Answer.\n")
                quiz = [
                    ("What do we call each repetition of a loop?", ["iteration"]),
                    ("Which loop is best when the number of repetitions is known? (for/while)", ["for"]),
                    ("Which loop repeats while a condition is True? (for/while)", ["while"]),
                    ("Which keyword stops a loop?", ["break"]),
                    ("What symbol must come after the loop header? (name or symbol)", [":", "colon"]),
                    ("How many times does range(4) repeat? (number)", ["4"]),
                    ("What is the first number printed by range(1, 6)?", ["1"]),
                    ("What is the last number printed by range(1, 6)?", ["5"]),
                    ("Is the stop value in range() included? (yes/no)", ["no"]),
                    ("What step is used to count downward from 5 to 1? (number)", ["-1"]),
                    ("What does count += 1 do? (increase/decrease)", ["increase"]),
                    ("What does number -= 1 do? (increase/decrease)", ["decrease"]),
                    ("range(1, 10, 2) prints odd or even numbers? (odd/even)", ["odd"]),
                    ("range(2, 11, 2) prints odd or even numbers? (odd/even)", ["even"]),
                    ("Which statement keeps a program repeating forever until break? (while True/for)", ["while true"]),
                ]

                points = 0
                for number, (question, answers) in enumerate(quiz, start=1):
                    reply = input(f"{number}. {question} ").strip().lower()
                    if reply in answers:
                        print("   \033[92mCorrect ✓\033[0m")
                        points += 1
                    else:
                        print(f"   \033[91mWrong ✗\033[0m  The answer is: {answers[0]}")

                print()
                print(100 * "_")
                print(f"YOUR SCORE: {points} / {len(quiz)}")
                percent = points / len(quiz) * 100
                print(f"PERCENTAGE: {percent:.0f}%")
                if points == len(quiz):
                    print("AYWA PERFECT YA, IKA NA!")
                elif percent >= 75:
                    print("GALING NA!")
                elif percent >= 50:
                    print("Good, keep practicing!")
                else:
                    print("Review the lessons and try again!")
                input("\nPress Enter to continue...")

            elif zir == "x":
                print("Returning to Main Menu...")
                break

            else:
                print("Invalid choice. Please type a, b, c, d, e, or x.")

    else:
        print("\033[91mInvalid choice. Please enter 1, 2, 3, or 0.\033[0m")
