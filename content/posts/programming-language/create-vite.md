---
title: "关于npm create 和 Vite"
date: 2024-06-04T20:52:53+08:00
draft: false
showSummary: false
description: "本文主要梳理了 `npm create` 的功能，对比了 `create-react-app` 和 `create-vite` 的区别，并简单的实现了一个 `create-myvite` 的库学习创建逻辑。"
tags: ["技术", "Learn"]
categories: ["技术"]
keywords:
  - "npm create"
  - "create-vite"
  - "手写vite"
  - "create-react-app和create-vite对比"
---
本文主要梳理了 `npm create` 的功能，对比了 `create-react-app` 和 `create-vite` 的区别，并简单的实现了一个 `create-myvite` 的库学习创建逻辑。

## 从npm create 说起

`npm create`是npm命令的一部分，用于通过npm运行特定的脚本或包来创建新的项目。它简化了创建项目的过程，特别是当你需要基于某个模板或特定工具来初始化项目时。

比如我们执行：

```shell
npm create xxx
```

1. **`npm create`**:
    - `npm`是Node Package Manager的缩写，用于管理JavaScript包。
    - `create`是一个关键字，表示你要运行一个创建项目的脚本。
2. **`xxx`**:
    - `xxx`表示你要使用的创建器包的名称。这可以是`vite`，也可以是其他任何支持`npm create`命令的创建器包。

当你运行`npm create xxx`时，npm会执行以下步骤：

1. **查找并下载创建器包**：
    - npm会从注册表中下载名为`create-xxx`的包。例如，如果你运行`npm create vite`，npm实际上会查找并使用`create-vite`包。
2. **执行创建器包的逻辑**：
    - 下载并安装`create-xxx`包后，npm会运行该包的创建脚本。这通常会涉及到询问用户一些问题（如项目名称、模板选择等），然后根据用户的输入来生成项目结构和文件。

## create-vite 这个包具体做了什么

```shell
npm create vite@latest part1 -- --template react
```

这个命令用于通过Vite创建一个新的React项目。让我们逐步解释每个部分的含义：

1. `vite@latest`确保使用的是最新发布的版本。
2. **part1**: 这是新项目的名称。在这个例子中，项目将被创建在一个名为`part1`的文件夹中。
3. **-- --template react**: 这部分指定了模板。`--template react`告诉Vite使用React模板来初始化项目。这意味着生成的项目将已经配置好React的相关依赖和文件结构。

### 询问用户输入

当你运行 `npm create vite@latest` 时，`create-vite` 包会启动一个命令行交互界面，询问你一些基本问题，比如项目名称、要使用的模板（如 React、Vue、Svelte 等）以及其他配置选项。

### 创建项目目录和文件

- 根据用户输入，`create-vite` 会在指定的目录下生成项目结构和文件。这些文件包括：
- `package.json`：定义项目的元数据和依赖。
- `index.html`：项目的入口 HTML 文件。
- `src` 目录：包含源代码，通常会包含一个基本的 `main.js` 或 `main.ts` 文件，以及一个示例组件。
- 配置文件：如 `vite.config.js` 或 `vite.config.ts`，用于配置 Vite。

### 安装依赖

如果你选择了特定的模板，`create-vite` 会自动添加相关的依赖到 `package.json` 中，并且会提供安装依赖的提示

### 提供运行指令

创建项目后，`create-vite` 会提示你下一步的操作，例如进入项目目录并运行开发服务器的命令（通常是 `npm install` 然后 `npm run dev`）。

## 自己动手写一个脚手架

### 步骤 1：初始化项目

首先，创建一个新的 Node.js 项目：

```sh
mkdir create-myvite
cd create-myvite
npm init -y

```

### 步骤 2：安装依赖

安装所需的依赖库，比如 `inquirer` 用于命令行交互，`fs-extra` 用于文件操作：

```sh
npm install inquirer fs-extra
```

### 步骤 3：编写脚本

index.mjs 文件

```js
#!/usr/bin/env node

import inquirer from 'inquirer';
import fs from 'fs-extra';
import path from 'path';
import { fileURLToPath } from 'url';

// These lines are necessary to get __dirname in an ES module
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

async function createProject() {
  const answers = await inquirer.prompt([
    {
      type: 'input',
      name: 'projectName',
      message: 'Project name:',
      default: 'my-vite-project'
    },
    {
      type: 'list',
      name: 'template',
      message: 'Select a template:',
      choices: ['vanilla', 'react', 'vue']
    }
  ]);

  const { projectName, template } = answers;
  const projectPath = path.join(process.cwd(), projectName);

  if (fs.existsSync(projectPath)) {
    console.error(`Error: Directory ${projectName} already exists.`);
    process.exit(1);
  }

  fs.mkdirSync(projectPath);

  // Create a basic Vite project structure
  fs.writeFileSync(path.join(projectPath, 'index.html'), `<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Vite App</title>
  </head>
  <body>
    <div id="app"></div>
    <script type="module" src="/src/main.js"></script>
  </body>
</html>`);

  let dependencies = {};
  let devDependencies = {
    vite: "^3.0.0"
  };

  const srcDir = path.join(projectPath, 'src');
  fs.mkdirSync(srcDir);

  if (template === 'react') {
    dependencies.react = '^17.0.0';
    dependencies['react-dom'] = '^17.0.0';

    fs.writeFileSync(path.join(srcDir, 'main.jsx'), `import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.createRoot(document.getElementById('app')).render(<App />);`);

    fs.writeFileSync(path.join(srcDir, 'App.jsx'), `import React from 'react';

function App() {
  return <h1>Hello, Vite + React!</h1>;
}

export default App;`);
  } else if (template === 'vue') {
    dependencies.vue = '^3.0.0';
    devDependencies['@vitejs/plugin-vue'] = '^2.0.0';

    fs.writeFileSync(path.join(srcDir, 'main.js'), `import { createApp } from 'vue';
import App from './App.vue';

createApp(App).mount('#app');`);

    fs.writeFileSync(path.join(srcDir, 'App.vue'), `<template>
  <h1>Hello, Vite + Vue!</h1>
</template>

<script>
export default {
  name: 'App'
};
</script>`);

    fs.writeFileSync(path.join(projectPath, 'vite.config.js'), `import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

export default defineConfig({
  plugins: [vue()]
});
`);
  } else {
    fs.writeFileSync(path.join(srcDir, 'main.js'), `document.getElementById('app').innerHTML = '<h1>Hello, Vite!</h1>';`);
  }

  fs.writeFileSync(
    path.join(projectPath, "package.json"),
    JSON.stringify({
      name: projectName,
      version: "0.0.1",
      scripts: {
        dev: "vite",
        build: "vite build",
        serve: "vite preview"
      },
      dependencies,
      devDependencies
    }, null, 2)
  );

  console.log(`Project ${projectName} created successfully.`);
  console.log(`Navigate to the project directory and run 'npm install' to install dependencies.`);
}

createProject();

```

package.json文件

```json
{
  "name": "create-myvite",
  "version": "1.0.0",
  "type": "module",
  "main": "index.mjs",
  "bin": {
    "create-myvite": "./index.mjs"
  },
  "dependencies": {
    "inquirer": "^8.1.2",
    "fs-extra": "^10.0.0"
  }
}

```

### 步骤 4：添加执行权限和链接

使 `index.mjs` 文件可执行，并创建全局链接：

```sh
chmod +x index.mjs
npm link

```

### 运行示例

运行以下命令来创建一个新项目：

```sh
create-myvite
```

## `create-vite` 和 CRA（`create-react-app`）比较

### 相似之处

1. **快速搭建应用程序：** 两者都旨在简化新项目的搭建过程。通过运行一个命令，你可以快速创建一个基本的项目结构，并且可以立即开始编写代码。
2. **现代化的工具链：** 两者都使用了现代化的工具链，包括 Babel、Webpack、ESLint 等，以确保你可以使用最新的 JavaScript 特性，并且具备良好的开发体验。
3. **默认配置：** 默认情况下，它们提供了一个预配置的开发环境，包括热重载、代码分割、生产构建等功能。

### 区别

1. **构建工具：** 最明显的区别是它们使用的构建工具不同。`create-react-app` 使用的是 Webpack，而 `create-vite` 使用的是 Vite。Vite 是一个由 Vue.js 核心团队开发的新型前端构建工具，它利用了现代浏览器对 ES 模块的原生支持，能够实现非常快速的开发构建速度。
2. **模块热更新（HMR）：** `create-vite` 基于 Vite，利用了浏览器原生支持的 ES 模块特性，因此具有更快的热更新速度。而 `create-react-app` 使用的 HMR 则是基于 Webpack 的实现，速度相对较慢。
3. **生态系统：** 由于 `create-react-app` 是由 Facebook 团队维护的，因此它更倾向于与 React 生态系统无缝集成。相比之下，`create-vite` 在刚推出时可能会受到生态系统限制，但由于 Vite 本身已经得到了 Vue.js 社区的广泛支持，因此其生态系统也在不断壮大。
4. **生产构建方式：** `create-react-app` 使用 Webpack 来构建生产环境的代码，而 `create-vite` 则使用 Rollup 来构建生产代码。Rollup 是一个专注于构建 JavaScript 库的工具，通常被认为比 Webpack 更适合用于构建库和框架。

总的来说，`create-vite` 相对于 `create-react-app` 更加轻量、快速，尤其适合于构建 Vue.js 项目或者需要更快速开发体验的应用程序。但在选择工具时，还应考虑到项目的具体需求和团队的熟悉程度。
