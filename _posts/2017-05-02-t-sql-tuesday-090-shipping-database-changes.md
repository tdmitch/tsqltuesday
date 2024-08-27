---
id: 2881
title: 'T-SQL Tuesday #090 &#8211; Shipping Database Changes'
date: '2017-05-02T07:48:49+00:00'
author: way0utwest
layout: post
permalink: '/090'
categories:
    - Invitations
tags:
    - '2017'
    - 'database development'
---

[Invitation](http://thedatabaseavenger.com/2017/05/t-sql-tuesday-shipping-database-changes/) and [wrap up](http://thedatabaseavenger.com/2017/05/t-sql-tuesday-90-shipping-database-changes-wrap-up/) from James Anderson.

I was once asked to add a new feature to an application. It was installed on multiple SQL Server instances across multiple physical sites. The problem was that different instances of the application had different database schemas. New code may work on my local schema, but it could fail on the different schemas in live.

To develop the feature, I knew that I needed one universal version of the database schema.

I merged the schemas into a version that met the requirements of all environments and redeployed. Once in source control, this schema became the single source of truth that all future deployments were built from.

Not only did this solve my problem, it served as the foundation for the automation of builds, tests and deployments.

I’ve been interested in Continuous Integration and Database Lifecycle Management ever since. For more details, check my series of posts that start with [SQL Server &amp; Continuous Integration](http://thedatabaseavenger.com/2016/07/sql-server-and-continuous-integration/).

For this T-SQL Tuesday, I’d like to hear about your thoughts or experiences with database deployments.

Read the rules below and join in by publishing a short post about database deployments. If you develop or deploy database changes, I want to hear about it.

Your post can cover anything related to database deployments, but if you need inspiration, feel free to cover any of the topics below:

- What you’ve you seen work
- What you’ve seen fail. Be careful not to make any clients or employers look bad.
- [Database Lifecycle Management](https://www.simple-talk.com/sql/database-delivery/what-is-database-lifecycle-management-dlm/)
- [Continuous Integration](https://www.simple-talk.com/sql/database-delivery/database-continuous-integration/)
- Continuous Deployment
- Database builds
- Database unit tests
- The [migration or the state method](http://workingwithdevs.com/delivering-databases-migrations-vs-state/) for database deployments
- The tools you use