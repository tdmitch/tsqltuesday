---
id: 1641
title: 'T-SQL Tuesday #071 &#8211; SQL Server Audit'
date: '2015-09-01T22:38:02+00:00'
author: way0utwest
layout: post
permalink: '/071'
categories:
    - Uncategorized
tags:
    - '2015'
    - auditing
---

[Invitation ](http://sqlity.net/en/2890/tsql2sday-71-sql-server-audit/)from [Sebastian Meine](http://sqlity.net/en/blog/).

For this month, I would like to invite you to write about Auditing. Auditing is certainly a security related topic, and with that fits right in with the August topic ([Encryption](http://sqlbama.com/archive/2015/08/t-sql-tuesday-69-encryption/)).

But don’t write this up as yet another “boring” security topic. There are other use cases for auditing too. The built-in SQL Server Audit feature for example can be used to track down how many different applications are accessing a particular table.

<div>[![The result of a SQL Server Audit](http://sqlity.net/wp-content/uploads/2015/09/The_Result_of_a_SQL_Server_Audit.jpg)](http://sqlity.net/wp-content/uploads/2015/09/The_Result_of_a_SQL_Server_Audit.jpg)</div>There are several approaches you can take with this topic. You could tell us a story:

- Have you encountered a situation where auditing saved the day?
- Where you able to stop an ongoing attack because auditing alerted you?
- Have you encountered a situation, in which auditing would have been helpful, but was not set up?
- Have you worked with the SQL Server Audit feature? What is particularly interesting to you about it?
- Do you think that everybody should use some form of auditing? Let us know, why.
- Do you think auditing is a waste of resources? We would like to hear more.
- Are you forced to be compliant? Under what regulation? HIIPA, PCI, CCC? How did auditing help to get you compliant?

If stories are not your thing, let us know how you use auditing. Or, write about how to use a fascinating piece of SQL Server Audit.

- What are the advantages and disadvantages of SQL Server Audit over other possible audit implementations, like triggers, traces, [Extended Events](http://blogs.lessthandot.com/index.php/uncategorized/t-sql-tuesday-67-extended-events-target-blog/) or external tools like log file readers?
- How can you use SQL Server Audit to see if a particular table or procedure is still in use?
- What is the difference between a <span class="tt">Server Audit Specification</span> and a <span class="tt">Database Audit Specification</span> and when should you use which?
- SQL Server Audit is based on Extended Events. What does it offer that XEs do not provide?

Finally, you could go totally meta:

- How do you audit the audit? How do you make sure that the audit does not just get disabled by an adversary?
- How do you [monitor](http://www.cathrinewilhelmsen.net/2015/05/19/roundup-of-t-sql-tuesday-66-monitoring/) your audit log to make sure you get alerted when something irregular is happening?

I hope I was able to spark your interest. I can’t wait to see you (or at least your post) next week at the party.