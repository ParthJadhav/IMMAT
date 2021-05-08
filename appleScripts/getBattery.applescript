on run {phone as String, batteryPercent}
tell application "Messages"
    set num to phone
    set myid to get id of first service
    set battery to batteryPercent
	set theBuddy to participant phone of account id myid
	send battery to theBuddy
end tell
end run