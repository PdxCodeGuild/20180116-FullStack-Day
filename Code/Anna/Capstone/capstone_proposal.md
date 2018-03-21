# IFF (If and Only If) ⇔

_In logic and related fields such as mathematics and philosophy, if and only if (shortened iff) is a biconditional logical connective between statements._ (Wikipedia) :metal:

IFF is an online "get to do" list rather than a to do list. You get to do a thing _if and only if_ you complete the task or tasks you need to do.

## Project Overview

Traditional to do lists are typically comprised of unpleasant tasks or chores that need to be done, with no system of rewards. [Studies](https://lifehacker.com/beat-procrastination-with-temptation-bundling-1781175382) [have](http://opim.wharton.upenn.edu/~kmilkman/2013_Mgmt_Sci.pdf) [shown](http://www.bbc.com/capital/story/20170927-a-unique-way-to-get-work-done) that temptation bundling, or coupling an unpleasant task with a reward, is a more effective way to get things done. IFF will allow users to combine pleasant and unpleasant tasks, and use accountability as a motivating tool.

The IFF website will allow users to create an account, in which they will be able to store multiple "get to do" lists. Each list will have one "get to do" task and one or more "to do" tasks. As the "to do" tasks are checked off, the "get to do" task becomes available.

**Example list:**

I get to: 
- [ ] play Xbox for one hour

IFF I: 
- [ ] clean the garage
- [x] send the final proposal to my boss
- [ ] work on my app for one hour

IFF will use Django in the backend to store user accounts and user lists. It will use VueJS in the frontend to display each list and provide basic functionality.

**Core technologies:**
- Django backend
- PostgreSQL for the user and list database
- VueJS frontend
- Materialize CSS for style
- Deploy on Heroku/AWS (tbd)

**Potential users**:

- Employees with set daily tasks
- Anyone who needs to do chores at home
- People trying to get in shape/lose weight can reward themselves for going to the gym, etc.
- Parents who want to give their kids incentives to do their chores
- Anyone who currently uses a to do list app

**Monetization**: While the app will be launched as a free service initially, future monetization is possible via the following:

- Paid account levels with additional features: 
    - Free accounts can be capped at ~10 lists at a time, while monthly subscribers get unlimited lists and possible additional features such as shared lists.
- Paid iOS/Android app:
    - Future iOS/Android versions can be downloaded from app stores for a fee
    
## Functionality
The user starts on the landing page, which will look like so:

![Image of landing page](https://octodex.github.com/images/yaktocat.png)


