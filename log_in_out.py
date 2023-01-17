# define the var search_string to help us out in our loop
search_string = "UserSessionActor"

# we open both Lucid.log and app.log's contents and import them into log1 and log 2 respectively
# then we initiate a for and if loop to help us pinpoint the exact locations of the string we need and print that guy out
# I also had to use ISO-8859-1 encoding because of some characters in the logs causing an error when launching the script

print("=====================================================\nBELOW YOU WILL FIND THE LOG IN AND LOG OUT INSTANCES\n=====================================================")

with open("Lucid.log", encoding="ISO-8859-1") as log1, open("app.log", encoding="ISO-8859-1") as log2:
	for line in log1:
		if search_string in line:
			print(line)
	for line in log2:
		if search_string in line:
			print(line)

