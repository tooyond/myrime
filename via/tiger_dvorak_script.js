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
      case 'q': return 's..'
      case 'w': return 'v..'
      case 'e': return 'w..'
      case 'r': return 'p..'
      case 't': return 'y..'
      case 'y': return 'f..'
      case 'u': return 'g..'
      case 'i': return 'c..'
      case 'o': return 'r..'
      case 'p': return 'l..'
      case 'a': return 'a..'
      case 's': return 'o..'
      case 'd': return 'e..'
      case 'f': return 'u..'
      case 'g': return 'i..'
      case 'h': return 'd..'
      case 'j': return 'h..'
      case 'k': return 't..'
      case 'l': return 'n..'
      case 'z': return 'z..'
      case 'x': return 'q..'
      case 'c': return 'j..'
      case 'v': return 'k..'
      case 'b': return 'x..'
      case 'n': return 'b..'
      case 'm': return 'm..'
      case ' ': return '   '
      default: return 's'
    }
  }

  setInterval(function name(params) {
    var a = document.querySelector("body > div:nth-child(1) > main > div > main > div > div > div > div > div > div > span:nth-child(2)")
    var sarr = a.textContent.split('')
    var text = a.textContent
    if (sarr.length == 0) return
    if (sarr.length == 1)
      text = transform(sarr[0])
    if (sarr.length == 2)
      text = transform(sarr[0]) + transform(sarr[1])
    a.textContent = text
  }, 100)
})();