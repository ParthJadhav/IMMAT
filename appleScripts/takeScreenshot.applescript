# Get the File
on run {rep as String , phone as String}
set PATH_TO_REPOSITORY to rep
set path_to_file to PATH_TO_REPOSITORY & "my_screenshot.png"
# set it as a POSIX file
set my_file to (path_to_file as POSIX file)

# send stuff
tell application "Messages"
    set myid to get id of first service
	set theBuddy to participant phone of account id myid
	send my_file to theBuddy
end tell
end run