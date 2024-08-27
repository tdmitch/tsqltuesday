---
id: 4575
title: 'T-SQL Tuesday #166 &#8211; Why Not Extended Events?'
date: '2023-09-06T12:53:00+00:00'
author: way0utwest
layout: post
permalink: '/166'
categories:
    - Invitations
tags:
    - '2023'
    - administration
---

[Invitation](https://www.scarydba.com/2023/09/14/t-sql-tuesday-166-why-not-extended-events/) from [Grant Fritchey](https://www.scarydba.com/).

With 165 T-SQL Tuesday events, two, just two, this one, [T-SQL Tuesday #166](https://www.scarydba.com/2023/09/11/t-sql-tuesday-166-extended-events/), and another one back in 2018 or 2019 (I forget and I’m far too lazy to go look) have been on Extended Events.

At conferences I’m frequently the only one doing sessions on Extended Events (although, sometimes, Erin Stellato is there, presenting a better session than mine). I did a session at [SQL Konferenz](https://sqlkonferenz.de/) in Germany earlier this week on Extended Events. Hanging out in the hallway at the event (which was great by the way), I was talking with some consultants. Here’s their paraphrased (probably badly) story:

“I was working with an organization just a few weeks back. They found that Trace was truncating the text on some queries they were trying to track. I asked them if they had tried using Extended Events. They responded: What’s that? After explaining it to them, they went away for an hour or so and came back to me saying that had fixed the problem.”

We all smiled and chuckled. But then it struck me. This wasn’t a case of someone who simply had a lot more experience and understanding of Profiler/Trace, so they preferred to use it. They had literally never heard of Extended Events.

Why?

## Search Engines

I did a search on [Bing](https://www.bing.com/search?q=%22sql+server%22+identify+slow+queries&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=%22sql+server%22+identify+slow+queries&sc=11-34&sk=&cvid=01AC3568D70848968D25074D1083DDCD&ghsh=0&ghacc=0&ghpl=), [Google](https://www.google.com/search?q=%22sql+server%22+identify+slow+queries&sca_esv=565286027&sxsrf=AM9HkKmpj2jtM3BW142TEOc8boCkfeXfVw%3A1694680333238&source=hp&ei=DcUCZcKIDIyKgAakj6eACA&iflsig=AO6bgOgAAAAAZQLTHYuhlcgwmXuBuwj0E0loPV2T84M3&ved=0ahUKEwiCw5Ka2KmBAxUMBcAKHaTHCYAQ4dUDCAs&uact=5&oq=%22sql+server%22+identify+slow+queries&gs_lp=Egdnd3Mtd2l6IiIic3FsIHNlcnZlciIgaWRlbnRpZnkgc2xvdyBxdWVyaWVzMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMggQABiKBRiGA0jWCFAAWABwAHgAkAEAmAFloAFlqgEDMC4xuAEDyAEA-AEC-AEB&sclient=gws-wiz#ip=1) and [DuckDuckGo](https://duckduckgo.com/?t=h_&q=%22sql+server%22+identify+slow+queries&ia=web). The results were instructive.

The top result on Bing was to a 14 year old StackOverFlow post. To say the least, yeah, it’s not showing anyone how to use Extended Events. It talks about DMVs in addition to Trace/Profiler.

The top result in Google was a site I’ve never even heard of before, Sit24x7.com. It talked about DMVs, and nothing else. I couldn’t find a publish date on the article, but since it didn’t talk about sys.dm\_exec\_procedure\_stats, but only talked about query\_stats, either the person writing it was ignorant of more recent DMVs (and, let’s be clear, saying that procedure\_stats is recent is s stretch), or this is a very old article indeed.

The top result in DuckDuckGo was a post on SQLShack written in 2017 using examples from SQL Server 2016. The tools used were, kind of oddly, Activity Monitor within SSMS and Query Store. No mention of Profiler/Trace, Extended Events, or even DMVs. The second result was the 14 year old Stack overflow post.

If you were looking to identify a long running query, you might be lead to believe the consensus is that the only tool to use is DMVs.

## The Whole First Page

The common wisdom is that people never go beyond the first page of search results (I’ve no idea if this is true). So, what’s on the first page?

Well, Bing had eleven results that weren’t ads when I ran the query linked above. It wasn’t until links 7 and 8 that Extended Events are mentioned. Further, links 7 &amp; 8 were the same article, just published in two different places with a few edits between them. Four of the links were to Microsoft and NONE (zero, 0, zip, nicht) of those mentioned Extended Events, although they did talk about DMVs. Of the top 10, most of the links were old. Many 10 years or more. The two links, 7 &amp; 8, were the only ones to mention Extended Events.

With Google I saw 10 non-sponsored links on the first page. Many of them were duplicates of the links in Bing, just in a different order. Link 4 was to the same article I found in Bing. Link 5 was to a new source that did had Extended Events as the #1 tool for gathering query performance metrics. There was only one Microsoft link, duplicated from Bing, and it didn’t list Extended Events. Just like with Bing, most of the links were old. Many of the links from Google were older than the ones from Bing.

DuckDuckGo was just a little better. The 3rd and 4th slots had two different articles talking about Extended Events with the 3rd slot being the same article from both Bing and Google and the 4th slot being a new one. Three of the slots were Microsoft and again, no mention of Extended Events. And, once more, many of the links are minimum 7 or 8 years old, but some being 13 or 14 years old.

## Conclusion

We can have a lot of discussion about the technical aspects of Extended Events. We can also talk about whether or not you should, or shouldn’t use Extended Events. The simple fact of the matter is, there’s a good chance that people aren’t using Extended Events, not because they’re problematic, hard, contain XML, muscle memory, or any of the other issues that I, and others, bring up, but instead, because they simply don’t know that they exist.

So, if you are #TeamXE, not only do we have to overcome years of bad information and indifference due to a poor launch (2008 XE just wasn’t good, let’s be honest), but the fact that the way search engines work, Extended Events may be hidden from many people.