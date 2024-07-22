// ==UserScript==
// @name         虎码字根练习
// @namespace    https://viayoo.com/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @run-at       document-start
// @match        https://tiger-code.com/practice/base
// @grant        none
// ==/UserScript==

(function () {
  'use strict';

  // Your code here...  
  function transform(s) {
    switch (s) {
      case 'q': return '都'
      case 'w': return '得'
      case 'e': return '也'
      case 'r': return '了'
      case 't': return '我'
      case 'y': return '到'
      case 'u': return '的'
      case 'i': return '为'
      case 'o': return '是'
      case 'p': return '行'
      case 'a': return '来'
      case 's': return '说'
      case 'd': return '中'
      case 'f': return '一'
      case 'g': return '就'
      case 'h': return '道'
      case 'j': return '人'
      case 'k': return '能'
      case 'l': return '而'
      case 'z': return '可'
      case 'x': return '和'
      case 'c': return '不'
      case 'v': return '要'
      case 'b': return '如'
      case 'n': return '在'
      case 'm': return '大'
      default: return s
    }
  }

  setInterval(function name(params) {
    var a = document.querySelector("body > div:nth-child(1) > main > div > main > div > div > div > div > div > div > span:nth-child(2)")
    var sarr = a.textContent.split('')
    if (sarr.length != 2) return
    var text2 = transform(sarr[0]) + transform(sarr[1])
    a.textContent = text2
  }, 500)
})();