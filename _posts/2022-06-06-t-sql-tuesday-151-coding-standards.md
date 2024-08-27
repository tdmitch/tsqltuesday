---
id: 4407
title: 'T-SQL Tuesday #151 &#8211; Coding Standards'
date: '2022-06-06T08:35:09+00:00'
author: way0utwest
layout: post
permalink: '/151'
categories:
    - Invitations
tags:
    - '2022'
    - t-sql
---

[Invitation](https://curiousaboutdata.com/2022/06/06/t-sql-tuesday-151-invite-t-sql-coding-standards/) and [roundup](https://curiousaboutdata.com/2022/06/17/t-sql-tuesday-151-round-up-coding-standards/) from Mala Mahadevan.

My invite is about coding standards, or what I now call Linting Rules, for T-SQL. **What are the T-SQL coding rules that are appropriate for where you work and what you do? If there are exceptions to those rules, state them too!** If this is enough, read the blog party rules below and get started!!

- Your post must be published on Tuesday June 14, 2022.
- Your post must contain the T-SQL Tuesday logo (see above) and the image must link back to this blog post.
- Trackbacks should work, but if not please put a link to your post in the comments section so everyone can see your contribution! (My comments are moderated so please don’t worry if yours doesn’t appear right away, I will make sure it does!)
- If you are on twitter include the hash tag #tsql2sday – it helps with RT-s and visibility!!

More on why I picked this topic as below –

When I started out as a DBA two decades ago, I had a list of rules that I would carry with me into every job I went..these are things I look for in T-SQL code and try to enforce as standard. Some examples were casing rules, minimized usage of SELECT STAR, equating the right data types in columns, avoiding NOLOCK hint and so on. Standards ensure quality and consistency in code.

Standards differ for each firm, depending on what is appropriate for an environment..it is even possible to have varying standards in the same company, depending on the environment and what is appropriate for a database. [This](https://www.red-gate.com/simple-talk/databases/sql-server/t-sql-programming-sql-server/basics-good-t-sql-coding-style/) is an excellent article on what are the different components that comprise coding standards, and why we need them. I am also a big proponent of automated code checking for standards – there are lots of tools available for doing this – [SQL Prompt](https://www.red-gate.com/products/sql-development/sql-prompt/), which is a personal favorite of mine, and many others as listed [here](https://analysis-tools.dev/tag/sql).

Several tools currently do linting on many relational platforms, not just SQL Server. Almost all of them though, have rules that the author(s) think are best for the worlds they work in, and do not include other conditions which they have not encountered yet. A common example I like to use is unnamed primary keys on temporary tables. There is nothing inherently wrong with having an inline primary key constraint/index on a temporary table – but if you use Query Store, plan forcing on a plan that uses this temp table will not work simply because the constraint gets named differently each time. When I started to look for a linting tool for where I work – I ran into so many rules that were non-existent or not applicable to my environment with outside tools that I decided to write my own using [ScriptDOM](https://www.sqlservercentral.com/steps/stairway-to-scriptdom-level-1-an-introduction-to-scriptdom) – a Microsoft-provided library that was created specifically for this purpose.  
  
It would help greatly if we had a collection of rules that people use to pick from and enforce as appropriate for their environments. It will also help me to code some of these into ScriptDOM and put it out on GitHub, if the rule is one that ScriptDOM can find easily. So, re-stating the call for this month – **What are the T-SQL coding rules that are appropriate for where you work and what you do? If there are exceptions to those rules, state them too!**