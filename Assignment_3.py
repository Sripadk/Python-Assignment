class Assignment3:
    #This class defination as per OOPS programming concept for Assignment 3.
    def Q1():
        import logging
        logging.basicConfig(filename="Q1.log",level=logging.INFO,format="%(asctime)s %(name)s %(levelname)s %(message)s")
        # Write a Python Program to Check if a Number is Positive, Negative or Zero?
        print("This is Python program to check if the entered number is positive or negative or Zero")
        logging.info("Program start")
        try:
            a = int(input("kindly enter the integer"))
            if a < 0:
                logging.info("The entered number is negative")
                return "The entered number is negative"
            elif a > 0:
                logging.info("The entered number is positive")
                return "The entered number is positive"
            elif a==0:
                logging.info("The entered number is Zero")
                return "The entered number is Zero"
        except Exception as e:
            logging.exception(e)
#Assignment3.Q1()
    def Q2():
        import logging
        logging.basicConfig(filename="Q2.log", level=logging.INFO,format="%(asctime)s %(name)s %(levelname)s %(message)s")
        #Write a Python Program to Check if a Number is Odd or Even?
        print("Python Program to Check if a Number is Odd or Even")
        logging.info("Program Start")
        try:
            a = int(input("kindly enter the integer"))
            logging.info("entered value is %s", a)
            if a <= 1:
                logging.info("entered number is less than 1")
            elif a%2 == 0:
                logging.info("Even Number")
            else:
                logging.info("Odd Number")
        except Exception as e:
            logging.exception(e)
#Assignment3.Q2()
    def Q3():
        import logging
        logging.basicConfig(filename="Q3.log",level=logging.INFO,format="%(asctime)s %(name)s %(levelname)s %(message)s")
        #Write a Python Program to Check Leap Year
        logging.info("Program start")
        try:
            a = int(input("enter the year"))
            logging.info(("entered year is %s",a))
            if a%400 ==0 and a%100 == 0:
                logging.info("Entered year %s is a leap year",a)
            elif a%4 == 0 and a % 100 != 0:
                logging.info("entered year %s is a leap year",a)
            else:
                logging.info("Entered year %s is not a leap year",a)
        except Exception as e:
            logging.exception(e)
#Assignment3.Q3()
    def Q4():
        # Write a Python Program to Check Prime Number?
        import logging
        logging.basicConfig(filename="Q4.log",level=logging.INFO,format="%(asctime)s %(name)s %(levelname)s %(message)s")
        logging.info("program start to check if the given number is prime")
        try:
            a = int(input("Enter the number"))
            if a > 1:
                for i in range (2,int(a/2)+1):
                    if a%i == 0:
                        logging.info("The entered number %s is not a prime number",a)
                    else:
                        logging.info("Entered number %s is a prime number",a)
                    break
            else:
                logging.info("Kindly enter a value greater than 1, %s is not a prime number",a)
        except Exception as e:
            logging.exception(e)
#Assignment3.Q4()

    def Q5():
        # Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
        import logging
        logging.basicConfig(filename="Q5.log",level=logging.INFO,format="%(asctime)s %(name)s %(levelname)s %(message)s")
        logging.info("Program Start to print all the prime numbers between 1 - 1000")
        try:
            l = [1]
            for i in range(2, 1001):
                a = 0
                for j in range(2, int(i / 2) + 1):
                    if i % j == 0:
                        a = 1
                        break
                if a == 0:
                    l.append(i)
            logging.info(l)
        except Exception as e:
            logging.exception(e)
#Assignment3.Q5()