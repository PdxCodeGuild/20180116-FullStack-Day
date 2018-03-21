# IFF (If and Only If) ⇔

_In logic and related fields such as mathematics and philosophy, if and only if (shortened iff) is a biconditional logical connective between statements._ (Wikipedia) :metal:

IFF is an online "get to do" list rather than a to-do list. You get to do a thing _**if and only if**_ you complete the task or tasks you need to do.

## Project Overview

Traditional to-do lists are typically comprised of unpleasant tasks or chores that need to be done, with no system of rewards. [Studies](https://lifehacker.com/beat-procrastination-with-temptation-bundling-1781175382) [have](http://opim.wharton.upenn.edu/~kmilkman/2013_Mgmt_Sci.pdf) [shown](http://www.bbc.com/capital/story/20170927-a-unique-way-to-get-work-done) that temptation bundling, or coupling an unpleasant task with a reward, is a more effective way to get things done. IFF will allow users to combine pleasant and unpleasant tasks, and use social accountability as a motivating tool.

The IFF website will allow users to create an account, in which they will be able to store multiple "get-to-do" lists. Each list will have one get-to-do task and one or more to-do tasks. As the to-do tasks are checked off, the get-to-do task becomes available.

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
- Anyone who currently uses a to-do list app

**Monetization**: While the app will be launched as a free service initially, future monetization is possible via the following:

- Paid account levels with additional features: 
    - Free accounts can be capped at ~10 lists at a time, while monthly subscribers get unlimited lists and possible additional features such as shared lists.
- Paid iOS/Android app:
    - Future iOS/Android versions can be downloaded from app stores for a fee
    
## Functionality
The user starts on the landing page, which will look like so:

![Image of landing page](https://raw.githubusercontent.com/PdxCodeGuild/20180116-FullStack-Day/32fb93dacbb08965f67cddb6c3ed06fc6ba41625/Code/Anna/Capstone/mockup/img/Screen%20Shot%202018-03-21%20at%2015.33.26.png)

A user signs up, and creates their first IFF list. They enter one get-to-do and how ever many to-dos they want.

Once a user has an account, their home screen shows a list of all of their IFF lists. If they click on one, they go to a detail page where they can see all their to-do items and can check them off. If all of a get-to-do's to-do items are checked off, they get a message saying they can now do their reward task, and the whole list disappears.

Users can also have a history (archive) of all of the things they've done and have gotten to do in the past.

## Data Model

There are two main data models:
1. User
2. IFF Task

The User model includes the user's login information, a profile picture, and all of their active and archived IFF lists. Future versions of IFF will add a social media aspect to the user profile, connecting users as friends and letting them see each others' IFF lists and even keep each other accountable by verifying that the to-do tasks were in fact completed (via photo or something like that).

The IFF Task model is just one get-to-do item followed by at least one to-do item. Each new task is an instance of the IFF model.

## Schedule

#### Milestone 1
_Due date: March 30th_

Entire project is set up, including installing Webpack, Django, and Vue and getting them to play nicely together in a virtual env. A rough front-end including the landing page and user log-in screen is completed.
#### Milestone 2
_Due date: April 6th_

Ability for users to register and add lists is complete. It doesn't have to look pretty yet.
#### Milestone 3
_Due date: April 13th_(Capstone presentation day)

An MVP of IFF is deployed and live, with the ability for users to sign up. The frontend is finalized.
#### Milestone 4
_Due date: April 20th_

User testing and debugging with actual users.
#### Milestone 5
_Due date: May 31st_

All bugs fixed and mass roll-out of platform. Functionality limited to signing up and adding up to 10 IFF lists at a time.
#### Milestone 6
_Due date: Fall 2018_

Add social aspect to platform. Users can become friends, invite their friends, and show lists to friends who will keep them accountable.
#### Milestone 7
_Due date: end of 2018_

Monetization of platform. Add premium monthly plan for unlimited lists.
#### Milestone 8
_Due date: Q1 2019_

Monetization of platform. Add team premium tier where multiple people can share lists.
#### Milestone 9
_Due date: Q2 2019_

Launch iOS and Android apps.
#### Milestone 10
_Due date: ?_

Sell IFF to Mark Zuckerberg and retire to a private island.

