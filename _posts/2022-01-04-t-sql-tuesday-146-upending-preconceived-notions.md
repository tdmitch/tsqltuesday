---
id: 4352
title: 'T-SQL Tuesday #146: Upending Preconceived Notions'
date: '2022-01-04T09:15:08+00:00'
author: way0utwest
layout: post
permalink: '/146'
categories:
    - Invitations
tags:
    - '2022'
    - 'career improvement'
---

[Invitation ](https://sqlbek.wordpress.com/2022/01/04/t-sql-tuesday-146-upending-preconceived-notions/)and [round-up](https://sqlbek.wordpress.com/2022/01/24/t-sql-tuesday-146-round-up-upending-preconceived-notions/) from [Andy Yun](https://sqlbek.wordpress.com/).

Welcome back to another edition of T-SQL Tuesday! I’m honored to be your host once again!

## Theme to Kick off 2022

This month, I’d like to ask everyone to think about something you’ve learned, that subsequently changed your opinion/viewpoint/etc. on something. Maybe you’ve had a certain opinion, belief, or bias? Perhaps you’ve always thought something worked a certain way? Or you’ve always thought that a certain something (called “X”) was only good for “A”, only to later learn that it can help with “B”, and “C” as well. Regardless, you learned something and it totally upended and changed that preconceived notion you held previously.

## When has this happened to you Andy?

Let me share an example. In my past as a T-SQL developer, I remember when I first learned about CTEs. I thought the world of them and started using them everywhere! However, there was one slight problem. I was under the mistaken impression that they pre-materialize each sub-query. And they do… in OTHER RDBMS’s. Whoops! After a few years, I learned that they don’t behave that way in SQL Server. Instead the query optimizer inlines the query in the CTE, making them functionally no different that a subquery. And well, let’s just say that that made me regret some of the coding decisions I’d made during my “CTEs-are-awesome” phase.