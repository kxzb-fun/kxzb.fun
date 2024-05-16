---
title: "Linux系统CentOS7.9安装docker-compose"
date: "2023-08-01T02:30:23+0000"
tags: ['docker']
---

在 Linux 系统中，docker-compose 需要单独安装。 如果想要安装最新的版本，可以查看 GitHub 上的 docker-compose
仓库[发布页面](https://github.com/docker/compose/releases),并检查是否有新版本可下载。
本文写作时，使用的是最新版本 `2.20.2`

## 1\. 使用 curl 将 Compose 文件下载到/usr/local/bin 目录中

```bash
sudo curl -L "https://github.com/docker/compose/releases/download/2.20.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

## 2\. 使用 chmod 修改 docker-compose 文件可执行权限

```bash
sudo chmod +x /usr/local/bin/docker-compose
```

## 3\. 验证安装是否成功

```bash
docker-compose --version
```

## 4\. bash: docker-compose: 未找到命令

一般情况下是路径不在 PATH 中，需要在 `.bashrc` 中添加如下代码

```bash
export PATH=$PATH:/usr/local/bin
```

查看自己使用的默认 shell

```bash
echo $SHELL # /bin/bash
```

再次查看,问题得到解决
