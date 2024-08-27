---
id: 4209
title: 'T-SQL Tuesday #133: What (Else) Have You Learned from Presenting?'
date: '2020-12-01T11:35:27+00:00'
author: way0utwest
layout: post
permalink: '/133'
categories:
    - Invitations
tags:
    - '2020'
    - 'career improvement'
---

[Invitation ](https://lisagb.info/archives/77)and [wrap-up](https://lisagb.info/archives/80) from [Lisa Griffin Bohm](https://lisagb.info/).

This month, I’d like those of you who have presented, or written a presentation, to share something technical THAT DID NOT RELATE to the topic of the presentation, that you’ve learned in writing or giving the presentation. This can include a work presentation, for those of you who haven’t spoken at an event!

Why do I ask? Well, if any of you have heard Allen White ([b](http://blog.allenmwhite.com/)|[t](https://twitter.com/sqlrunr?lang=en)) speak on any topic, he will start his presentation speaking about how much PASS has contributed to his life and career. He will then talk about how every person has a story to share, and there will be a piece of that story that no one has ever heard before. We ALL have something to learn from each other. He will also tell you that you will learn more than you ever thought just by writing and presenting on ANY topic, as well as answering questions! So, I’d like folks who have done this to share and encourage – especially the new folks who are on the fence about presenting. Feel free to go more in-depth with some of the technical details of your learning than I did!

I will share a couple of stories about my own experiences. My first presentation at our local PASS user group was a lightning talk about a bizarre performance hit we took from a foreign key with an ON DELETE CASCADE option. It was a rare scenario, so I figured most folks hadn’t run into this.

As I was researching foreign keys in general, I realized… hey! Did you know there were other options for updating and deleting data tied to foreign key constraints? I don’t know that I’ve paid attention to that for the last… at least 10 years. I’ve never seen any of these options used in code I’ve maintained or identified as problematic. You can specify default behaviors for both delete and update options – for example, if I update the value that the foreign key constraint points to, I can change all those foreign key values to be NULL. Or to update that foreign key value to the new value. Or… not do anything. There are ramifications for all of the choices, but I could definitely see how they might be useful in certain scenarios.

Also, people were interested enough in the topic to ask about indexing on some of the different fields, and asked me to expand this into a full presentation. I did so and presented at our next local SQL Saturday, including testing with the indexes that were recommended to me.

**Learning summary:**

1. tables may show up in the execution plan even if they weren’t in the query AT ALL (look for constraints!)
2. there are other options for coding foreign keys to handle updates/deletes to the primary key data that could be useful elsewhere
3. Reinforcement: Indexes with low cardinality don’t always improve performance!

I also wrote a book on refactoring legacy T-SQL. I was talking about functions, and how SQL Server’s STATISTICS IO won’t show IO that a function performs. I remember thinking, “I CANNOT write a book in 2019 that talks about running a trace!” So, I started using simple Extended Events to show the increased IO for functions that the native SQL Server STATISTICS IO sneakily avoids. I need to start making more use of Extended Events but this was a great .. kick in the pants to get going on those, as well as being able to code a very simple, more modern solution to share with readers on how to more accurately find IO stats of the SQL you’re running/tuning!

I could continue about buying a “lab” laptop, re-learning how to use Oracle Virtualbox, dealing with networking (not one of my strengths), using SQL Server core (sooo fast to install!), and all of those fun things. But, there will be future blog posts on those topics, and it’s time for others to share THEIR stories and experiences! Thanks for reading!