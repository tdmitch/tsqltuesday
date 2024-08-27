---
id: 2321
title: 'T-SQL Tuesday #051 &#8211; Place Your Bets'
date: '2014-02-07T17:16:36+00:00'
author: way0utwest
layout: post
permalink: '/051'
categories:
    - Invitations
tags:
    - '2014'
---

[Invitation](http://www.sqlservercentral.com/blogs/sqlrnnr/2014/02/04/t-sql-tuesday-051-place-your-bets/) and [roundup](http://www.sqlservercentral.com/blogs/sqlrnnr/2014/02/19/t-sql-tuesday-051-bets-and-results/) from [Jason Brimhall](http://jasonbrimhall.info/).

All bets on the table please. This is the last call for bets, no new bets will be allowed.

This marks the 51st invitation for TSQL Tuesday. This also marks what should have been the month of the first SQL Saturday event in Las Vegas. But the house lost on that event so it was pushed out to April 5th.

With that loss and the subsequent push, it is time for you to put on your **[Poker Face](http://www.youtube.com/watch?v=bESGLojNYSo)**. This month TSQL Tuesday is taking on a Vegas theme. I want to know about the gambles within your databases or not within your databases that you have seen over the years.

When has somebody (a CTO, Developer, Business User) placed a bet that was far too risky in your opinion? What kinds of gambles have been parlayed into catastrophes that could have been easily avoided? Once you are all in on these dogs and the aggregate limit has been reached, I want to know the handicap and how you fixed it.

Here are some examples.

1. I encountered a Sharepoint database server that had a 940 GB error log. The log was locked by antivirus software and couldn’t be cycled. Upon getting that resolved, I found the log was growing at about 500 MB an hour. There was a problem with Sharepoint talking to Active Directory.
2. A developer wrote a cursor that ran for 36 hours. Upon investigation, the cursor was re-written into a set-based script that ran in 42 seconds.
3. A 3rd party hosting service stopped SQL Server Services and deleted the system databases. The line on this bet was that they would have less than 15 minutes of outage and minimal revenue loss. The reality in this case was a sucker bet. They lost 4hrs of uptime and nearly 2 million dollars for the client.

I will leave it to you to offer up tokes and/or to discuss any trends this may have revealed to you while producing the rundown. Have fun with it and remember, with databases a big bet is not necessarily worth the risk.