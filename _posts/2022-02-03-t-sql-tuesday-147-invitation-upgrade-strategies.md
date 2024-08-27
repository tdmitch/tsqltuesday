---
id: 4368
title: 'T-SQL Tuesday #147 Invitation – Upgrade Strategies'
date: '2022-02-03T14:51:41+00:00'
author: way0utwest
layout: post
permalink: '/147'
categories:
    - Invitations
tags:
    - '2022'
    - administration
---

[Invitation ](https://voiceofthedba.com/2022/02/01/t-sql-tuesday-147-invitation-upgrade-strategies/) and [wrap-up](https://voiceofthedba.com/2022/02/24/t-sql-tuesday-147-wrap-up/) from [Steve Jones](https://voiceofthedba.com/)

## Planning for Upgrades

In my career, most of the time we don’t upgrade production databases very often. In most of my jobs, we’d change versions for new databases, but existing ones often lived on their original version. It’s how I got into a job where I was managing 4 different versions of SQL Server. These days I expect it’s common for many DBAs to have to deal with that many, or more, versions.

I do have customers these days that try to upgrade often, and limit the number of versions they work with. I have customers now that are on a mix of 2016-2019 only, some that might be working on 2014-2016 only, and I’ve run into a customer that only has SQL Server 2017. Of course, they have few databases and look to upgrade about every 5 years when mainstream support is running out for their edition.

This month I want you to write about how you look at SQL Server upgrades. A few things you might think about:

- Why we wait to upgrade?
- Strategies for testing an upgrade
- Smoke tests or other ways to verify the upgrade worked
- Moving to the cloud to avoid upgrades
- Using compatibility levels to upgrade an instance by not a database.
- Checklists of things to use in planning
- The time it takes to upgrade your environment
- What you evaluate in making a decision to upgrade or not?
- Anything else

I don’t know when SQL Server 2022 will release, but certainly many of us will need to consider in 2023 whether we want to upgrade systems or not. Think about it and write about something that matters to you.