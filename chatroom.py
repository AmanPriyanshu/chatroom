import subprocess

def cmd_command(command):
	arr = command.split()
	result = subprocess.run(
	    arr,
	    stdout=subprocess.PIPE,
	    stderr=subprocess.STDOUT,
	)

	return result.stdout.decode("utf-8")

print("OUT ",cmd_command("git init"))

def input_chat():
	inp = input("Enter msg or -e EXIT:")
	if len(inp) == 0:
		cmd_command("git pull origin chatroom")
		cmd_command("clear")
		read = read_write(False, "")
		print(read)
		return 1
	elif inp == '-e':
		return 0
	else:
		cmd_command("git pull origin chatroom")
		read = read_write(True, inp)
		cmd_command("git add -A")
		cmd_command('git commit -m "Update"')
		cmd_command("git push origin chatroom")
		cmd_command("git pull origin chatroom")
		cmd_command("clear")
		read = read_write(False, "")
		print(read)

def read_write(bool, txt):
	file = open("chats.txt","r")
	read = file.readlines() 
	file.close()
	read_data = ""
	for i in read:
		read_data += i
	if bool:
		file_w = open("chats.txt","w")
		file_w.write(read_data + txt + "\n")
		file_w.close()
	return read

def main():
	a = 1
	while a != 0:
		a = input_chat()

main()
