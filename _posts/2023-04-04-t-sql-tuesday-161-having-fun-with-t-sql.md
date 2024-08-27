---
id: 4516
title: 'T-SQL Tuesday #161 &#8211; Having Fun with T-SQL'
date: '2023-04-04T13:31:00+00:00'
author: way0utwest
layout: post
permalink: '/161'
categories:
    - Invitations
tags:
    - '2023'
    - t-sql
---

[Invitation ](https://sqlreitse.com/2023/04/04/t-sql-tuesday-161-invitation-having-fun-with-t-sql/)and [writeup ](https://sqlreitse.com/2023/04/24/tsql2sday-161-the-writeup/)from [Reitse Eskens](https://sqlreitse.com/).

So, what to blog about this month. Well, it’s just been April fools day and as you’re reading this, you survived. Congratulations! But it did spark a question; what fun are we having with our code? And I’m not talking about commit messages in the Git repository or funny comments inside the code. I’m just as guilty on that part as the next programmer, but I’d like to focus on something else.

What are your most fun script, procedures or statements that you’ve written. Let me give two examples to set a bit of a stage.

The first fun script I wrote is one that has some history with it. About ten years ago when my wife was pregnant we were in the garden discussing the future. We were pulling out some weeds, trimming back some plants and enjoying the spring weather. For some reason we got onto the long term future and there a long running joke emerged. Our kid would have 18 years with us, when he would turn 18, the main present would be a set of moving boxes. Let’s call it a hint. Every now and then the joke serves it’s purpose to as a lightning rod when things don’t go like we like. The remark “well, only X years to go” relieves some of the stress. Nothing more serious than that. Until some co-workers got wind of the joke and asked for more precision. So, I wrote a very small piece of code that resulted in a number of results, the amount of years, day, hours, minutes and seconds until his 18th birthday.

```
CREATE OR ALTER PROCEDURE sp_howlong<br></br>AS<br></br>DECLARE @birthdate DATETIME;<br></br>SET @birthdate = '2013-01-01 00:00:00'; -- enter the correct birthday here<br></br>SET @birthdate = DATEADD (YEAR, 18, @birthdate);<br></br>WITH getData<br></br>AS ( SELECT<br></br>CONVERT (VARCHAR(12), DATEDIFF (SECOND, SYSDATETIME (), @birthdate) / 60 / 60 / 24 / 365) AS ' Year(s) '<br></br>, +CONVERT (VARCHAR(12), DATEDIFF (SECOND, SYSDATETIME (), @birthdate) / 60 / 60 / 24 % 365) AS ' Day(s) '<br></br>, +CONVERT (VARCHAR(12), DATEDIFF (SECOND, SYSDATETIME (), @birthdate) / 60 / 60 % 24) AS ' Hour(s) '<br></br>, +CONVERT (VARCHAR(2), DATEDIFF (SECOND, SYSDATETIME (), @birthdate) / 60 % 60) AS ' Minute(s) '<br></br>, +CONVERT (VARCHAR(2), DATEDIFF (SECOND, SYSDATETIME (), @birthdate) % 60) AS ' Second(s) ')<br></br>SELECT CONCAT_WS (':', [ Year(s) ], [ Day(s) ], [ Hour(s) ], [ Minute(s) ], [ Second(s) ]) AS [This is how long…]<br></br>FROM getData;
```

What this procedure does is getting the birthdate as it happened, adding 18 years because that’s the target. The select then calculates the differences based on on the modulo function (the % sign). As I’m converting to seconds, I can work my way down from years to seconds by changing the modulo.

I’ve used this technique in some customer cases as well to determine if a certain record had expired its valid date or not.

The second one is more work related but fun nonetheless. It’s one I didn’t think of myself but it was heavily inspired on the work from [Brent Ozar.](https://www.brentozar.com/archive/2020/07/get-alerted-when-your-sql-server-restarts-with-sp_sendstartupmail/) I’m a great believer in attribution, and as this is mostly his work, check out the link to get a quick working setup and adjust it to your needs.

  
The reason for this script came from a customer who wanted to know if all databases were up and running if a server went into a failover, reboot or whatever. We discussed the issue shortly and, having paid attention in classes of Brent, I came up with a procedure that runs after startup and checks the state of all the databases. If all the databases are online and running, it will send an email stating everything is OK. If one of the databases didn’t get to the normal state, the email will have a line for each database with the state it was in when the procedure ran. Of course, this isn’t watertight and fails if either the mailserver is down or the server never returns to normal running, but that is being monitored elsewhere.

Now this script has been running for years and just one simple ‘out of order’ message has been seen: Database Offline. Every other database has resumed without hesitation or error. Yes, some database servers are just summer children.

So without further ado, time to hit your keyboard and write about your funny scripts, code.