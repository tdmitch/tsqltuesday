---
id: 4327
title: 'T-SQL Tuesday #143 – Short code examples'
date: '2021-10-05T09:18:27+00:00'
author: way0utwest
layout: post
permalink: '/143'
categories:
    - Invitations
tags:
    - '2021'
    - t-sql
---

[Invitation](https://johnmccormack.it/2021/10/t-sql-tuesday-143-short-code-examples/) and [wrap-up](https://johnmccormack.it/2021/10/t-sql-tuesday-143-wrap-up/) from [John McCormack](https://johnmccormack.it/).

T-SQL Tuesday this month is going back to basics and its all about code. I’d like to know **“What are your go to handy short scripts”?**

What are those little short bits of code that you can’t live without? I’m talking about little snippets that are only a few lines, that you may even have memorised. It could be T-SQL, PowerShell, Python or anything else you use day to day.

e.g. I manage a lot of SQL agent jobs. Quite often, I need to find out which job has a certain t-sql string in the command so I’ll run:

```
SELECT * from msdb..sysjobs sj 
JOIN msdb..sysjobsteps sjs 
on sj.job_id = sjs.job_id 
where sjs.command like 'backup log%'
```

</div></div>Of course, there are many other ways to find this out including DBATools commands but sometime I just revert to memory for convenience.

Another one I like is to get the estimated completion rate of a backup or restore. Now there are better scripts than this but sometimes, nothing beats getting a quick estimation back from a couple of lines of memorised t-sql.

```
SELECT percent_complete pc,*
FROM sys.dm_exec_requests
order by pc desc
```

***My invitation*** to you for this month’s #tsql2sday is…

I would like you to share with the community what your go to script snippets are and why you find them useful. By sharing these, you will undoubtedly be helping someone who hasn’t thought of doing it that way, and hopefully you’ll pick up some handy hints as well.

- Any language is fine, not just t-sql
- Please share as many as you wish
- Perhaps you never do this and always work off saved scripts or convert your snippets to stored procedures? Tell us why this works for you.