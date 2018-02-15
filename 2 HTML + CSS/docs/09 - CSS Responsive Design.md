
# CSS Responsive Design

With the uniquity of smart phones and tablets, it's imperative that your website adapts to whatever device a user has. One option is to check the screen width or the [user agent](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent), and redirect to a mobile version of the site (example [here](https://css-tricks.com/snippets/javascript/redirect-mobile-devices/)). The problem with this approach is that you have to maintain two versions of the same site.

A better approach is to have your website resize to match any screen, this is called "responsive design". You can read more about responsive design on [MDN](https://developer.mozilla.org/en-US/Apps/Progressive/Responsive/responsive_design_building_blocks) and [w3schools](https://www.w3schools.com/css/css_rwd_intro.asp).

Many [CSS frameworks](03%20-%20CSS%20Overview.md#css-frameworks) have responsiveness built-in. [Flexbox and CSS Grid](08%20-%20CSS%20Flexbox%20+%20Grid.md) also help, particularly when paired with [auto-fill and auto-fit](https://css-tricks.com/auto-sizing-columns-css-grid-auto-fill-vs-auto-fit/).

To help you test, the major browsers have tools which let you change your browser's size to match that of phones and tablets: [firefox](https://developer.mozilla.org/en-US/docs/Tools/Responsive_Design_Mode), [chrome](https://developers.google.com/web/tools/chrome-devtools/device-mode/emulate-mobile-viewports), and [safari](https://support.apple.com/kb/PH26266?locale=en_US). There are also various browser extensions which have additional features: [firefox](https://addons.mozilla.org/en-US/firefox/addon/window-resizer-webextension/), [chrome](https://chrome.google.com/webstore/detail/window-resizer/kkelicaakdanhinjdeammmilcgefonfh?hl=en), [safari](http://resizesafari.com/).


## Media Queries

Media queries let you control what style rules are applied when certain conditions are present. This can include the width of the page, the orientation, the aspect ratio, etc. You can read more about media queries on the [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Media_Queries/Using_media_queries) and [here](https://www.w3schools.com/cSS/css_rwd_mediaqueries.asp). You can view a list of each feature on the [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/@media).

| Media Type | Description |
|--- |--- |
| `all` | used for all devices |
| `print` | used when a page is printed |
| `screen` | used when the page is displayed on a screen |
| `speech` | used for speech synthesizers |

| Parameter | Description |
|--- |--- |
| `color`, `monochrome` | whether the device is color or monochrome (ereaders) |
| `min-width`, `min-height` | applies when the screen's size is greater |
| `max-width`, `max-height` | applies when the screen's size is lesser |
| `orientation` | either `portrait` or `landscape` |
| `aspect-ratio` | e.g. `16/9`, `4/3`, etc |

| Operator | Description |
|--- |--- |
| `,` | applies to multiple situations |
| `and` | applies only when both conditions are present |
| `not` | applies only when a condition is not present |

e.g.

```css
@media screen and (min-width: 30em) and (orientation: landscape) { ... }
```
