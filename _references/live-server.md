---
week: 6
title: Install the VSCode live server extension
---

Using VSCode for web development is great.
However, loading local files into the browser is subtly different from loading content over HTTP.

If you want to see how your content would work if it were on a web server, then you can use the [live server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) extension.

This plugin enables a *go live* button which runs a local web server configured to deliver your project.
This provides you with a more realistic result, but also automatically updates your browser whenever you save your files.
This means you can work more smoothly by editing code and viewing the results directly without needing to return to the browser and refresh the page.

## Installation

There are many ways to install the extension.
One of the simplest is to select the extensions icon on the left panel and search for *"live server"*.
You should see the correct extension at the top of the list, it has over 30 million downloads at the time I wrote this. 

![installing live server]({{ "assets/img/week_6/live-server.png" | relative_url }})

> Notice that I already have it installed, so I don't have an *install* button for live server.

Simply click on the *install* button and it should automatically install the extension.
Once it is complete you will have the option to turn on the server by clicking the *go live* button in the bottom panel.

![the go live button]({{ "assets/img/week_6/go-live.png" | relative_url }})
