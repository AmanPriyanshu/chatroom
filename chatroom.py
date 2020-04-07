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

def input_chat(room_name):
	cmd_command("clear")
	inp = input("Enter msg or -e EXIT:")
	if inp == '-e':
		return 0
	desc = cmd_command("git config --list")
	desc = desc[desc.find("user.name=")+len("user.name="):]
	desc = desc[:desc.find("\n")]
	inp = desc+ ":" + inp
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
		cmd_command("git push origin "+room_name)
		cmd_command("git pull origin "+room_name)
		cmd_command("clear")
		read = read_write(False, "")
		for i in read:
			print(i)

def read_write(bool, txt):
	if bool:
		file_w = open("chats.txt","a")
		file_w.write(txt + "\n")
		file_w.close()
	return read

def main():
	a = 1
	room_name = input('room_name:\t')
	while a != 0:
		a = input_chat(room_name)
		cmd_command("clear")

main()
# An attempt to create a simple chatroom using git. Hope you understood.
