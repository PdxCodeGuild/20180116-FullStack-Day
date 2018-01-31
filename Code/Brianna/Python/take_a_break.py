import time, webbrowser

gapHours = 2
gapSeconds = gapHours * 60 * 60

print "This program started on {0} and will make you take a break every {1} hours\n".format(time.ctime(), gapHours)
print "When you're done with this program, you can either close this window or hit CTRL-C to quit."

while True:
    try:
        time.sleep(gapSeconds)
        webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
        while True:
            confirmation = raw_input("\nDid you actually take a break? >").lower()
            if confirmation in ("y", "yes", "yeah", "sure", "affirmative", "yup", "okay", "ok", "yea", "done"):
                print "\nPerfect! The next reminder will happen in {0} hours.".format(gapHours)
                break
            elif confirmation in ("n", "no", "nah", "nope", "negative", "nix"):
                print "\nTake a break, it's good for you."
                time.sleep(10)
                webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
                break
            else:
                print '\nYour response was not recognized as a "Yes" or "No", please try again.'
    except KeyboardInterrupt:
        raise SystemExit("\nGood job today!  Don't forget to start this program next time you're going to work for 3+ hours straight.")