---
title: "Solidity语言基础入门 1"
date: 2024-06-22T09:54:41+08:00
draft: false
showSummary: false
description: "本文介绍"
tags: ["技术","Solidity","智能合约"]
categories: ["Solidity"]
keywords:
  - "Solidity"
  - "智能合约"
---

本文主要认识 Solidity 语言的基础用法，包括：

1. 基础数据类型
2. 定义函数
3. 数组和 strucs
4. 错误和警告
5. Memory storage 和 calldata
6. mappings
7. 部署智能合约

## 快速上手

本文因为是基础上手，所以直接使用 [Remix 在线编辑器](https://remix.ethereum.org/)。

删除所有文件，然后新建一个 SimpleStorage.sol 的文件，`.sol` 是 Solidity 语言文件的后缀名。

```sol
// SPDX-License-Identifier: MIT
pragma solidity 0.8.18; // solidity versions

contract SimpleStorage {

}
```

- 开源标识符 // SPDX-License-Identifier: MIT
- 表明 Solidity 语言的版本声明 `pragma solidity ^0.8.18;` 0.8.18 表示版本号，^ 符号表示 大于等于0.8.18版本是ok的
- contract 关键词是智能合约的标识符， 名称SimpleStorage 约定俗成和文件名保持一致，contract 类似 js 语言中的类。

## 基础数据类型

- Integers 整数类型
  - uint 无符号整型，数字前不可以有正负号
  - int 有符号整型， 可以带正负号
- Booleans 布尔类型
  - bool 值有 true 和 false
- String 字符串类型
  - string

这里我们只介绍常用的数据类型，更多的用法可以查看 [Solidity 官方文档](https://docs.soliditylang.org/en/v0.8.26/types.html)

## 定义函数

```sol
function store(uint256 _likeNumber) public virtual  {
    likeNumber = _likeNumber;
} // Note that function the curly brackets {} not add ";"

function retrieve () public view returns(uint256) {
    return likeNumber;
}

function getPureNumber () public pure returns(uint256) {
    return 999;
}
```

## 数组和 strucs

```sol

struct Student {
    uint256 number;
    string name;
}
// static array
// Student[3] public listOfStudent;
// dynamic array
Student[] public listOfStudent;
Student public tom =  Student(42, 'Tom');
Student public lily =  Student({number: 11, name: 'Lily'});

```

## 错误和警告

错误表示编写的代码无法通过编译器的编译，不可以正常发布到的服务器上。

警告则表示没有按照约定的规范去写代码，但是不影响编译，可以正常部署。

## Memory storage 和 calldata

## mappings

```sol
// mapping 映射关系 tom --> 88
mapping (string => uint256) public nameToNumber;

function addStudent(string memory _name, uint _number) public  {
    Student memory newStudent = Student(_number, _name);
    // listOfStudent.push(Student(_number, _name));
    listOfStudent.push(newStudent);
    // Adding someone to the mapping
    nameToNumber[_name] = _number;
}

```

## 部署智能合约

这里我们需要安装一下 MateMask 钱包插件。
