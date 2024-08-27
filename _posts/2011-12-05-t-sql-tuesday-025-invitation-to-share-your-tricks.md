---
id: 3878
title: 'T-SQL Tuesday #025 &#8211; Invitation to Share Your Tricks'
date: '2011-12-05T16:28:26+00:00'
author: way0utwest
layout: post
permalink: '/025'
categories:
    - Invitations
tags:
    - '2011'
    - t-sql
---

[Invitation](http://sqlblog.com/blogs/allen_white/archive/2011/12/05/t-sql-tuesday-025-invitation-to-share-your-tricks.aspx) and [followup](http://sqlblog.com/blogs/allen_white/archive/2011/12/17/t-sql-tuesday-25-followup-just-in-time-for-the-holidays.aspx) from Allen White

It doesn’t seem that long ago that having cool little tidbits of information about SQL Server made a huge difference in how effective you could be. Well, that’s still true, but let me give you an example.

```
SELECT name FROM sysobjects WHERE sysstat & 4 > 0
```

In the early days of SQL Server, this was the way to pull a list of the names of all the stored procedures in your database. The 4 bit in the sysstat column represented stored procedures. (1 represented user tables and 2 represented view, as I recall, so changing the WHERE clause to read WHERE sysstat &amp; 7 &gt; 0 returned all tables, views and stored procedures.)

As SQL Server has evolved, Microsoft has made it easier to query the metadata to determine what objects existed, adding columns that helped (like ‘Type’ in this case), catalog views, Dynamic Management Objects, etc.

So, the challenge for this month’s T-SQL Tuesday is: What T-SQL tricks do you use today to make your job easier? (Notice I didn’t say PowerShell – I have a bunch of those now, but this is T-SQL Tuesday, not PowerShell Tuesday.)