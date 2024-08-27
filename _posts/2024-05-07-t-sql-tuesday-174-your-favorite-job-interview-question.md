---
id: 4655
title: 'T-SQL Tuesday #174: Your Favorite Job Interview Question'
date: '2024-05-07T16:27:28+00:00'
author: way0utwest
layout: post
permalink: '/174'
categories:
    - Invitations
tags:
    - '2024'
    - career
---

[Invitation ](https://36chambers.wordpress.com/2024/05/07/t-sql-tuesday-your-favorite-job-interview-question/)from [Kevin Feasel](https://36chambers.wordpress.com/).

## I’VE GOT A JOB FOR YOU

<figure class="wp-block-image">[![](https://36chambers.files.wordpress.com/2024/05/image.png?w=600)](https://36chambers.wordpress.com/?p=19613)</figure>If you’re reading this, there’s a pretty good chance you’ve been on a job interview before. You might even have received a job at some point!

Or maybe you’re on the other side of the hiring table: you’re searching for the best possible candidate for your company’s Paper Shuffler 3 opening (with a possibility of promotion within the next 5 years to Paper Shuffler 4).

Today’s question applies to both sets of people: interviewers and interviewees. The question is, **What is your favorite job interview question?** There’s a lot of latitude in how you answer this, and as a spoiler, that’s the type of question I like a lot.

## I HAVE A QUESTION, BY WHICH I MEAN I’M GOING TO STAND AT THE MICROPHONE FOR FIVE MINUTES AND RAMBLE ON ABOUT MY OWN PERSONAL INTERESTS TO THE EXCLUSION OF WHATEVER WE’RE ACTUALLY GATHERED HERE TO DISCUSS

Job interviews are a strange and awkward dance, where interviewers and interviewees are trying their best not to embarrass themselves too badly while simultaneously attempting to suss out whether there’s a mutual fit. Along the way, the interviewers tend to ask a bunch of questions, listen to the interviewees’ responses, make affirming noises on occasion, and quietly write down their lunch orders because they already know this person’s a hard pass but they feel like it would be rude to cut the interview short.

But what actually goes into these interview questions? Are you simply googling “DBA job interview questions” and asking people whatever pops up at the top of that list? Or maybe asking your favorite chat bot to do your job for you, like an even-more-dystopian version of Wall-E?

Hopefully not! Because this is your chance to shine, dear interviewer. And dear interviewee, as well: remember, you’re interviewing the company at the same time that their agents are interviewing you. You can **and should** have questions of the company and the job.

Now that I’ve given you the rough idea of the task at hand, I’ll share some of my favorite questions, both as interviewer and interviewee.

## A SET OF QUESTIONS

I’ll split this two ways, once as interviewer and once as interviewee.

### Interviewer

Because I struggle to come up with just one question in this section, I’ll give you a few. And it’s only happenstance that none of the questions in this section actually come in the form of a question.

#### TELL ME WHAT YOU SEE

As an interviewer, I love open questions, some of which don’t necessarily have correct answers. For example, here’s an idea I stole from Brent Ozar. I really like showing a picture to an interviewee and asking what they see, similar to a Rorschach test but hopefully with fewer psychological hang-ups. I’ll show a person a picture like the following:

<figure class="wp-block-image">[![](https://36chambers.files.wordpress.com/2024/05/interview-question.png?w=1024)](https://36chambers.files.wordpress.com/2024/05/interview-question.png)<figcaption>Clearly, this patient has Oedipal issues. I recommend he blind himself and go into exile.</figcaption></figure>While showing the image, I tell the interviewee something like, “I would like you to tell me what you see in the picture. There are no right or wrong answers, but I would like to hear what you find interesting about this.”

What’s important is, these pictures are simulations of real code and processes. This is a picture from Azure Data Studio that includes some T-SQL. If I’m hiring a person to be a T-SQL developer, I’ll want to hear about the code itself—with bonus points for telling me a horror story about the performance of `PERCENTILE_DISC()` or `PERCENTILE_CONT()` over large datasets and how you’ve had a great time working with `APPROX_PERCENTILE_CONT()` in SQL Server 2022—and recognition of the tool. This may spur on some further conversation. But what’s important is, I don’t necessarily have some set of right or wrong answers, such as “You must point out these six things on the image in order to pass.” For example, if the interviewee hasn’t used the `WITHIN GROUP` clause before, we might chat about that. Or maybe I’ll hear a story about using SQL Server ML Services and calculating five-number summaries in R instead. What I want to get out of this is your level of familiarity with the most important tools and code concepts that we’d expect a person to have based on our job description.

#### ASK YOURSELF A QUESTION

This question I stole from Sean McCown. It’s simple but powerful: “During this interview, we certainly didn’t cover everything there is to know about this field. What I’d like you to do is, ask yourself a technical question. Then, provide the answer to it.”

Sometimes, during an interview, a candidate has a rough time of it. You’re mentally ticking a lot of “wrong answer” boxes and ready to write this person off. But you could be missing something. Suppose the candidate is a replication savant, but you didn’t ask anything about replication at all during the interview. This gives the candidate a chance to talk about replication and gives you a chance to drill into the topic further. Even if your company doesn’t use replication at all and you still pass on the candidate, what this question can do is change the feeling of the interview from “How did this person possibly get past the screening?” to a more positive outcome. And there have been cases in which I’ve recommended a person for hire who didn’t do a great job in some of my questions but opened up an entirely new avenue of discussion with this question, where it helped me learn that the person was erudite but in a somewhat different field, and so we could pivot the line of questioning and even expectations for the position based on this.

From the interviewee side, there’s a bit of risk here. The candidate could, of course, ask something like, “What is 2+2?” and then provide the answer. That’s pretty weak. As an interviewer, I’ll take it as an answer, but it’s a red flag. On the other side, there’s risk from trying too hard to impress the interviewer, asking yourself a question whose answer you don’t actually know. If the interviewer does happen to know that answer and you get it wrong, that’s a self-inflicted oopsie.

#### TEACH ME SOMETHING

The final question I like to ask during an interview is, “Tell me something you have learned recently, with one caveat: it can be about anything **except** SQL Server \[or whatever the job entails\].”

I ask this for three reasons. First, I like to learn new things, and I have a <s>captive audience</s> candidate in front of me. Second, it’s a direct opportunity for the type of person who talks about “life-long” learning to walk the walk. Learning isn’t just about the job, so if learning is a passion, you’re (hopefully) picking up on things outside of your day-to-day job. Third, this gives even a junior-level interviewee an opportunity to explain a topic, allowing me to listen to this candidate’s ability to frame and explain an idea under some pressure.

Along the way, I’ve had discussions with candidates about the right way to load flatware in dishwashers, the best chicken noodle soup recipe, historical events, and characters in a then-recent anime. Did any of these questions or answers cause me to hire someone I wouldn’t otherwise have hired? No. But I will point out a correlation: 100% of the people I’d already planned to recommend for hire have had an answer to this question. Well under 100% of the people I’d already planned not to recommend for hire had an answer.

### Interviewee

As the interviewee, I want direct answers to some of the most important aspects of the job. The job description may say one thing, but what you get from interviewers may be a different story. Here are some of the types of questions I’m liable to ask at almost any job interview:

1. **What expectations do you have around hours per week worked?** For me, any number over 40 is a red flag, though your mileage may vary depending on industry and job.
2. **When is the last time people on your team worked overtime? What was the reason for that?** I’m trying to determine what the overtime demands are. Sometimes you do need to put in extra hours, but it’d better be temporary and for a good reason.
3. **Is there a budget for continuing education and training? If so, how much is available?**
4. **A train is heading eastbound from Lincoln, Nebraska at 68 miles per hour. Simultaneously, a train leaves a station in Chicago, heading west at 61 miles per hour. What is the nearest town (with a population of at least 5,000 people) from the point at which these two trains pass each other?** If the interviewers ask me dumb riddles about irrelevant topics they got from a Google search or job hiring book from the ’90s, I get to counter-ask similar questions.