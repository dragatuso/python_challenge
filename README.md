First, I set up the folders for each challenge and organize the files.

PyBank Challenge:
For the PyBank Challenge I started by setting the path for opening the CSV file. At the beginning I had some difficulties with working with the file in the Resources folder but, after developping the code, I was able to set the correct path.
After that, I completed the calculations of the months and the net total amount of profits/losses. Before continuing to the next step, I realized that the code could be simplificed by not opeining the CSV file every time I wanted to calculate something, so I took the time to clean up the code.
Later, I focused on calculating the average change and the greatest increase and decrease in profits, both date and amount. Until this step, I was able to apply different examples seen in class and answers from Copilot to develop the code.
Finally, for printing the results in the txt file I took the code from https://blog.finxter.com/5-easy-ways-to-save-python-terminal-output-to-a-text-file/ and used the Method 2 listed in the blog.

PyPoll Challenge:
For completing this second challenge I leverage many of the code wrote for the PyBank Challenge.
First, I started setting the path for opening the CSV file and defining some variables an a list that later will be used to perform important calculations.
After that, I loop through the rows to calculate the total number of rows and creating a list with the names of all candidates. Later, I calculated the votes received by each candidate and calculated the corresponding percentages.
Finally, to finish printing the resutls, I used the if to define who the winner was, and printed the results in the txt file.