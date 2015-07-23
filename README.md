PX - REM Translate
======
- by Paul Wang
- 17 June 2015
- e-mail:		paulwang[at]vip[dot]qq[dot]com

---

A Sublime Text plugin that allows easy conversion of rem to px and px to rem.

## Installation
You can easily install the pluing through Will Bond's excellent Package Control (https://sublime.wbond.net/).
If you want to install this plugin manually for some reason, simply clone this repo into your packages directory (make sure not to put it in the user sub dir).

## Instructions



### Converting px to rem
1. Select a code block
2. Hit ctrl+shift+e by default (cmd+shift+e on Mac OS) to convert the value to rem. 

### Converting rem to px
1. Select a code block
2. Hit ctrl+shift+w by default (cmd+shift+w on Mac OS) to convert the value to px. 

## Supported Features
- Batch Convert px values to rem
- Batch Convert rem values to px
- Checks to make sure the value is a valid px unit to convert to rem and visa versa

## Notes
1. The default size of 1rem is 40px which can be changed in the user settings.
2. All values will remove trailing zero's (e.g. '1.500rem' would become '1.5rem').

## Examples (1rem = 40px)

### Example 1 (px to rem)
```css

select a code block for follow code:

body {
	width: 10px 20px 40px 50px;
	margin: 20px;
	color: #fff;
	padding: 10px 3px;
}

will conver to:

body {
	width: 0.625rem 1.25rem 2.5rem 3.125rem;
	margin: 1.25rem;
	color: #fff;
	padding: 0.625rem 0.1875rem;
}



### Example 2 (rem to px)

```css
body {
	width: 0.625rem 1.25rem 2.5rem 3.125rem;
	margin: 1.25rem;
	color: #fff;
	padding: 0.625rem 0.1875rem;
}

will conver to:


body {
	width: 10px 20px 40px 50px;
	margin: 20px;
	color: #fff;
	padding: 10px 3px;
}
