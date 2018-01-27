This blog is personal learning note for free online courses offered by Udacity.

Click [URL for course](https://cn.udacity.com/course/reinforcement-learning--ud600) to go to the course.

[toc]

# Lesson 2

## Decision Making and Reinforcement Learning

Differences between three kinds of learning:

- Supervised learning: It takes the form of function approximation,where we are given a bunch of x, y pairs, and our goal is to  find a function f that will map some new x to a proper y; 

- Unsupervised learning: Similar to supervised learning. It turns out that we're given a bunch of x's, and our goal is to find some f that gives us a compact descriptions of the set of x's that we've seen. So we call this clustering or description as opposed to function approximation.

- Reinforcement learning: Superficially it looks a lot like supervised learning, in which we're going to be given a string of pairs of data, and we're going to try to learn some functions. Then in supervised learning, we would be given a bunch of X and Y pairs and are asked to learn function f. But in reinforcement learning, we're instead going to be given x's and z's (the meaning of them will be told then).

You may notice our title for this part, the relation between decision making and reinforcement learning (RL) is that: RL is one mechanism for doing decision making.

![](1.png)

## Warm up: The World

As is shown in below picture, We set a world as a king of game, where a player has a start state, and it is only able to execute actions (one of there four: up, down, left and right). And the purpose is to wonder around this world in such a way that eventually you make it to the **little green spot**. Simultaneously, under all circumstances, we must avoid the red spot. That is to say, if you enter into the green spot, the game is over; if you enter into the red spot, the game is also over.

Notice if you find yourself at a boundary, you can't move toward the direction where boundary is.

Besides, black spot is a place we can't enter into, so it acts just like a wall.

![](2.png)

**Question 1 comes out: What is the shortest sequence getting from start to goal?**

we got two correct answers:

- U U R R R
- R R U U R

![](3.png)


- Now we are going to make some changes to the World: introduce uncertainty/stochasticity

That is: **When we execute an action, it executes correctly with probability of 0.8**. So 80% of the time, if we go up, it goes up and the same for left and right directions. **Now 20% of the time, the action we take actually causes you to move at a right angle.**  Now that 20% gets a distributed uniformally.

For example: if you try to go up at the start state, you have a 80% chance of moving up, and have a 10% chance of moving to the right, and 10% of moving to the left but we'd bump the wall (so actually would stay at start state).


**Question 2 comes out: What is the reliability of our answer sequence U U R R R? (The reliability here means the probability of it actually succeeding in going from start state to the green spot)**

answer: 0.32776=$0.8^5 (=0.32768, means taking 5 actions smoothly)+ 0.1*0.1*0.1*0.1*0.8 (=0.00008, means former four actions being abnormal, and the last action working well)$.


This is actually a warm up for following method which is to solve decision making problems where uncertainty exists.

## Markov Decison Processes

![](4.png)

It's describes a framework to capture the problem world:

- STATES: s
- MODEL: T(s,a,$s'$) ~ Pr($s'$|s,a)
- ACTIONS: A(s),A
- REWARD: R(s), R(s,a), R(s,a,$s'$)
***
- Policy: $\pi(s)->a$

STATE means a set of tokens, it represents every possible state one could be in. In the World we mentioned above, every grid could be seen as a state s (so we have 12 different states in the World).

ACTiONS are what you are allowed to do in a particular state s (up down left right). 

MODELS describes rules of the game that you're playing (Physics of the World). T(s,a,$s'$) is a function that produces probability that you will end up transitioning the $s'$ given that you were in state s, and you took action a.

> For example, in earliest deterministic World, if we try to go up at the start state, T(s,a,$s'$) would produce 100% when $s'$ is (1,2) (taking start state as (1,1)). While in uncertain World, if we try to go up at the start state, T(s,a,$s'$) would produce 80% when $s'$ is (1,2), and 10% when $s'$ is (2,1), and 10% when $s'$ is (1,1) (moves to the left but bump the boundary).

- Markov Property

![](5.png)

**Only the present matters!**

This property is showed in our transition function, because it shows that **the probability you end up in some state $s'$, given that you're in state s and took action A, only depends on the current state S.**


