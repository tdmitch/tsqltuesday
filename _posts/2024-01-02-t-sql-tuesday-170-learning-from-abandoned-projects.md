---
id: 4613
title: 'T-SQL Tuesday #170 – Learning from Abandoned Projects'
date: '2024-01-02T13:41:23+00:00'
author: way0utwest
layout: post
permalink: '/170'
categories:
    - Invitations
tags:
    - '2024'
---

[Invitation](https://sqlreitse.com/2024/01/02/t-sql-tuesday-170-invite-learning-from-abandoned-projects/) and [write up](https://sqlreitse.com/2024/01/13/t-sql-tuesday-170-write-up-learning-from-abandoned-projects/) from [Reitse Eskens](https://sqlreitse.com/)

appy new year to all of you avid bloggers! I hope most of you had a great time during the past weeks, though most of you have seen the sad news of the loss of an excellent member of the Sql Family. Let’s keep Leila in our minds and send strength to Reza.

I was having a nice chat with Steve last year on possible subjects for this [fun monthly blog event.](http://tsqltuesday.com/) And my initial inspiration was “what have you learned from abandoned SQL projects”. Yes, let’s kick off the year on a happy subject, talk about failures.  
But wait, you should look on this one in a positive way, like Buck Woody ([T](https://twitter.com/BuckWoodyMSFT)) does

<figure class="wp-block-image">![](https://sqlreitsehome.files.wordpress.com/2024/01/afbeelding.png?w=953)</figure>We all learn by doing stuff, but we learn most by ‘failing’, working on things that are less than optimal. If you have the time to look back on projects, to review them, you usually see where things went wrong. I think that most of us have been in projects like that and have learned from that.

Let me give you an example. A few years ago we started a project where we had to use an Azure Sql database as the target database. Sources were on-premises and with some magic wizardry, the data landed in the Azure database. But the performance was less than expected. Because deadlines we had to rush through a number of options and ended up with a database we had to reconfigure a number of times after the project finished. When we did the review, this was a bit of a sore point because I felt (and feel) responsible for this part.  
During the review, I decided to dig into the different tiers and sku’s of Azure Sql databases and find out their differences in behaviour. This lead to a series of blog posts (that have to be revised as a lot of things changed since writing them). But the key is, I can now give a better advice and reduce the number of reconfigurations.

Now, I could go on, but the main intent of this blog is to trigger your stories; what projects did you abandon but learn a lot from OR what’s your favourite learning from a failure.

As it’s january, I’ll give you some slack on the subject and how much you digress.