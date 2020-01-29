def cmd_command(command):
	arr = command.split()
	result = subprocess.run(
	    arr,
	    stdout=subprocess.PIPE,
	    stderr=subprocess.STDOUT,
	)

	return result.stdout.decode("utf-8")

def main():
	name = input("Enter username:\t")
	email = input("Enter email:\t")
	cmd_command("git init")
	#cmd_command("git clone https://github.com/AmanPriyanshu/chatroom.git .")
	cmd_command("git config --global user.name "+name)
	cmd_command("git config --global user.email "+email)
	f= open("chats.txt","w+")
	f.close()
	cmd_command("git status")
	cmd_command('git commit -m "Initial commit"')

main()
