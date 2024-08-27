---
id: 971
title: 'T-SQL Tuesday #006: &#8220;What About BLOB?&#8221;'
date: '2010-05-03T20:45:52+00:00'
author: way0utwest
layout: post
permalink: '/006'
categories:
    - Uncategorized
tags:
    - '2010'
    - BLOB
---

[Invitation](http://sqlblog.com/blogs/michael_coles/archive/2010/05/03/t-sql-tuesday-006-what-about-blob.aspx) and [roundup](http://sqlblog.com/blogs/michael_coles/archive/2010/05/13/t-sql-tuesday-006-round-up.aspx) from [Michael Coles](http://sqlblog.com/blogs/michael_coles/default.aspx).

[MSDN](http://msdn.microsoft.com/en-us/library/a1904w6t%28VS.80%29.aspx) conveniently defines Large Object (“LOB”) data types for us: “*LOB data types are those that exceed the maximum row size of 8 kilobytes (KB).”*

There have been a several improvements in LOB data functionality in SQL Server 2008 (there were even some in SQL Server 2005). In 2008 the XML, GEOMETRY, GEOGRAPHY data types can all hold 2.1 GB of data. CLR data types can also hold up to 2.1 GB of data. So the question of the day is how do you use LOB data? Here are a few possible starting points:

- LOB data storage, optimization, limitations, “under-the-hood”
- Indexing, querying, optimization, tricks, tips, performance tuning of LOB data
- Interesting uses/projects for LOB data types: 
    - The MAX data types (VARCHAR(MAX), NVARCHAR(MAX), VARBINARY(MAX))
    - XML
    - GEOMETRY/GEOGRAPHY (spatial)
    - CLR data types
- FILESTREAM hints, tips, tricks, .NET SqlFileStream Class

The only rule is that your topic has to involve SQL Server’s LOB data types in some form. If you want to demonstrate handling LOB data in .NET, for instance, go for it. If you want to demonstrate Oracle LOB data handling, this might not be the place to do it (although a comparison of the two might be interesting…) 🙂