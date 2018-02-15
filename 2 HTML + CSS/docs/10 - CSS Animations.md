
# CSS Animations

Animations allow us to move elements, change their color, change their shape, etc. You can read more about animations on the [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/animation) and [w3schools](https://www.w3schools.com/css/css3_animations.asp).

We can define animations in CSS either by a "from" and a "to" set of styles:

```css
@keyframes example {
    from {background-color: red;}
    to {background-color: yellow;}
}
```

Or by specifying a series of keyframes:

```css
@keyframes example {
    0%   {background-color: red;}
    25%  {background-color: yellow;}
    50%  {background-color: blue;}
    100% {background-color: green;}
}
```



## Animation Properties

| Property | Description |
|--- |--- |
| animation-name | the name of the animation to apply to this element |
| animation-duration | the duration of the animation (`4s` for 4 seconds) |
| animation-delay | the delay before the animation starts, can be negative |
| animation-iteration-count | an integer (`3`, `8`), or `infinite` |
| animation-direction | can be `normal`, `reverse`, `alternate`, or `alternate-reverse` |
| animation-timing-function | controls the timing function, see below for possible values |
| animation-fill-mode | specifies the style for an element when an animation is not playing, see below for possible values |

## Timing Functions 

You can read more about timing functions on the [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/single-transition-timing-function).

| Timing Function | Description |
|--- |--- |
| ease | slow start, fast, slow end |
| linear | consistent speed |
| ease-in | slow start, fast end |
| ease-out | fast start, slow end |
| ease-in-out | slow start and end |
| cubic-bezier(a,b,c,d) | custom speed curve, parameters should be around the range [-1,1] |

## Fill Mode

| Fill Mode | Description |
|--- |--- |
| none (default) | no styles applied when not animating |
| forwards | style set by the last keyframe |
| backwards | style set by the first keyframe, retained during animation delay |
| both | style set to the first keyframe before the animation starts, and set to the last keyframe after the animation ends |
