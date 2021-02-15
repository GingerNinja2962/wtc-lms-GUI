
problems = {
        "HelloWorld" : "0cf50308-e8f5-429f-97af-d8a05bca2b3f",
        "Hangman1" : "291fe834-5e48-4c8d-a8eb-5dfba8e3cd3a",
        "Hangman2" : "9e760d4f-adc7-4184-8c6c-538dd5c02532",
        "Pyramid" : "aeda1496-2eeb-49ed-9c86-d84593456cc3",
        "Hangman3" : "c4ed8104-22a0-4b2b-96a8-879b4c9e6e69",
        "Outline" : "0b447f96-8fb9-4876-ae91-046267423a3e",
        "Mastermind1" : "eb04c6dc-ddee-4751-a999-6e28f7861978",
        "ToyRobt1" : "ef4e20e2-6ed5-4eea-93b6-78116b0083eb",
        "Mastermind2" : "ead9542e-a32a-43d2-bfcf-c60e7559611f",
        "Mastermind3" : "ec83fd21-6c13-4a78-9396-f57c8ffd3c83",
        "Recursion" : "decea39d-7a2a-45d9-bd08-1af152c94516",
        "ToyRobot2" : "e5be25a3-5fd4-4f71-8dc0-67e3b8b211bf",
        "Wordprocessing" : "254a6e98-30b6-4a8b-b255-a4e7aa0c4547",
        "ToyRobot3" : "8dea9e69-07da-440d-964c-08e868e11561",
        "AccountingApp" : "da2f7a67-be13-4e03-995d-1c63dc429bd6",
        "ToyRobot4" : "c96a3dc4-1ee0-4cac-8d78-11a63c8213fd",
        "ToyRobot5" : "f899e822-161f-4c92-9a42-7c7a2467c021",
        "TrollHunter" : "d3c51cf8-c246-478c-a3b2-fac6ac41df67",
        "FizzBuzz" : "72027eea-ee21-459b-83e9-84044edc6610"
}

review_problems = [
	"Using the wtc command line tool",
	"Hangman - Iteration 1",
	"Hangman - Iteration 2",
	"Hangman - Iteration 3",
	"Problem - Pyramid",
	"Problem - Outline",
	"Mastermind - Iteration 1",
	"Mastermind - Iteration 2",
	"Mastermind - Iteration 3",
	"Problem - Recursion",
	"Problem - Word Processing",
	"Problem - Accounting App",
	"Toy Robot - Iteration 1",
	"Toy Robot - Iteration 2",
	"Toy Robot - Iteration 3",
	"Toy Robot - Iteration 4",
	"Toy Robot - Iteration 5",
	"Problem - Fix the Bugs",
	"Unit Testing with Java > FizzBuzz"
]

help_data = """
usage: wtc-lms  [-h | --help]
		<command> [<args>]
        
These are the wtc-lms commands that can be used in various situations:
        
setup and login
	init               Creates the config file that will be used
	config             View your config file that was created
	token              View your token
	login              Used to login
	register           Used to register

various learning path options
	modules            View available modules
	topics             View available topics for a module
	problems           View available problems for a topic
	start              Starts a specific problem
	save [message]     Commits work and pushes to Origin, with optional commit message
	grade              Submits work for grading
	history            Displays grading history for a problem

working with reviews
	reviews            List your reviews
	accept             Accept a review invitation
	decline            Decline a review invitation
	review_details     List the details of a given review
	sync_review        Update the local copy of the grading repo to align with the provided review
	add_comment        Add a comment to a review
	edit_comment       Edit an existing review comment
	grade_review       Grade review (grade must be an integer between 0 and 10 inclusively)

others
	-c, -credits       Displays students who have contributed in forms of ideas/suggestions into the lms

"""