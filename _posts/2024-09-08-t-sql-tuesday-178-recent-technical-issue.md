---
id: 4676
title: 'T-SQL Tuesday #178: A Recent Technical Issue You Resolved'
date: '2024-09-03T00:02:00+00:00'
author: way0utwest
layout: post
permalink: '/178'
categories:
    - Invitations
tags:
    - '2024'
    - 'database development'
    - 'database administration'
---

[Invitation ](https://dbanuggets.com/2024/09/03/t-sql-tuesday-178-invitation-recent-technical-challenge-you-resolved/) from [Deepthi Goguri](https://dbanuggets.com/)

Have you had any recent technological problems at work that you were able to fix? You might have tried very hard for days to figure out the answer to the technical issue you faced, but it turns out that a minor modification you made may have resolved the issue. Alternatively, the error message you see might be completely different from the solution you adopted to resolve the issue. Please blog for me about any problem, no matter how big or minor, that you may have encountered lately. I’d like to see all kinds of issues you’ve faced and how you fixed them.

I’ll share my latest experience here.

The DEV and UAT migrations for the SSRS migration project I was working on recently went well, but when we opened the webpage URL, we noticed the following HTTP address problem. ReportServer services servers and databases are housed on separate servers. The servers were set up correctly, the SSRS service delegation was established, and the Report Server service accounts had the appropriate rights to the Report Server databases. Days passed before I was able to work with the Server team member to resolve the problem—that is, we missed creating an SPN for the Report Service server using the Server name. The problem was fixed by adding the SPN made for the service using HTTP and the Servername. We also had to change the authentication configuration file to RSWindowsNegotiate instead of RSWindowsNTLM.

Until this problem was resolved, we had seen weird errors from an application running the reports, testing the data sources showed the login failure error message – “Login failed for user ‘NT AUTHORITY\ANONYMOUS LOGON'”.

This article really helped us pinpoint the [issue](https://redmondmag.com/Articles/2010/08/23/Reporting-Services-Double-Hop-Authentication.aspx).