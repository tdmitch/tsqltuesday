---
layout: page
title: Migration Testing
permalink: /news/20240822-migrationtesting
---

I have been testing a migration of the T-SQL Tuesday site from Azure Websites to GitHub Pages. The repo is at [https://github.com/sqlsaturday/tsql2sdaytest](https://github.com/sqlsaturday/tsql2sdaytest), and this is a jekyll-based static site, which is suited for T-SQL Tuesday.

Please feel free to test the site at [https://sqlsaturday.github.io/tsql2sdaytest/](https://sqlsaturday.github.io/tsql2sdaytest/) to look for issues and problems.

## The Reasons
Microsoft Azure is deprecating the MySQL version I was using and causing me to pick a more expensive version. I decided a few months ago to not bother finding a different way to do this and instead migrate the site to GitHub pages. This makes it easier (For me) to manage, and it also allows me to move this under the SQL Saturday private foundation, which will be more community based and easier for me to transfer this to others to manage in the future.
