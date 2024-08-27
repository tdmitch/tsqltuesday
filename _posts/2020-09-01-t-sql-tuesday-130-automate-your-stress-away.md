---
id: 4160
title: 'T-SQL Tuesday #130 – Automate Your Stress Away'
date: '2020-09-01T09:18:21+00:00'
author: way0utwest
layout: post
permalink: '/130'
categories:
    - Invitations
tags:
    - '2020'
    - Automation
    - DevOps
---

[Invitation](https://sqlzelda.wordpress.com/2020/09/01/t-sql-tuesday-130-automate-your-stress-away/) and [recap](https://sqlzelda.wordpress.com/2020/09/21/t-sql-tuesday-130-recap-automate-your-stress-away/) from [Elizabeth Noble](https://sqlzelda.wordpress.com/).

Life as a data professional is stressful. This year is even more stressful. We have so many responsibilities and so may demands coming at us every day. I’ve found over the years that I love the stress, but I also want to make my life and the lives of those around me easier, calmer, more peaceful. I can’t change everything about my job or what is expected of me. After a particularly stressful summer many years ago, I wanted to figure I could change in my day to day tasks. How could I make my life easier?

At the time, the largest hurdle I had was around deployments. Our deployments consisted of a collection of SQL scripts collected from individual user stories. Each script was executed separately as we didn’t have a good process for what to do if any particular script did fail. In addition, we created rollbacks for each script that was deployed. The process worked for us for quite some time until one day we deployed our first new application in years.

Eventually, we moved a handful of our databases to source control. That part was easy as you can use Visual Studio and SQL Server Data Tools (SSDT) to import a schema for an existing database. The next steps took quite a bit of communication between the teams. A few missteps later, we had 2 of our 10 or so databases deploying through Continuous Integration Continuous Delivery (CICD) pipeline. We still deploy once every two weeks, but our deployments our generally quicker and less tedious.

The time savings is nice. We have about 24-26 deployments a year, and we easily save at least an hour on average per deployment. That’s a full day a year! But the best part for me is the next day. I still check my email as soon as I wake up to ensure that aren’t any issues reported, but even if there are issues, they are usually quickly resolved and we go on about our day.

My invitation to you is I want to know what you have automated to make your life easier? This can be anything creating a SQL Server Agent job to automated running a daily report or using dbatools to manage your servers. I’m curious what challenges you’ve found at your job and what you’ve done to make things better. If you haven’t had a chance to automate some part of your job, what would you like to automate and what are your hurdles? If you’re interested in some help or advice, let us know. I love #SqlFamily, and I’d love to see what we can do to help out.