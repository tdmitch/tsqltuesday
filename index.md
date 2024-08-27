---
layout: home
title: "T-SQL Tuesday"
---

## The Current Invitation

The current invitation (August 2024) is for T-SQL Tuesday #177. The next invitation should be released on September 3.

## T-SQL Tuesday #177: Managing database code
[Invitation](https://curiousaboutdata.com/2024/08/07/t-sql-tuesday-177-managing-database-code/) and [recap](https://curiousaboutdata.com/2024/08/18/t-sql-tuesday-177-roundup-managing-database-code/) from [Mala Mahadevan](https://curiousaboutdata.com/)

I am excited to host the T-SQL Tuesday blog party for August 2024. I’ve done this many times, but I always remember when I was new to the community and how much it helped me gain recognition. Thanks to Adam Machanic for starting this initiative and to Steve Jones for keeping it going.

This month’s topic is ‘Managing Database Code’. I initially called it ‘How do you manage your database repo?’, but Steve pointed out that many people in the database community might not know what a ‘repo’ is. So, we simplified it to ‘Managing Database Code’. Managing code has been a big part of my work as a database engineer for the past six years.

A repo, for those who are not aware, is just short for [‘repository‘](https://www.merriam-webster.com/dictionary/repository), a place to store stuff. In this context, a place where ‘keep’ code. It is version control for code. I remember the days before repos were common. We used tools like VSS/TFS and searched through tickets and comments to track changes. We used DMV-based queries to find objects. Now, with repos, everything is much easier. I can’t imagine working without one.

I’m curious about how others manage their database code. Here are some questions to consider:

Where do you keep your database code? Is it in a GIT-based repo, or just in the database the old-fashioned way?
If it is in a repo, how is it created? Do you script out individual scripts and add them, or do you use tools to script out the entire database, like SSMS scripter, SMO-based scripts, or third-party tools? This could apply to any relational database, not just SQL Server.
How do you keep your repo up to date when code changes? Depending on what your shop does, you may or may not have a well evolved [CI/CD pipeline](https://about.gitlab.com/topics/ci-cd/). If you do, explain how it works. If you don’t, that’s fine – we just want to know where the code resides, if it is outside the database.
If you don’t have a repo, why not? How do you manage things like searching code or finding who made changes and when?
I look forward to reading your responses. 