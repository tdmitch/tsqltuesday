---
id: 4109
title: 'T-SQL Tuesday #125 –  Unit testing databases – we need to do this!!'
date: '2020-04-07T10:30:19+00:00'
author: way0utwest
layout: post
permalink: '/125'
categories:
    - Invitations
tags:
    - '2020'
    - testing
---

[Invitation ](https://hybriddbablog.com/2020/04/07/t-sql-tuesday-125-unit-testing-databases-we-need-to-do-this/) from [Hamish Watson](https://hybriddbablog.com/).

It’s an awesome way of encouraging blog posts from the community and helping to share that knowledge out.

My topic is about unit testing databases – something that I don’t see enough of when I am working with clients. The good news is that over the years I’ve noticed that more people are speaking and writing about unit testing databases and folding that testing into DevOps processes like Continuous Integration &amp; Continuous Delivery processes (CI/CD).

I hope that this topic drives some conversation both for it (because it protects your code and **data**…) and against it (it takes too long to write these pesky unit tests…!!).

### We’re now delivering Bugs to Production faster than ever!!

This clickbait type heading actually describes what will happen if you embrace DevOps processes without doing any form of testing. Because DevOps is all about accelerating the delivery of software – we want to do more deployments and do them quicker…

..which is why testing is core to DevOps practises. Specifically testing right throughout the deployment pipeline – that is starting at your laptop and finishing in Production (yes I advocate for testing in production but that’s a whole other blog post..).

### What is Unit Testing?

Unit testing is a software testing method by which individual units of source code are tested to determine whether they are fit for use. A unit is the smallest possible testable software component. A unit is small, so it is easier to design, execute, record, and analyse test results for than larger chunks of code are. Defects revealed by a unit test are easy to locate and relatively easy to repair.

This is opposed to finding the defect in Production – which is harder to triage and is now affecting users – whereas if you find that bug on your laptop via a unit test – it is way easier to remediate and only affects – you.

### The ideal qualities of unit tests:

Decisive – the unit test has all info to determine success/failure

Valid – it produces a result that matches the intention of the code written

Complete – it contains all information it needs to run correctly within the test harness

Repeatable – always gives the same results if the test harness and code are same

Isolated – is not affected by other tests run before nor affects the tests run after it

Automated – requires only a start signal in order to run to completion

### Benefits of Unit Testing

Below are the benefits of unit tests – this relates to application and databases alike.

#### Code Quality goes up:

Unit testing improves the quality of the code. It identifies every defect that may have come up before code is sent further for integration testing. Writing tests before actual coding makes you think harder about the problem. It exposes the edge cases and makes you write better code.

#### Find Issues early:

Issues are found at an early stage. Since unit testing is carried out by testing individual code before integration, issues can be found very early and can be resolved then and there without impacting the other pieces of the code.

#### Simplifies Integration

Unit testing allows us to refactor code or upgrade things at a later date and make sure everything still works correctly. Unit tests detect changes that may break things and help with maintaining and changing the code base.

The best part about unit testing is that it verifies the accuracy of the each unit of code. Afterward, when we integrate the code units together and run some form of integration testing during the build process we can then verify the individual units of code.

#### So what about databases?

So now that I have introduced unit testing – is it valuable for implementing with databases? Rather than write my own opinion – I’m going to hand it over to the community to answer this…

🙂

(BTW I think it is valuable – I speak on it regularly and I implement it with clients to safeguard their production databases…)

Lastly – we’re currently in a lockdown in New Zealand – because of the COVID-19 pandemic sweeping the world.

I want to say to all who are reading this:

Be Safe

Be Strong

and please:

Be Kind

If you’re struggling with things – please reach out to your support network (we care about you), I wrote some things that have been helping keep myself:

Take care – we’re in this together and you’re not alone  
\#sqlfamily

Yip.