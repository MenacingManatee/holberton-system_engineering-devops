![server meme](https://preview.redd.it/t7r4r2643hv21.jpg?auto=webp&s=bdbbf4f0f8edc5141c0a7940ad601f0f94eec01b)
\***Summary:**\* Web page returned a 500 error for a period of 37 minutes, from 08:07 to 08:44, following an update that contained a typo, resulting al all users that accessed the page during that timeframe being unable to access site.

\***Timeline:**\*
* 07:57 - Final update for scheduled maintenance pushed to queue
* 08:00 - Scheduled maintenance update queued
* 08:01 - Update pushed to server.
* 08:06 - Server goes down temporarily to update
* 08:07 - \***Outage Begins**\* Server rebooted
* 08:09 - User report received on 500 error
* 08:10 - All traffic to web page confirmed to be failing
* 08:11 - Ticket taken by IT technician
* 08:14 - Ticket escalated to software department
* 08:15 - Brett starts investigating, starts with attempt to reboot nginx
* 08:19 - Strace used to log booting attempt of webserver, multiple “file not found” errors logged
* 08:20 - Investigation begun into file structure to ensure all files present and included
* 08:27 - Logs reviewed, discovered one file that was not found requested a “phpp” filetype
* 08:35 - Grep used to search files for the string “phpp”
* 08:39 - Typo discovered in an include command on line 137 of file ‘/var/www/html/wp-settings.php’
* 08:40 - Typo fixed using sed command
* 08:41 - Testing performed locally to ensure fix worked
* 08:43 - Fix pushed to server
* 08:44 - Server robooted
* 08:44 \***Outage ends**\*

\***Root Cause:**\* The cause of the outage was discovered to be a typo in a settings file that was updated shortly before the scheduled maintenance update was pushed to the server. Based on update logs for the file in question, it was most likely a last minute addition that did not receive the necessary time for error checking. The error was fixed simply by removing the typo, testing locally, and then pushing the change to the server before rebooting.

\***Corrective and preventative measures:**\*

**TODO/Done - Action - Reason**

TODO - add monitoring on server responses - Customer reports are useful but should not be relied upon

TODO - Require local testing before updates can be added to main server - Should reduce chances of typos and other errors remaining uncaught before users can see it

TODO - Require a hold period on changes before they can be pushed to the server, barring critical issues - Allows time for a peer to review, as a second set of eyes may catch previously unseen errors

TODO - Add alert for failure to find files after updating - Allows for quicker action in similar situations
