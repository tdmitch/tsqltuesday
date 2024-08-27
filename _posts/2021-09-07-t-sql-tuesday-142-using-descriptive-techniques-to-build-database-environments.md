---
id: 4320
title: 'T-SQL Tuesday #142: Using descriptive techniques to build database environments'
date: '2021-09-07T09:37:00+00:00'
author: way0utwest
layout: post
permalink: '/142'
categories:
    - Invitations
tags:
    - '2021'
    - administration
    - Azure
    - cloud
---

[Invitation](https://gds-business-intelligence.de/2021/09/06/invitation-for-t-sql-tuesday-142-using-descriptive-techniques-to-build-database-environments/) from [Frank Geisler](https://gds-business-intelligence.de/category/sql-server/).

In the old glory days back then it was usual that you must deal with one or two or probably three SQL Servers. As you all know these times are over. Through the rise of the cloud, every one of us must deal with more and more systems, not only Infrastructure but also Platform as a Service (PaaS) offerings. The systems themselves are getting more complex through all the new services and technologies that are involved and somehow interconnected. New movements like Azure Arc enabled Data Services bring a whole new aspect to the table where you can easily choose weather to run your data workload on your on-premises Kubernetes Cluster or in the cloud.

All these systems can easily be built with the Azure Portal, but this is not sustainable. Each time you use the portal, you must remember how to build a certain system and – and that is more important – how to apply best practices. For sure you can build e.g., an Azure SQL Database with an open endpoint into the internet and secure this by Firewall settings but this should be done with much caution because you are exposing your database to the internet. A better approach would be to build an Azure SQL Database that does not have a public endpoint but a private endpoint to an Azure V-Net which hosts the systems that must access the database, or which is connected to a local Network via VPN Gateway. As you can imagine there are a lot of moving parts to get such an environment up and running and you must remember (or document) each of these. This is very cumbersome work. There must be a better solution and for sure there is one: Scripting.

When you write a script, you are making your work once and whenever there is the same or a similar situation e.g., deploy an Azure SQL Database best practice, you can just pull out your script and there you go. This can be even taken to another level when you have a parametrization for your script that allows to just put in the parameters and let the script do the rest. Using this as a mantra I developed several scripts to build different cloud environments in PowerShell. This has the big advantage that the environment is documented as you have a script, and that the environment is versioned as well because all our scripts are saved within a source control system. The overall approach is called Infrastructure as Code ([https://en.wikipedia.org/wiki/Infrastructure\_as\_code](https://en.wikipedia.org/wiki/Infrastructure_as_code)).

But doing imperative scripting in PowerShell also has its shortcomings. The cloud and the internet in general, is a very uncertain environment. While running the script that deploys your environment many things can happen. Your internet connection can break down, there could be an error deploying your script for whatever reason and so many other things you can think of. So you have to build many conditions in your script: If the resource group exists skip that and just build the Azure SQL Database if the V-Net exists skip that, check if all needed subnets exist and so on. Right? Wrong! Besides the imperative way of telling the Azure Resource Manager what to do you can also use a declarative approach to build resources in Azure.

This declarative approach is very common to everyone who has ever written T-SQL Code. If you write e.g., a query that selects data, you don’t instruct the database system how to retrieve the data from the underlying file structure. You only tell the system how the data you are looking for should look like: Select all the rows of data where the first name is “Frank”. This is the exact same approach that techniques like ARM-Templates, Bicep-Templates or if we are talking about Kubernetes YAML-Scripts take. The scripts are a description of how the target environment should look like. How this target environment is reached is fully up to the underlying System like the Azure Resource Manager. And there is even more: If you are changing an existent environment, only the parts that changed in the script will be altered in the target environment. Say you have an Azure SQL Database of a certain size and you change the size in your Bicep script. Next time you deploy the script the Azure SQL Database will be resized without deleting and redeploying it.

The ideal process of working with Infrastructure as Code would be that the code is checked in to Azure DevOps and that an automatic process will then deploy the changes to your target environment. To change your environment or to add resources you will only have to write the needed changes into your bicep scripts, check them in and let Azure do the magic.

**My invitation to you for this month’s #tsql2sday is:**

This is my invitation to you this T-SQL Tuesday to think about deploying SQL Component through descriptive Methods and of course to blog about it. It does not matter if you are using Azure and ARM-Templates or Bicep or Kubernetes and YAML. Just write about it and build some new cool Templates that implement some of your best practices infrastructure / environment wise. Or you can write an article on where you have already used descriptive scripts to build environments.

As always there is a whole lot of stuff on the internet you can use as a starting point. I summarize a little bit here:

- <https://docs.microsoft.com/en-us/learn/paths/bicep-deploy/>
- <https://docs.microsoft.com/en-us/learn/paths/bicep-collaborate/>
- <https://docs.microsoft.com/en-us/azure/templates/microsoft.sql/servers?tabs=bicep>
- <https://docs.microsoft.com/en-us/azure/templates/microsoft.sql/managedinstances?tabs=bicep>
- <https://github.com/Azure/bicep>