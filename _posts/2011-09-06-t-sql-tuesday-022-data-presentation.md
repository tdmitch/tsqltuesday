---
id: 3865
title: 'T-SQL Tuesday #022 &#8211; Data Presentation'
date: '2011-09-06T16:17:06+00:00'
author: way0utwest
layout: post
permalink: '/022'
categories:
    - Invitations
tags:
    - '2011'
    - 'data visualization'
---

[Invitation](http://www.sqlservercentral.com/blogs/pearlknows/2011/09/06/invitation-for-t-sql-tuesday-22-data-presentation/) and [round-up](http://www.sqlservercentral.com/blogs/pearlknows/2011/09/20/t-sql-tuesday-22-round-up-data-presentation/) from [Robert Pearl](http://www.sqlservercentral.com/blogs/pearlknows/).

**On to this month’s Topic**

What I have described above may be some behind-the-scenes details, but nevertheless, I packaged it in such a way that would provide entertainment (maybe ridicule?) to the reader at large. This was my ***presentation*** to the reader.

Therefore, the topic of this month’s T-SQL Tuesday is, “**data-presentation**” Or put better, formatting data for presentation to the end-user.

We may be the developers, and techno-geeks behind the code, whether simple, advanced, spaghetti, or otherwise. But, the data the user sees is most critical. The query output, the report, or data presentation, must be absolutely formatted in such a way that is easily understandable and readable by the end-user. The end-user can be the boss, supervisor, department head, the analyst, employees, or customers. And they must be the ones we cater our queries to!

It helps a lot, if we can simplify our code too. For example, when doing comparative analysis of the dataset results returned by a query, it makes it completely understandable if the output includes a percentage column. While for the end-user, it may be hard to digest milliseconds, megabytes, totals, and other assorted aggregated data, everyone can easily comprehend when something is X% percentage out of the whole.

For example, with the advent of [Common Table Expressions (CTE)](http://msdn.microsoft.com/en-us/library/ms190766.aspx), this makes it a whole lot easier to return all the data rows, along with the percentage in one single T-SQL pass.

Therefore, I am inviting you all to write about “data presentation” to the user. This can be in the form of T-SQL code, an SSRS report, etc. What can you do to streamline data presentation? I used a CTE, you can use one, but you don’t have to. No hard format, just be creative, and mention the importance of data presentation.