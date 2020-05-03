# Who Solved BOJ?

You can run two of python file.
- check.py : for just checking homework whether students solved problems.
- checkWithOption.py : for checking homework, plus, checking if students sovled problem before expiry date or used specific language... etc
( checkWithOption will be spent more time than check.py )

## Before you use this...

Before run this code, you have to install these python module

 - asyncio
 - bs4
 - requests
 - selenium ( You don't have to install selenium unless you want to run 'checkWithOption.py' )

And you should create 'students.txt', refer 'student-example.txt'
Also you should modify 'homeworkCodes.txt' what you want to check.
For checkWithOption.py, make sure that 'driver/chromedriver' is up to date and is available on your computer's OS.

## Result like this...

- This project permit you can check your student's BOJ homework.
- Like lower image, 'result.csv' will be printed.

<img src="_readme/result.png" style="zoom:50%;" />
