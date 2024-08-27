---
id: 4004
title: 'T-SQL Tuesday #117 &#8211; When Have You Used MOT Tables?'
date: '2019-08-08T08:27:43+00:00'
author: way0utwest
layout: post
permalink: '/117'
categories:
    - Invitations
tags:
    - '2019'
    - 'In-Memory OLTP'
---

[Invitation ](http://voiceofthedba.com/2019/08/08/t-sql-tuesday-117-invitation-when-have-you-used-mot-tables/)and [roundup](https://voiceofthedba.wordpress.com/?p=17894&preview=true) from Steve Jones.

When [Memory-Optimized Tables](https://docs.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/overview-and-usage-scenarios?view=sql-server-2017) (MOT) were [announced for SQL Server](https://www.red-gate.com/simple-talk/sql/database-administration/hekaton-in-1000-words/), there was a lot of excitement about the technology. After this was released on SQL Server 2014, feelings waned with a lot of restrictions and limitations for using the technology. I remember a panel at a conference years ago where most of the MVPs and experts recommended against using the technology for most users.

Today there have been improvements ([2017](https://docs.microsoft.com/en-us/sql/sql-server/what-s-new-in-sql-server-2017?view=sql-server-2017), [2016](https://docs.microsoft.com/en-us/sql/sql-server/what-s-new-in-sql-server-2016?view=sql-server-2017)) in the MOT features, restrictions have been removed, and all editions can use MOT tables. That’s not to say that this is suitable for every table or situation where a DBA or developer suspects performance issues.

This month I want to ask you about when you’ve made that decision. This can be *to use* MOT tables or *NOT to use* MOT tables. This could be a simple thought, a POC, or actual testing of the feature.

Some ideas for you to write about:

- Performance analysis of MOT tables that affected a decision
- Reading the limitations and knowing this would prevent their use
- A scenario where MOT tables improved performance
- A successful implementation of MOT tables and what needed to change in your app
- A failed attempt at trying MOT tables

There might be other things that are related to MOT technology, but let us know this month what you think of the technology and how it has (or has not) impacted your application.