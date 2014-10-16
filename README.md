SPG2 Community Rebalance
========================

Starpoint Gemini 2 Community Rebalance Mod

This is a community driven long term project to rebalance the SPG2 Economy and to add more cargo ships, opportunities and scenarios, that any SPG2 modder can contribute to.


Setting Up Your Repo
=====================
There are 2 ways to set up your repo.

1) You can have it in the default folder, and copy across the files to your mod folder when you want to play the mod

Pros - You can keep any existing mods. Cons - You have to copy it across each time

2) You can have it saved in to your mods folder. This means when you update you have the complete files in your mod folder and can play right away, but any /other/ mods you have in the folder will try to be automatically added to the mod, which we cant have happening. 

Pros - Easy to play/update. Cons - Cant have any other mods while developing this one.


Good Modding Practice
=====================
Because there will be lots of different authors, with lots of different ideas, there is a really easy way for us all to keep track of whos code is whos.

At the top of each file, you need to add the following lines

/* Community Rebalance Mod<br>
	- IdeaName (For example, PlayerBounty)<br>
	- By AuthorName (Your name here)<br>
	- ModID (3 letters that identify your mod (Example: PLB)<br>
*/

Then, when it comes to writing to your bit of code, add

/* ModID Start */

and at the end add

/* ModID End */

This should be done for each section of code. If you're writing or editing just one line, add this before and after. If you're writing 10 lines, add this at the start, and at the end.

If you're editing original code, you still need to add it before and after every line you edit.

IMPORTANT! If you're editing someone elses code, that already has the tags, then add your tag after it. Example:

/* PLB Start */<br>
/* Mod1 Start */

--> Code

/* PLB End */<br>
/* Mod1 End */

It may also be useful to give a small summary of what you have edited, although this is optional.


FAQ
====

Q) How do I contribute?

A) There are 2 ways to contribute. If you're a well known SPG2 modder already, then I'll set you up as a contributer, and you can directly edit the files. If you're new to the SPG2 Mod Scene, then you'll need to follow these steps:

1) Create a GitHub account, and preferably, although optional, download the GutHub software.

2) Fork this master repo.

3) Submit any changes you make to your fork.

4) Create a pull request between the masters of both your fork, and this repository.


Enough commits (that don't corrupt files!) and you'll be given contributer status.
