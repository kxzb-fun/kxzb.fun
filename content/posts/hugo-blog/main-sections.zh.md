---
title: "hugo 搭建博客修改最近文章内容"
date: 2024-06-04T21:11:22+08:00
draft: false
showSummary: false
description: "本文介绍hugo + congo 主题搭建的博客如何修改最近文章展示内容是什么"
tags: ["技术"]
categories: ["blog"]
keywords:
  - "hugo博客"
  - "congo 主题"
---

本文使用hugo + congo 主题搭建，今天刚意识到主页的最近文章展示的日记列表内容。之前认为是时间格式的问题导致的，查阅了[congo的文档](https://jpanther.github.io/congo/docs/homepage-layout/#recent-articles)才改正。

需要修改 `config/_default/languages.zh.toml` 文件下的 mainSections 属性

```toml
[params]
  mainSections = ["posts"]
```

如果是多语言，则一同修改即可。
